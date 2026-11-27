/* Outils pédagogiques : aucune fonction ne délivre une autorisation de travail. */
(function(root){
'use strict';
function number(value){
  var s=String(value==null?'':value).trim();
  if(!/^(?:\d+(?:[.,]\d+)?|[.,]\d+)$/.test(s))return null;
  var n=Number(s.replace(',','.'));return Number.isFinite(n)?n:null;
}
function clearance(required,available,reference){
  var r=number(required),a=number(available);
  if(r===null||r<=0||a===null)return{state:'invalid'};
  if(reference!=='feet'&&reference!=='anchor'&&reference!=='attachment')return{state:'reference'};
  return{state:a<r?'insufficient':'geometry',required:r,available:a,delta:a-r};
}
function factor(height,length){
  var h=number(height),l=number(length);
  if(h===null||l===null||l<=0)return{state:'invalid'};
  var f=h/l;return{state:f>2?'outside':'model',factor:f};
}
var api={number:number,clearance:clearance,factor:factor};
root.HeightTools=api;if(typeof module!=='undefined')module.exports=api;
})(typeof window!=='undefined'?window:globalThis);
