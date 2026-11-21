(function(){
'use strict';
var K=window.KnotAnim,G=window.KnotGeo;
function build(kind,tail){
  tail=tail||{};
  var P=K.fit(G[kind](),tail.box||{x:230,y:60,w:340,h:330});
  var want=K.crossings(P,true).length,n=P.length,cx=0,cy=0;P.forEach(function(p){cx+=p.x;cy+=p.y});cx/=n;cy/=n;
  var idx=P.map(function(p,i){return i}).sort(function(a,b){return Math.hypot(P[b].x-cx,P[b].y-cy)-Math.hypot(P[a].x-cx,P[a].y-cy)});
  var best=null,tries=0;
  for(var q=0;q<idx.length&&!best&&tries<3000;q+=6){[.8,1.2,1.8].forEach(function(sp){[60,40].forEach(function(gp){if(best)return;tries++;
    var O0=K.openKnot(P,idx[q],tail.gap||gp,tail.len||170,sp),C=K.resample(O0,7);
    if(K.crossings(C,false).length===want&&Math.hypot(C[0].x-C[C.length-1].x,C[0].y-C[C.length-1].y)>70&&C.every(function(p){return p.x>4&&p.x<796&&p.y>4&&p.y<446})){var F=K.resample(O0,2.2);if(K.crossings(F,false).length===want)best=F}})})}
  if(!best)best=K.resample(K.openKnot(P,idx[0],26,170,.5),2.2);
  return best;
}
var TR=window.KnotTresse?window.KnotTresse():null;
window.KNOTS={
  overhand:{title:'Nœud d’arrêt simple',kind:'overhand',intro:'<strong>Usage :</strong> arrêter le bout d’une corde pour qu’il ne sorte pas d’un descendeur, d’un connecteur ou d’un anneau.',fin:'Le nœud est formé : une boucle dans laquelle le bout est passé.',tail:{box:{x:240,y:130,w:320,h:270},len:110},steps:[]},
  tresse:TR?{title:'Nœud en huit tressé sur un anneau',custom:TR,occluder:ringOcc(TR.ring,57,26),steps:TR?[
{t:'Départ : le brin dormant',d:'La corde part du brin dormant. Suivre la pastille rose : elle montre le bout de la corde qui avance.',p:0.02},
{t:'Préparer : un huit simple, lâche',d:'Prévoir assez de corde et former un huit simple, lâche, à distance du point de connexion (anneau). Le bout se retrouve devant l’anneau.',p:TR.marks.a},
{t:'Connecter : passer le bout dans l’anneau',d:'Passer le brin actif dans l’anneau ou le point de connexion prévu, puis revenir vers le huit.',p:TR.marks.b},
{t:'Suivre le chemin (1/3)',d:'Repasser le brin actif dans le huit, brin contre brin, en suivant exactement le premier passage. Aucun croisement, aucune vrille.',p:TR.marks.b+(TR.marks.c-TR.marks.b)/3},
{t:'Suivre le chemin (2/3)',d:'Continuer à longer le premier brin, côte à côte, en gardant les deux brins parallèles.',p:TR.marks.b+2*(TR.marks.c-TR.marks.b)/3},
{t:'Suivre le chemin (3/3)',d:'Terminer le parcours : le bout ressort à côté du brin dormant. Dans le nœud, les brins restent parallèles, sans croisement.',p:TR.marks.c},
{t:'Serrer, aligner, contrôler',d:'Reprendre chaque brin pour serrer le nœud, aligner les paires parallèles, conserver un brin libre suffisant.',p:1,w:'Contrôle croisé par le binôme avant toute mise en charge.'}
]:[],intro:'<strong>Usage :</strong> former une boucle solide sur un anneau ou un point de connexion prévu, en suivant en double le chemin d’un huit.'}:null,
  huit:{title:'Nœud en huit simple',kind:'huit',intro:'<strong>Usage :</strong> nœud d’arrêt volumineux, facile à défaire après charge ; première étape du huit tressé.',fin:'Le huit est formé : deux boucles croisées, le bout ressort du côté du brin dormant.',tail:{},steps:[]}
};
window.buildKnotPoints=build;
function ph(id,list){return list.map(function(x,i){return{src:'assets/img/noeuds/'+id+'-'+x[0]+'.jpg',cap:x[1]}})}
window.KNOT_PHOTOS={
  overhand:ph('arret-simple',[['final','Nœud d’arrêt simple, terminé'],['1','Former la boucle'],['2','Passer le bout dans la boucle'],['3','Serrer']]),
  huit:ph('huit-simple',[['final','Nœud en huit simple, terminé'],['1','Former la boucle'],['2','Contourner le brin dormant'],['3','Passer dans la boucle'],['4','Serrer']]),
  tresse:ph('huit-tresse',[['final','Huit tressé sur anneau, terminé'],['1','Huit simple, lâche'],['2','Passer le bout dans l’anneau'],['3','Suivre le chemin'],['4','Serrer, aligner']])
};
/* anneau métallique en relief (occulteur) */
function ringOcc(C,r,w){return function(g,id,el){
  var gr=el('linearGradient',{id:id+'rg',gradientUnits:'userSpaceOnUse',x1:C.x-r,y1:C.y-r,x2:C.x+r,y2:C.y+r},g);
  [['0','#f4f6f8'],['.35','#a9b3bb'],['.7','#6c7782'],['1','#3c444c']].forEach(function(s){el('stop',{offset:s[0],'stop-color':s[1]},gr)});
  el('circle',{cx:C.x+6,cy:C.y+9,r:r,fill:'none',stroke:'#0b1d2c','stroke-width':w+4,opacity:.28,filter:'url(#'+id+'sh)'},g);
  el('circle',{cx:C.x,cy:C.y,r:r,fill:'none',stroke:'#2a3138','stroke-width':w+2.4},g);
  el('circle',{cx:C.x,cy:C.y,r:r,fill:'none',stroke:'url(#'+id+'rg)','stroke-width':w},g);
  el('circle',{cx:C.x-1.5,cy:C.y-2,r:r,fill:'none',stroke:'#ffffff','stroke-width':w*.28,opacity:.6,filter:'url(#'+id+'b3)'},g);
  el('circle',{cx:C.x+2,cy:C.y+3,r:r,fill:'none',stroke:'#2a3138','stroke-width':w*.2,opacity:.35,filter:'url(#'+id+'b3)'},g)}}
window.ringOcc=ringOcc;
})();
