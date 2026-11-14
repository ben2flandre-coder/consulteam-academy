'use strict';
(function(){
var A=window.A,CFG={destinataire:'',endpoint:''};
function E(s){return String(s==null?'':s).replace(/[&<>"']/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})}
window.E=E;
try{if(localStorage.getItem('he.nuit')==='1')document.body.classList.add('nuit')}catch(e){}
var pages=[['index.html','Accueil'],['parcours.html','Parcours'],['evaluation.html','Évaluation'],['animation.html','Animation'],['mediatheque.html','Médiathèque'],['registre.html','Sources'],['formateur.html','Formateur']];
var here=location.pathname.split('/').pop()||'index.html';
var h='<a class="skip" href="#main">Aller au contenu</a><header class="top"><div class="bar"><a class="brand" href="index.html"><img src="images/logos/logo-consulteam-groupe.png" alt="Consul Team" width="150" height="31" style="background:#fff;border-radius:6px;padding:4px 8px;height:34px;width:auto"><span>Habilitation électrique</span></a><nav aria-label="Navigation">';
pages.forEach(function(p){h+='<a href="'+p[0]+'"'+(here===p[0]?' aria-current="page"':'')+'>'+p[1]+'</a>'});
h+='<button type="button" id="nuit" aria-pressed="false">Mode nuit</button></nav></div></header>';
document.body.insertAdjacentHTML('afterbegin',h);
var b=document.getElementById('nuit');
function sync(){b.setAttribute('aria-pressed',document.body.classList.contains('nuit'))}sync();
b.onclick=function(){document.body.classList.toggle('nuit');try{localStorage.setItem('he.nuit',document.body.classList.contains('nuit')?'1':'0')}catch(e){}sync()};
window.module=function(id){return A.modules.filter(function(m){return m.id==id})[0]};
window.statTag=function(s){return '<span class="tag '+(s==='repris'?'rep':s==='à compléter'?'cpl':s==='nouveau'?'cpl':'red')+'">'+(s==='repris'?'Contenu repris':s==='à compléter'?'À compléter':s==='nouveau'?'Nouveau, à valider':'En préparation')+'</span>'};
window.shuffle=function(a){a=a.slice();for(var i=a.length-1;i>0;i--){var j=Math.floor(Math.random()*(i+1));var t=a[i];a[i]=a[j];a[j]=t}return a};
if('serviceWorker' in navigator&&location.protocol.indexOf('http')===0){navigator.serviceWorker.register('sw.js').catch(function(){})}
fetch('assets/config.json').then(function(r){return r.json()}).then(function(c){CFG=c;window.CFG=c}).catch(function(){});
window.CFG=CFG;
})();
