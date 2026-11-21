/* Moteur d'animation de nœuds : corde en relief (dégradés, ombres, reflets), tracé exact dessus/dessous,
   progression pas à pas, légendes. Aucune dépendance. */
(function(root){
'use strict';
var NS='http://www.w3.org/2000/svg';
function el(n,a,p){var e=document.createElementNS(NS,n);for(var k in a)e.setAttribute(k,a[k]);if(p)p.appendChild(e);return e}

/* ---------- géométrie ---------- */
function segInt(a,b,c,d){ /* intersection de [a,b] et [c,d] */
  var r1x=b.x-a.x,r1y=b.y-a.y,r2x=d.x-c.x,r2y=d.y-c.y,den=r1x*r2y-r1y*r2x;
  if(Math.abs(den)<1e-9)return null;
  var t=((c.x-a.x)*r2y-(c.y-a.y)*r2x)/den,u=((c.x-a.x)*r1y-(c.y-a.y)*r1x)/den;
  if(t<0||t>=1||u<0||u>=1)return null;return{t:t,u:u};
}
function crossings(P,closed){
  var n=P.length,out=[],m=closed?n:n-1;
  for(var i=0;i<m;i++){var a=P[i],b=P[(i+1)%n];
    for(var j=i+2;j<m;j++){ if(closed&&i===0&&j===m-1)continue;
      var h=segInt(a,b,P[j],P[(j+1)%n]);
      if(h){var zi=a.z+(b.z-a.z)*h.t,zj=P[j].z+(P[(j+1)%n].z-P[j].z)*h.u;
        out.push({i:i+h.t,j:j+h.u,over:zi>zj?'i':'j'})}}}
  return out;
}
/* déterminant de Fox (validation de topologie d'un nœud fermé) */
function foxDet(P){
  var cr=crossings(P,true),ev=[];
  cr.forEach(function(c,k){ev.push({s:c.i,k:k,o:c.over==='i'});ev.push({s:c.j,k:k,o:c.over==='j'})});
  ev.sort(function(a,b){return a.s-b.s});
  var n=cr.length;if(n===0)return 1;
  var arcOf=[],cur=0,rows=[];for(var k=0;k<n;k++)rows.push({o:0,b:0,a:0});
  ev.forEach(function(e){ if(e.o){rows[e.k].o=cur}else{rows[e.k].b=cur;cur++;rows[e.k].a=cur} });
  var arcs=cur;/* nombre d'arcs = n */
  var M=[];rows.forEach(function(r){var v=new Array(arcs).fill(0);v[r.o%arcs]+=2;v[r.b%arcs]-=1;v[r.a%arcs]-=1;M.push(v)});
  var A=M.slice(1).map(function(v){return v.slice(1)});var N=A.length,det=1;
  for(var c=0;c<N;c++){var p=c;for(var r=c+1;r<N;r++)if(Math.abs(A[r][c])>Math.abs(A[p][c]))p=r;
    if(Math.abs(A[p][c])<1e-9)return 0;if(p!==c){var t=A[p];A[p]=A[c];A[c]=t;det=-det}
    det*=A[c][c];for(var r2=c+1;r2<N;r2++){var f=A[r2][c]/A[c][c];for(var q=c;q<N;q++)A[r2][q]-=f*A[c][q]}}
  return Math.round(Math.abs(det));
}
/* ouvre un nœud fermé : coupe au point c (indice), ajoute deux brins libres */
function openKnot(P,c,gap,tailLen,spread){
  var n=P.length,pts=[];
  if(c<0){var mx=0,cx0=0,cy0=0;P.forEach(function(p){cx0+=p.x;cy0+=p.y});cx0/=n;cy0/=n;P.forEach(function(p,i){var d=Math.hypot(p.x-cx0,p.y-cy0);if(d>mx){mx=d;c=i}})}
  for(var k=gap;k<n-gap;k++)pts.push(P[(c+k)%n]);
  var cx=0,cy=0;P.forEach(function(p){cx+=p.x;cy+=p.y});cx/=n;cy/=n;
  function tail(E,F,sign){ /* E extrémité, F voisin intérieur */
    var tx=E.x-F.x,ty=E.y-F.y,tl=Math.hypot(tx,ty);tx/=tl;ty/=tl;
    var ox=E.x-cx,oy=E.y-cy,ol=Math.hypot(ox,oy);ox/=ol;oy/=ol;
    var res=[],x=E.x,y=E.y,steps=Math.round(tailLen/4);
    for(var s=1;s<=steps;s++){var w=Math.min(1,s/20);
      var dx=tx*(1-w)+ (ox*0.8+(-oy)*sign*spread)*w,dy=ty*(1-w)+(oy*0.8+ox*sign*spread)*w;var dl=Math.hypot(dx,dy);dx/=dl;dy/=dl;
      x+=dx*4;y+=dy*4;res.push({x:x,y:y,z:E.z})}
    return res;}
  var e1=pts[0],f1=pts[1],e2=pts[pts.length-1],f2=pts[pts.length-2];
  var t1=tail(e1,f1,-1).reverse(),t2=tail(e2,f2,1);
  return t1.concat(pts,t2);
}
function fit(P,box){ /* recadre dans box {x,y,w,h} */
  var x0=1e9,y0=1e9,x1=-1e9,y1=-1e9;P.forEach(function(p){x0=Math.min(x0,p.x);x1=Math.max(x1,p.x);y0=Math.min(y0,p.y);y1=Math.max(y1,p.y)});
  var s=Math.min(box.w/(x1-x0),box.h/(y1-y0)),ox=box.x+(box.w-(x1-x0)*s)/2-x0*s,oy=box.y+(box.h-(y1-y0)*s)/2-y0*s;
  return P.map(function(p){return{x:p.x*s+ox,y:p.y*s+oy,z:p.z*s}});
}
function arclen(P){var s=[0];for(var i=1;i<P.length;i++)s.push(s[i-1]+Math.hypot(P[i].x-P[i-1].x,P[i].y-P[i-1].y));return s}
function resample(P,step){var s=arclen(P),L=s[s.length-1],n=Math.max(2,Math.round(L/step)),out=[],j=0;
  for(var k=0;k<=n;k++){var t=L*k/n;while(j<s.length-2&&s[j+1]<t)j++;var u=(t-s[j])/Math.max(1e-9,s[j+1]-s[j]);
    out.push({x:P[j].x+(P[j+1].x-P[j].x)*u,y:P[j].y+(P[j+1].y-P[j].y)*u,z:P[j].z+(P[j+1].z-P[j].z)*u})}return out}

/* ---------- rendu ---------- */
function defs(svg,id,pal){
  var d=el('defs',{},svg);
  var bg=el('linearGradient',{id:id+'bg',x1:0,y1:0,x2:0,y2:1},d);el('stop',{offset:0,'stop-color':'#f4f8fb'},bg);el('stop',{offset:1,'stop-color':'#d5e2ec'},bg);
  var b1=el('filter',{id:id+'b1',filterUnits:'userSpaceOnUse',x:0,y:0,width:800,height:450},d);el('feGaussianBlur',{stdDeviation:2.2},b1);
  var b2=el('filter',{id:id+'b2',filterUnits:'userSpaceOnUse',x:0,y:0,width:800,height:450},d);el('feGaussianBlur',{stdDeviation:5},b2);
  var b3=el('filter',{id:id+'b3',filterUnits:'userSpaceOnUse',x:0,y:0,width:800,height:450},d);el('feGaussianBlur',{stdDeviation:1},b3);
  var sh=el('filter',{id:id+'sh',filterUnits:'userSpaceOnUse',x:0,y:0,width:800,height:450},d);el('feGaussianBlur',{stdDeviation:7},sh);
  var mt=el('linearGradient',{id:id+'mt',x1:0,y1:0,x2:0,y2:1},d);
  [['0','#ffffff'],['.25','#c9d3da'],['.55','#8e9aa4'],['1','#4b5560']].forEach(function(s){el('stop',{offset:s[0],'stop-color':s[1]},mt)});
  return d;
}
function pathD(P,a,b){var d='';for(var i=a;i<=b;i++)d+=(i===a?'M':'L')+P[i].x.toFixed(1)+' '+P[i].y.toFixed(1);return d}

function Knot(container,cfg){
  var id='k'+Math.random().toString(36).slice(2,7),W=cfg.width||800,H=cfg.height||450,pal=cfg.palette||{dark:'#06223a',mid:'#075b9b',light:'#4aa3dc',hi:'#bfe3fa',acc:'#ec168c'};
  var P=cfg.points,n=P.length,S=arclen(P),L=S[n-1],rw=cfg.ropeWidth||21;
  var stepLen=L/(n-1),Wn=Math.ceil(rw*1.35/stepLen);
  var cr=crossings(P,false),wins=[];
  cr.forEach(function(c){var k=c.over==='i'?c.i:c.j;var a=Math.max(0,Math.floor(k)-Wn),b=Math.min(n-1,Math.ceil(k)+Wn);wins.push({a:a,b:b})});
  var svg=el('svg',{viewBox:'0 0 '+W+' '+H,role:'img','aria-label':cfg.title,class:'kn-svg'});
  defs(svg,id,pal);
  el('rect',{width:W,height:H,fill:'url(#'+id+'bg)',rx:14},svg);
  /* objet fixe (barre, anneau…) : dessiné avant/après la corde selon cfg.objects */
  var gBack=el('g',{},svg);if(cfg.drawBack)cfg.drawBack(gBack,id,el);
  var gRope=el('g',{},svg),gFront=el('g',{},svg);if(cfg.drawFront)cfg.drawFront(gFront,id,el);
  function hex(c){return[1,3,5].map(function(i){return parseInt(c.substr(i,2),16)})}
  function mix(c1,c2,t){var a=hex(c1),b=hex(c2);return'rgb('+a.map(function(v,i){return Math.round(v+(b[i]-v)*t)}).join(',')+')'}
  var layers=[{w:rw+9,c:'#0b1d2c',o:.30,f:'sh',dy:8,dx:5,base:true},{w:rw+2.6,c:pal.dark,o:1}];
  for(var q=0;q<=7;q++){var t=q/7;layers.push({w:rw*(1-.80*t)-0.4*(q===0?0:0),c:t<.5?mix(pal.mid,pal.light,t*2):mix(pal.light,pal.hi,(t-.5)*2),o:1,dx:-1.4*t,dy:-3.4*t})}
  layers.push({w:rw*.12,c:'#ffffff',o:.85,dx:-2.2,dy:-4.6});
  layers.push({w:rw,c:'#000',o:.10,dash:'2.6 5.0'});
  function addPiece(a,b,withShadow){
    var els=[],g=el('g',{},gRope);
    layers.forEach(function(l,li){
      if(li===0&&!withShadow&&false)return;
      if(l.base&&!withShadow)return;var attrs={fill:'none',stroke:l.c,'stroke-width':l.w,'stroke-linecap':'round','stroke-linejoin':'round',opacity:l.o};
      if(l.f)attrs.filter='url(#'+id+l.f+')';if(l.dash){attrs['stroke-dasharray']=l.dash;attrs['stroke-linecap']='butt'}
      if(!withShadow&&li===1)attrs['stroke-linecap']='butt';
      var p=el('path',attrs,g);if(l.dx||l.dy)p.setAttribute('transform','translate('+(l.dx||0)+' '+(l.dy||0)+')');els.push(p)});
    return{a:a,b:b,els:els,shadowOnly:false};
  }
  var base=addPiece(0,n-1,true),pieces=wins.map(function(w){return addPiece(w.a,w.b,false)});
  /* ombre d'occlusion sous les passages dessus */
  var occ=wins.map(function(w){return el('path',{fill:'none',stroke:'#071a29','stroke-width':rw+16,'stroke-linecap':'round',opacity:.34,filter:'url(#'+id+'b2)'},gRope)});
  /* réordonne : base, puis (ombre, pièce) pour chaque passage dessus */
  gRope.appendChild(base.els[0].parentNode);
  wins.forEach(function(w,k){gRope.appendChild(occ[k]);gRope.appendChild(pieces[k].els[0].parentNode)});
  var tip=el('circle',{r:rw*.95,fill:'none',stroke:pal.acc,'stroke-width':3,opacity:0},svg);
  var tag=el('g',{},svg);

  var ctrl={p:0,step:0};
  function render(p){
    var cut=Math.max(0,Math.min(n-1,Math.round(p*(n-1))));
    function setPiece(pc,a,b){var hi=Math.min(b,cut);
      var d=(hi>a)?pathD(P,a,hi):'M0 0';pc.els.forEach(function(e){e.setAttribute('d',d)})}
    setPiece(base,0,n-1);pieces.forEach(function(pc){setPiece(pc,pc.a,pc.b)});
    occ.forEach(function(o,k){var w=wins[k],hi=Math.min(w.b,cut);o.setAttribute('d',hi>w.a?pathD(P,w.a,hi):'M0 0')});
    var T=P[cut];tip.setAttribute('cx',T.x);tip.setAttribute('cy',T.y);tip.setAttribute('opacity',p>0&&p<1?.95:0);
  }
  render(0);
  /* légendes / commandes */
  var steps=cfg.steps,wrap=document.createElement('div');wrap.className='kn-anim';
  var cap=document.createElement('div');cap.className='kn-cap';cap.setAttribute('aria-live','polite');
  var bar=document.createElement('div');bar.className='kn-ctl';
  bar.innerHTML='<button type="button" class="btn alt" data-a="prev">← Précédente</button><button type="button" class="btn" data-a="play">▶ Lecture</button><button type="button" class="btn alt" data-a="next">Suivante →</button><button type="button" class="btn alt" data-a="re">↺ Recommencer</button>';
  var dots=document.createElement('ol');dots.className='kn-dots';
  steps.forEach(function(s,i){var li=document.createElement('li');var b=document.createElement('button');b.type='button';b.textContent=i+1;b.setAttribute('aria-label','Étape '+(i+1)+' : '+s.t);li.appendChild(b);dots.appendChild(li);b.addEventListener('click',function(){stop();goTo(i,true)})});
  wrap.appendChild(svg);wrap.appendChild(dots);wrap.appendChild(cap);wrap.appendChild(bar);container.appendChild(wrap);
  var reduce=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var raf=0,playing=false,timer=0;
  function ease(t){return t<.5?2*t*t:1-Math.pow(-2*t+2,2)/2}
  function showCap(i){var s=steps[i];cap.innerHTML='<strong>Étape '+(i+1)+' / '+steps.length+' · '+s.t+'</strong><p>'+s.d+'</p>'+(s.w?'<p class="kn-warn">'+s.w+'</p>':'');
    [].forEach.call(dots.querySelectorAll('button'),function(b,j){b.setAttribute('aria-current',j===i?'step':'false');b.className=j<i?'done':''})}
  function tween(to,done){cancelAnimationFrame(raf);var from=ctrl.p;if(reduce||from===to){ctrl.p=to;render(to);if(done)done();return}
    var dur=Math.max(500,Math.abs(to-from)*L*4.2),t0=performance.now();
    (function f(t){var u=Math.min(1,(t-t0)/dur);ctrl.p=from+(to-from)*ease(u);render(ctrl.p);if(u<1)raf=requestAnimationFrame(f);else if(done)done()})(t0)}
  function goTo(i,anim,done){ctrl.step=i;showCap(i);var to=steps[i].p;if(anim)tween(to,done);else{ctrl.p=to;render(to);if(done)done()}}
  function stop(){playing=false;clearTimeout(timer);bar.querySelector('[data-a=play]').textContent='▶ Lecture'}
  function play(){playing=true;bar.querySelector('[data-a=play]').textContent='❚❚ Pause';
    (function nxt(){if(!playing)return;if(ctrl.step>=steps.length-1){stop();return}
      goTo(ctrl.step+1,true,function(){timer=setTimeout(nxt,reduce?1500:900)})})()}
  bar.addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;var a=b.dataset.a;
    if(a==='prev'){stop();goTo(Math.max(0,ctrl.step-1),true)}
    else if(a==='next'){stop();goTo(Math.min(steps.length-1,ctrl.step+1),true)}
    else if(a==='re'){stop();ctrl.step=0;ctrl.p=0;render(0);goTo(0,false)}
    else if(a==='play'){if(playing)stop();else{if(ctrl.step>=steps.length-1){ctrl.step=0;ctrl.p=0;render(0);showCap(0)}play()}}});
  goTo(cfg.startStep===undefined?0:cfg.startStep,false);
  return{goTo:goTo,render:render,points:P,crossings:cr};
}

root.KnotAnim={create:Knot,crossings:crossings,foxDet:foxDet,openKnot:openKnot,fit:fit,resample:resample,arclen:arclen};
if(typeof module!=='undefined')module.exports=root.KnotAnim;
})(typeof window!=='undefined'?window:globalThis);
