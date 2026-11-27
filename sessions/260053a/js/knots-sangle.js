/* Nœud de sangle (nœud d'eau), construit à partir du trajet du nœud d'arrêt simple (knots-geo.js) :
   la première extrémité fait un nœud simple lâche ; la seconde extrémité suit le même chemin en sens inverse, à plat. */
(function(root){
'use strict';
var K=root.KnotAnim,G=root.KnotGeo;
function unit(x,y){var l=Math.hypot(x,y)||1;return[x/l,y/l]}
function build(opt){
  opt=opt||{};
  var D=opt.D||15.5,box=opt.box||{x:250,y:70,w:330,h:250};
  var O=G.overhandOpen(1);var i0=0;while(O[i0].y>270)i0++;var i1=O.length-1;while(O[i1].x<-165)i1--;
  O=K.resample(K.fit(O.slice(i0,i1+1),box),2);
  var n=O.length,T=O.map(function(p,i){var a=O[Math.max(0,i-1)],b=O[Math.min(n-1,i+1)];return unit(b.x-a.x,b.y-a.y)});
  function off(i,s){return{x:O[i].x+s*D*(-T[i][1]),y:O[i].y+s*D*T[i][0],z:O[i].z}}
  function tail(P,t,sg,len,dir){var r=[];for(var s=2;s<=len;s+=2)r.push({x:P.x+dir*t[0]*s+sg*D*(-t[1]),y:P.y+dir*t[1]*s+sg*D*t[0],z:0});return r}
  var S=O[0],E=O[n-1],ts=T[0],te=T[n-1];
  var Aarc=[],Barc=[];for(var i=0;i<n;i++){Aarc.push(off(i,1));Barc.push(off(i,-1))}
  /* extrémité 1 : longue côté brin dormant, courte à la sortie */
  var A=tail(S,ts,1,opt.lenLong||150,-1).reverse().concat(Aarc,tail(E,te,1,opt.lenShort||62,1));
  /* extrémité 2 : longue côté sortie, suit en sens inverse, courte côté brin dormant */
  var B=tail(E,te,-1,opt.lenLong||150,1).reverse().concat(Barc.slice().reverse(),tail(S,ts,-1,opt.lenShort||62,-1));
  var a1=A[A.length-1],b0=B[0],hid=[];for(var k=1;k<40;k++){var u=k/40;hid.push({x:a1.x+(b0.x-a1.x)*u,y:a1.y+(b0.y-a1.y)*u,z:0,h:true})}
  var R=A.concat(hid,B),pts=K.resample(R,2.2);
  var iAend=0,iBst=0;for(var j=0;j<pts.length;j++){if(pts[j].h){if(!iAend)iAend=j-1;iBst=j+1}}
  var cum=K.arclen(pts),L=cum[cum.length-1];
  var lenB=L-cum[iBst],iBmid=iBst;while(iBmid<pts.length-1&&cum[iBmid]-cum[iBst]<lenB*.62)iBmid++;
  return{points:pts,iAend:iAend,iBst:iBst,marks:{a:cum[iAend]/L,b:cum[iBmid]/L}};
}
function sangle(){return build({})}
root.KnotSangle=sangle;root.KnotSangleBuild=build;
})(typeof window!=='undefined'?window:globalThis);
