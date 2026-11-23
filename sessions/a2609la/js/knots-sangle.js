/* Nœud de sangle (nœud d'eau) : nœud simple validé, suivi en sens inverse par l'autre extrémité (câble à plat). */
(function(root){
'use strict';
var K=root.KnotAnim,G=root.KnotGeo;
function unit(x,y){var l=Math.hypot(x,y)||1;return[x/l,y/l]}
function build(cutOff,gs,sgn,blend){
  var D=17,P=K.fit(G.overhand(1500),{x:200,y:115,w:380,h:240}),n=P.length;
  var T=P.map(function(p,i){var a=P[(i-1+n)%n],b=P[(i+1)%n];return unit(b.x-a.x,b.y-a.y)});
  var cx=0,cy=0;P.forEach(function(p){cx+=p.x;cy+=p.y});cx/=n;cy/=n;
  var c0=0,md=0;P.forEach(function(p,i){var d=Math.hypot(p.x-cx,p.y-cy);if(d>md){md=d;c0=i}});
  var cut=(c0+cutOff+n)%n,st=(cut+gs)%n,en=(cut-gs+n)%n,len=(en-st+n)%n;
  function arc(sign){var o=[];for(var k=0;k<=len;k++){var i=(st+k)%n,t=T[i];o.push({x:P[i].x+sign*D*(-t[1]),y:P[i].y+sign*D*t[0],z:P[i].z})}return o}
  var outv=unit(P[cut].x-cx,P[cut].y-cy),tc=T[cut];
  var dR=unit(outv[0]*.85+sgn*tc[0]*.55,outv[1]*.85+sgn*tc[1]*.55),dS=unit(outv[0]*.85-sgn*tc[0]*.55,outv[1]*.85-sgn*tc[1]*.55);
  function path(from,t0,dir,L){var pts=[],x=from.x,y=from.y,s=0;while(s<L){var w=Math.min(1,s/blend),d=unit(t0[0]*(1-w)+dir[0]*w,t0[1]*(1-w)+dir[1]*w);x+=d[0]*3;y+=d[1]*3;s+=3;pts.push({x:x,y:y,z:from.z,d:d})}return pts}
  function offF(pts,sign){return pts.map(function(p){return{x:p.x+sign*D*(-p.d[1]),y:p.y+sign*D*p.d[0],z:p.z}})}
  function offB(pts,sign){return pts.map(function(p){return{x:p.x+sign*D*(p.d[1]),y:p.y-sign*D*(p.d[0]),z:p.z}})}
  var cS={x:P[st].x,y:P[st].y,z:P[st].z},cE={x:P[en].x,y:P[en].y,z:P[en].z};
  var psL=path(cS,[-T[st][0],-T[st][1]],dS,170),psS=path(cS,[-T[st][0],-T[st][1]],dS,64);
  var prL=path(cE,T[en],dR,170),prS=path(cE,T[en],dR,64);
  var A=offB(psL,1).reverse().concat(arc(1),offF(prS,1));
  var B=offF(prL,-1).reverse().concat(arc(-1).reverse(),offB(psS,-1));
  var a1=A[A.length-1],b0=B[0],hid=[];for(var k=1;k<40;k++){var u=k/40;hid.push({x:a1.x+(b0.x-a1.x)*u,y:a1.y+(b0.y-a1.y)*u,z:0,h:true})}
  hid[0].x=a1.x+(b0.x-a1.x)*.002;hid[0].y=a1.y+(b0.y-a1.y)*.002;hid[hid.length-1].x=b0.x-(b0.x-a1.x)*.002;hid[hid.length-1].y=b0.y-(b0.y-a1.y)*.002;
  var R=A.concat(hid,B),pts=K.resample(R,2.2);
  /* indices clés après rééchantillonnage */
  var iAend=0,iBst=0;for(var i=0;i<pts.length;i++){if(pts[i].h){if(!iAend)iAend=i-1;iBst=i+1}}
  var cum=K.arclen(pts),L=cum[cum.length-1];
  var lenB=cum[cum.length-1]-cum[iBst],iBmid=iBst;while(iBmid<pts.length-1&&cum[iBmid]-cum[iBst]<lenB*.55)iBmid++;
  return{points:pts,iAend:iAend,iBst:iBst,marks:{a:cum[iAend]/L,b:cum[iBmid]/L}};
}
function sangle(){
  var res=null;
  for(var o=-12;o<=12&&!res;o++)[1,-1].forEach(function(sgn){[30,40,52,64].forEach(function(gs){[50,70,110].forEach(function(bl){if(res)return;
    var r=build(o*14,gs,sgn,bl);var vis=r.points.filter(function(p){return!p.h});
    var ok=K.crossings(r.points,false).length===12&&vis.every(function(p){return p.x>8&&p.x<792&&p.y>8&&p.y<442});if(ok)res=r})})});
  return res||build(0,40,1,90);
}
root.KnotSangle=sangle;
})(typeof window!=='undefined'?window:globalThis);
