/* Huit tressé (« suivre le chemin ») sur un anneau : câble (2 brins parallèles) d'un huit validé, ouvert en un point.
   Un brin va du bout S, fait le tour du huit, passe dans l'anneau (demi-tour), puis suit le même chemin en sens inverse jusqu'au bout T. */
(function(root){
'use strict';
var K=root.KnotAnim,G=root.KnotGeo;
function unit(x,y){var l=Math.hypot(x,y)||1;return[x/l,y/l]}
function build(cutIdx,gs,sgn,blend,Lr){
  var D=11.8,P=K.fit(G.huit(1700),{x:50,y:135,w:380,h:240}),n=P.length;
  var T=P.map(function(p,i){var a=P[(i-1+n)%n],b=P[(i+1)%n];return unit(b.x-a.x,b.y-a.y)});
  var cut=cutIdx(P);
  var st=(cut+gs)%n,en=(cut-gs+n)%n,len=(en-st+n)%n;
  function arcPts(sign,rev){var out=[];for(var k=0;k<=len;k++){var i=(st+k)%n,t=T[i];out.push({x:P[i].x+sign*D*(-t[1]),y:P[i].y+sign*D*t[0],z:P[i].z})}return rev?out.reverse():out}
  var cx=0,cy=0;P.forEach(function(p){cx+=p.x;cy+=p.y});cx/=n;cy/=n;
  var outv=unit(P[cut].x-cx,P[cut].y-cy),tc=T[cut];
  var dR=unit(outv[0]*.85+sgn*tc[0]*.55,outv[1]*.85+sgn*tc[1]*.55),dS=unit(outv[0]*.85-sgn*tc[0]*.55,outv[1]*.85-sgn*tc[1]*.55);
  function path(from,t0,dir,L,step){var pts=[],x=from.x,y=from.y,s=0;
    while(s<L){var w=Math.min(1,s/blend),d=unit(t0[0]*(1-w)+dir[0]*w,t0[1]*(1-w)+dir[1]*w);x+=d[0]*step;y+=d[1]*step;s+=step;pts.push({x:x,y:y,z:from.z,d:d})}return pts}
  var cE={x:P[en].x,y:P[en].y,z:P[en].z},pr=path(cE,T[en],dR,Lr+34,3),ir=Math.round(Lr/3),Cring={x:pr[ir].x,y:pr[ir].y},dl=pr[ir].d;
  function off(pts,sign){return pts.map(function(p){return{x:p.x+sign*D*(-p.d[1]),y:p.y+sign*D*p.d[0],z:p.z}})}
  var outP=off(pr,1),backP=off(pr,-1).reverse();
  var last=pr[pr.length-1],th=Math.atan2(last.d[1],last.d[0]),turn=[];
  for(var k=1;k<20;k++){var a=th+Math.PI/2-Math.PI*k/20;turn.push({x:last.x+D*Math.cos(a),y:last.y+D*Math.sin(a),z:last.z})}
  var cS={x:P[st].x,y:P[st].y,z:P[st].z},ps=path(cS,[-T[st][0],-T[st][1]],dS,150,3);
  function offTail(pts,sign){return pts.map(function(p){return{x:p.x+sign*D*(p.d[1]),y:p.y-sign*D*(p.d[0]),z:p.z}})}
  var tailS=offTail(ps,1).reverse(),tailT=offTail(ps,-1);
  var a1=arcPts(1,false),a2=arcPts(-1,true);
  var R=tailS.concat(a1,outP,turn,backP,a2,tailT);
  var iA=tailS.length+a1.length,iB=iA+outP.length+turn.length+backP.length,iC=R.length-tailT.length;
  var cum=[0];R.forEach(function(p,i){if(i)cum.push(cum[i-1]+Math.hypot(p.x-R[i-1].x,p.y-R[i-1].y))});
  R.forEach(function(p,i){var u=(p.x-Cring.x)*dl[0]+(p.y-Cring.y)*dl[1];p.b=(i>=iA&&i<iB&&u>-18)});
  var Ltot=cum[cum.length-1],pts=K.resample(R,2.2);
  return{points:pts,ring:Cring,L:Ltot,marks:{a:cum[iA]/Ltot,b:cum[iB]/Ltot,c:cum[iC]/Ltot},dl:dl};
}
function tresse(){
  var tries=[],res=null;
  [-1,1].forEach(function(sgn){[26,34,44].forEach(function(gs){[70,110].forEach(function(bl){[0,1,2,3,4,5,6].forEach(function(o){
    tries.push([sgn,gs,bl,o])})})})});
  for(var q=0;q<tries.length&&!res;q++){var t=tries[q];
    var r=build(function(P){var c=0;P.forEach(function(p,i){if(p.x>P[c].x)c=i});return (c+(t[3]-3)*12+P.length)%P.length},t[1],t[0],t[2],118);
    var xs=r.points.map(function(p){return p.x}),ys=r.points.map(function(p){return p.y});
    var ok=K.crossings(r.points,false).length===16&&Math.max.apply(null,xs)<780&&Math.min.apply(null,xs)>6&&Math.max.apply(null,ys)<444&&Math.min.apply(null,ys)>6&&r.ring.y-64>4&&r.ring.x+64<796&&r.ring.y+64<446;
    if(ok)res=r}
  if(!res)res=build(function(P){var c=0;P.forEach(function(p,i){if(p.x>P[c].x)c=i});return c},26,-1,70,150);
  return res;
}
root.KnotTresse=tresse;
})(typeof window!=='undefined'?window:globalThis);
