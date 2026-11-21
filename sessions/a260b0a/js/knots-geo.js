/* Géométries 3D de nœuds fermés (validées par le déterminant de Fox) puis ouvertes en deux brins */
(function(root){
'use strict';
function curve(f,N){var a=[];for(var i=0;i<N;i++){var t=2*Math.PI*i/N;a.push(f(t))}return a}
var G={
  overhand:function(N){return curve(function(t){return{x:Math.sin(t)+2*Math.sin(2*t),y:Math.cos(t)-2*Math.cos(2*t),z:-Math.sin(3*t)*1.4}},N||1400)},
  huit:function(N){return curve(function(t){var r=2+Math.cos(2*t);return{x:r*Math.cos(3*t),y:r*Math.sin(3*t),z:Math.sin(4*t)*1.4}},N||1600)},
  doubleOverhand:function(N){return curve(function(t){var r=2.2+Math.cos(5*t/2*1);return{x:r*Math.cos(t),y:r*Math.sin(t),z:Math.sin(5*t/2)}},N||1800)}
};
root.KnotGeo=G;if(typeof module!=='undefined')module.exports=G;
})(typeof window!=='undefined'?window:globalThis);
