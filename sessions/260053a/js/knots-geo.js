/* Trajets de corde des nœuds, dessinés sous leur forme de manuel (nœud « ouvert », à plat).
   Chaque trajet est une liste de points de passage (x, y, z) : z > 0 = la corde passe DESSUS, z < 0 = DESSOUS.
   Le trajet part du brin dormant et finit au bout libre. Contrôle par calcul (test automatique) :
   nombre de croisements, alternance dessus/dessous, déterminant de Fox (arrêt simple = 3, huit = 5). */
(function(root){
'use strict';
/* courbe de Catmull-Rom centripète passant par les points de passage ; z interpolé linéairement */
function spline(W,step){
  var P=[W[0]].concat(W,[W[W.length-1]]),out=[];
  for(var i=1;i<P.length-2;i++){
    var p0=P[i-1],p1=P[i],p2=P[i+1],p3=P[i+2];
    function tj(a,b){return Math.pow(Math.hypot(b.x-a.x,b.y-a.y)||1e-6,.5)}
    var t0=0,t1=t0+tj(p0,p1),t2=t1+tj(p1,p2),t3=t2+tj(p2,p3);
    var seg=Math.hypot(p2.x-p1.x,p2.y-p1.y),n=Math.max(2,Math.ceil(seg/step));
    for(var k=0;k<n;k++){
      var t=t1+(t2-t1)*k/n;
      function L(a,b,ta,tb){var u=(t-ta)/((tb-ta)||1e-6);return{x:a.x+(b.x-a.x)*u,y:a.y+(b.y-a.y)*u}}
      var A1=L(p0,p1,t0,t1),A2=L(p1,p2,t1,t2),A3=L(p2,p3,t2,t3);
      var B1=L(A1,A2,t0,t2),B2=L(A2,A3,t1,t3),C=L(B1,B2,t1,t2);
      out.push({x:C.x,y:C.y,z:p1.z+(p2.z-p1.z)*k/n});
    }
  }
  var e=W[W.length-1];out.push({x:e.x,y:e.y,z:e.z});return out;
}
function w(x,y,z){return{x:x,y:y,z:z||0}}
/* Nœud d'arrêt simple : boucle (le bout passe DESSUS le brin dormant), puis le bout passe dans la boucle. */
var OVERHAND=[w(0,340),w(0,250),w(0,150,-1),w(0,58,1),w(-8,14),w(-45,-18),w(-97,-10),w(-124,36),w(-108,94,-1),w(-64,138),w(0,150,1),
  w(58,160),w(98,124),w(74,70),w(0,58,-1),w(-56,74),w(-108,94,1),w(-152,110),w(-240,120)];
/* Nœud en huit simple : 1 boucle (le bout passe DESSUS le brin dormant) ; 2 le bout passe DERRIÈRE le brin dormant ;
   3 il revient par-devant et entre dans la boucle (DESSUS le bord de la boucle), ressort DERRIÈRE le brin dormant. */
var HUIT=[w(0,360),w(0,232,1),w(0,130,-1),w(0,62,1),w(-8,16),w(-45,-14),w(-95,-6),w(-120,38),w(-102,96,-1),w(-58,124),w(0,130,1),
  w(50,146),w(84,186),w(62,224),w(0,232,-1),w(-56,236),w(-98,212),w(-110,166),w(-102,96,1),w(-64,70),w(0,62,-1),w(60,56),w(150,52),w(240,52)];
var G={
  spline:spline,
  overhandOpen:function(step){return spline(OVERHAND,step||2)},
  huitOpen:function(step){return spline(HUIT,step||2)},
  waypoints:{overhand:OVERHAND,huit:HUIT}
};
root.KnotGeo=G;if(typeof module!=='undefined')module.exports=G;
})(typeof window!=='undefined'?window:globalThis);
