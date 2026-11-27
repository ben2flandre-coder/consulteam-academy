(function(){
'use strict';
var K=window.KnotAnim,G=window.KnotGeo;
/* trajets ouverts dessinés (knots-geo.js), recadrés dans la zone de dessin */
function build(kind,tail){
  tail=tail||{};var P=kind==='huit'?G.huitOpen(1.5):G.overhandOpen(1.5);
  return K.resample(K.fit(P,tail.box||{x:230,y:28,w:340,h:400}),2.2);
}
var TR=window.KnotTresse?window.KnotTresse():null,SG=window.KnotSangle?window.KnotSangle():null;
window.KNOTS={
  overhand:{title:'Nœud d’arrêt simple',kind:'overhand',fiche:[{t:'Départ : le brin dormant',d:'La corde part du brin dormant ; la pastille rose suit le bout libre.',p0:0.03},{t:'Boucle',d:'Former une boucle avec le bout libre, le bout passant par-dessus le brin dormant, en laissant une queue suffisante.',ev:0},{t:'Passer',d:'Passer le bout dans la boucle.',ev:2},{t:'Contrôler le trajet, puis serrer sur corde réelle',d:'Tirer sur le bout et sur le brin dormant pour former un nœud compact. Bout libre d’au moins une dizaine de centimètres (repère courant).',end:1,w:'Il arrête le bout de la corde : il n’amarre pas.'}],intro:'<strong>Usage :</strong> arrêter le bout d’une corde pour qu’il ne sorte pas d’un descendeur, d’un connecteur ou d’un anneau.',fin:'Le nœud est formé : une boucle dans laquelle le bout est passé.',tail:{box:{x:250,y:40,w:330,h:380}},steps:[]},
  tresse:TR?{title:'Nœud en huit tressé sur un anneau',custom:TR,occluder:ringOcc(TR.ring,57,26),steps:TR?[
{t:'Départ : le brin dormant',d:'La corde part du brin dormant. Suivre la pastille rose : elle montre le bout de la corde qui avance.',p:0.06},
{t:'Préparer : un huit simple, lâche',d:'Prévoir assez de corde et former un huit simple, lâche, à distance du point de connexion (anneau). Le bout se retrouve devant l’anneau.',p:TR.marks.a},
{t:'Connecter : passer le bout dans l’anneau',d:'Passer le brin actif dans l’anneau ou le point de connexion prévu, puis revenir vers le huit.',p:TR.marks.b},
{t:'Suivre le chemin (1/3)',d:'Repasser le brin actif dans le huit, brin contre brin, en suivant exactement le premier passage. Aucun croisement, aucune vrille.',p:TR.marks.b+(TR.marks.c-TR.marks.b)/3},
{t:'Suivre le chemin (2/3)',d:'Continuer à longer le premier brin, côte à côte, en gardant les deux brins parallèles.',p:TR.marks.b+2*(TR.marks.c-TR.marks.b)/3},
{t:'Suivre le chemin (3/3)',d:'Terminer le parcours : le bout ressort à côté du brin dormant. Dans le nœud, les brins restent parallèles, sans croisement.',p:TR.marks.c},
{t:'Contrôler le trajet, puis serrer sur corde réelle',d:'Reprendre chaque brin pour serrer le nœud, aligner les paires parallèles, conserver un brin libre suffisant.',p:1,w:'Contrôle croisé par le binôme avant toute mise en charge.'}
]:[],intro:'<strong>Usage :</strong> former une boucle solide sur un anneau ou un point de connexion prévu, en suivant en double le chemin d’un huit.'}:null,
  sangle:SG?{title:'Nœud de sangle',custom:SG,flat:true,ropeWidth:28,palette:{dark:'#0b1b3f',mid:'#2153c9',light:'#6c9cf2',hi:'#d4e3ff',acc:'#ec168c'},caps:[SG.iAend],fadeAt:[0,SG.iBst],
    intro:'<strong>Usage :</strong> assembler deux bouts de sangle plate, ou fermer une sangle en boucle, pour un usage non critique, hors dispositif antichute.',
    steps:[{t:'Départ',d:'La première extrémité de la sangle part d’ici ; la pastille rose suit le bout.',p:.06},
      {t:'Nœud simple',d:'Faire un nœud simple lâche à une extrémité de la sangle, bien à plat.',p:SG.marks.a},
      {t:'Suivre',d:'Avec l’autre extrémité, suivre le même cheminement dans le sens inverse, en gardant la sangle à plat.',p:SG.marks.b},
      {t:'Contrôler le trajet, puis serrer sur corde réelle',d:'Serrer progressivement en tirant sur les quatre brins, sans vrille. Sangle à plat, queues d’au moins une dizaine de centimètres.',p:1,w:'Une sangle assemblée par nœud ne sert pas d’ancrage antichute sans validation du fabricant.'}]}:null,
  huit:{title:'Nœud en huit simple',kind:'huit',fiche:[{t:'Départ : le brin dormant',d:'La corde part du brin dormant ; la pastille rose suit le bout libre.',p0:0.03},{t:'Boucle',d:'Former une boucle avec le bout libre, le bout passant par-dessus le brin dormant.',ev:0},{t:'Contourner',d:'Passer le bout derrière le brin dormant.',ev:1},{t:'Revenir',d:'Ramener le bout par-devant et le glisser dans la boucle, de l’avant vers l’arrière.',ev:3},{t:'Trajet complet — serrage sur corde réelle',d:'Tirer les deux brins pour obtenir un 8 régulier, sans croisement parasite, avec un bout libre suffisant.',end:1}],intro:'<strong>Usage :</strong> nœud d’arrêt volumineux, plus facile à défaire que le nœud d’arrêt simple ; première étape du huit tressé.',fin:'Le huit est formé : deux boucles en forme de 8 autour du brin dormant.',tail:{},steps:[]}
};
window.buildKnotPoints=build;
function ph(id,list){return list.map(function(x,i){return{src:'assets/img/noeuds/'+id+'-'+x[0]+'.jpg',cap:x[1]}})}
window.KNOT_PHOTOS={
  overhand:ph('arret-simple',[['final','Trajet complet, nœud ouvert : nœud d’arrêt simple'],['1','Étape 1 · Boucle'],['2','Étape 2 · Passer'],['3','Étape 3 · Serrer']]),
  huit:ph('huit-simple',[['final','Trajet complet, nœud ouvert : nœud en huit simple'],['1','Étape 1 · Boucle'],['2','Étape 2 · Contourner'],['3','Étape 3 · Revenir'],['4','Étape 4 · Serrer']]),
  sangle:ph('sangle',[['final','Trajet complet, nœud ouvert : nœud de sangle'],['1','Étape 1 · Nœud simple'],['2','Étape 2 · Suivre'],['3','Étape 3 · Serrer']]),
  tresse:ph('huit-tresse',[['final','Trajet complet, nœud ouvert : huit tressé sur anneau'],['1','Étape 1 · Préparer'],['2','Étape 2 · Connecter'],['3','Étape 3 · Suivre le chemin'],['4','Étape 4 · Serrer et aligner']])
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

