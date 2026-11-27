/* Huit tressé (« suivre le chemin ») sur un anneau, construit à partir du trajet du huit simple (knots-geo.js).
   La corde part du brin dormant, fait le huit (premier passage), passe dans l'anneau (demi-tour),
   puis suit le même chemin en sens inverse, brin contre brin, jusqu'au bout libre qui ressort à côté du brin dormant. */
(function(root){
'use strict';
var K=root.KnotAnim,G=root.KnotGeo;
function unit(x,y){var l=Math.hypot(x,y)||1;return[x/l,y/l]}
function build(opt){
  opt=opt||{};
  var D=opt.D||11.5,box=opt.box||{x:110,y:56,w:300,h:322},R0=opt.ringR||57;
  /* trajet du huit : brin dormant raccourci (bas), bout coupé après la sortie (droite) */
  var O=G.huitOpen(1).filter(function(p,i,a){return true});
  var i0=0;while(O[i0].y>300)i0++;var i1=O.length-1;while(O[i1].x>95)i1--;
  O=O.slice(i0,i1+1);
  O=K.fit(O,box);O=K.resample(O,2);
  var n=O.length,T=O.map(function(p,i){var a=O[Math.max(0,i-1)],b=O[Math.min(n-1,i+1)];return unit(b.x-a.x,b.y-a.y)});
  function off(i,s){return{x:O[i].x+s*D*(-T[i][1]),y:O[i].y+s*D*T[i][0],z:O[i].z}}
  var A=[],B=[];for(var i=0;i<n;i++){A.push(off(i,1));B.push(off(i,-1))}
  /* prolongement vers l'anneau, dans le sens de sortie du bout */
  var E=O[n-1],te=T[n-1],dRing=opt.dRing||(R0+44),Lx=dRing+R0+22,ext=[];
  for(var s=2;s<=Lx;s+=2)ext.push({x:E.x+te[0]*s,y:E.y+te[1]*s,z:0});
  var ring={x:E.x+te[0]*dRing,y:E.y+te[1]*dRing};
  function offE(p,sg){return{x:p.x+sg*D*(-te[1]),y:p.y+sg*D*te[0],z:0}}
  var outP=ext.map(function(p){return offE(p,1)}),backP=ext.map(function(p){return offE(p,-1)}).reverse();
  var last=ext[ext.length-1],th=Math.atan2(te[1],te[0]),turn=[];
  for(var k=1;k<24;k++){var a=th+Math.PI/2-Math.PI*k/24;turn.push({x:last.x+D*Math.cos(a),y:last.y+D*Math.sin(a),z:0})}
  /* brins de sortie en bas : brin dormant (long) et bout libre (court) */
  var S=O[0],ts=T[0],tailA=[],tailB=[];
  for(var s2=2;s2<=(opt.lenA||110);s2+=2)tailA.push({x:S.x-ts[0]*s2+D*(-ts[1]),y:S.y-ts[1]*s2+D*ts[0],z:0});
  for(var s3=2;s3<=(opt.lenB||48);s3+=2)tailB.push({x:S.x-ts[0]*s3-D*(-ts[1]),y:S.y-ts[1]*s3-D*ts[0],z:0});
  tailA.reverse();
  var Rt=tailA.concat(A,outP,turn,backP,B.slice().reverse(),tailB);
  var iA=tailA.length+A.length,iB=iA+outP.length+turn.length+backP.length,iC=Rt.length-tailB.length;
  /* parties qui passent derrière l'anneau (dans le trou puis derrière le bord opposé) */
  Rt.forEach(function(p,j){var u=(p.x-ring.x)*te[0]+(p.y-ring.y)*te[1];p.b=(j>=iA&&j<iB&&u>-18)});
  var cum=K.arclen(Rt),L=cum[cum.length-1],pts=K.resample(Rt,2.2);
  /* reporter le marquage « derrière » après rééchantillonnage */
  pts.forEach(function(p){var u=(p.x-ring.x)*te[0]+(p.y-ring.y)*te[1],dn=Math.abs((p.x-ring.x)*(-te[1])+(p.y-ring.y)*te[0]);p.b=!!(p.b&&u>-18&&dn<D*2.2)});
  return{points:pts,ring:ring,L:L,marks:{a:cum[iA]/L,b:cum[iB]/L,c:cum[iC]/L},dl:te};
}
function tresse(){return build({})}
root.KnotTresse=tresse;root.KnotTresseBuild=build;
})(typeof window!=='undefined'?window:globalThis);
