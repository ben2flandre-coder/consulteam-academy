(function(){
'use strict';
var K=window.KnotAnim,G=window.KnotGeo;
function build(kind,tail){
  tail=tail||{};
  var P=K.fit(G[kind](),tail.box||{x:230,y:60,w:340,h:330});
  var want=K.crossings(P,true).length,n=P.length,cx=0,cy=0;P.forEach(function(p){cx+=p.x;cy+=p.y});cx/=n;cy/=n;
  var idx=P.map(function(p,i){return i}).sort(function(a,b){return Math.hypot(P[b].x-cx,P[b].y-cy)-Math.hypot(P[a].x-cx,P[a].y-cy)});
  var best=null;
  for(var q=0;q<idx.length&&!best;q+=3){[.15,.3,.5,.8,1.1,1.5].forEach(function(sp){if(best)return;
    var O=K.resample(K.openKnot(P,idx[q],tail.gap||26,tail.len||170,sp),2.2);
    if(K.crossings(O,false).length===want&&O.every(function(p){return p.x>4&&p.x<796&&p.y>4&&p.y<446}))best=O})}
  if(!best)best=K.resample(K.openKnot(P,idx[0],26,170,.5),2.2);
  return best;
}
window.KNOTS={
  overhand:{title:'Nœud d’arrêt simple',kind:'overhand',intro:'<strong>Usage :</strong> arrêter le bout d’une corde pour qu’il ne sorte pas d’un descendeur, d’un connecteur ou d’un anneau.',fin:'Le nœud est formé : une boucle dans laquelle le bout est passé.',tail:{box:{x:240,y:130,w:320,h:270},len:110},steps:[]},
  huit:{title:'Nœud en huit simple',kind:'huit',intro:'<strong>Usage :</strong> nœud d’arrêt volumineux, facile à défaire après charge ; première étape du huit tressé.',fin:'Le huit est formé : deux boucles croisées, le bout ressort du côté du brin dormant.',tail:{},steps:[]}
};
window.buildKnotPoints=build;
})();
