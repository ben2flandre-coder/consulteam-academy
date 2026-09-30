/* Fonctions communes — menu, mémoire locale sûre, cases à cocher, onglets, calculateurs, QCM */
(function(){
'use strict';
var store={get:function(k){try{return localStorage.getItem(k)}catch(e){return null}},set:function(k,v){try{localStorage.setItem(k,v)}catch(e){}},del:function(k){try{localStorage.removeItem(k)}catch(e){}}};
window.HStore=store;
document.addEventListener('DOMContentLoaded',function(){
  var mb=document.querySelector('.menu-btn'),nav=document.querySelector('.top nav');
  if(mb&&nav){mb.addEventListener('click',function(){var o=nav.classList.toggle('open');mb.setAttribute('aria-expanded',o)})}
  /* cases à cocher mémorisées (par page) */
  var pg=location.pathname.split('/').pop()||'index';
  document.querySelectorAll('input[type=checkbox][data-keep]').forEach(function(el,i){
    var k='h-'+pg+'-'+(el.dataset.keep||i);el.checked=store.get(k)==='1';
    el.addEventListener('change',function(){store.set(k,el.checked?'1':'0')});
  });
  /* autres champs mémorisés : data-save="clé" (radio, select, texte) */
  document.querySelectorAll('[data-save]').forEach(function(el){
    var k='h-'+pg+'-s-'+el.dataset.save+(el.type==='radio'?'-'+el.name:''),v=store.get(k);
    if(el.type==='radio'){el.checked=(v===el.value);el.addEventListener('change',function(){if(el.checked)store.set(k,el.value)})}
    else{if(v!==null&&v!==undefined)el.value=v;el.addEventListener('input',function(){store.set(k,el.value)})}
  });
  document.querySelectorAll('[data-reset]').forEach(function(b){b.addEventListener('click',function(){
    var box=document.querySelector(b.dataset.reset);if(!box)return;
    box.querySelectorAll('input[type=checkbox]').forEach(function(c){c.checked=false;c.dispatchEvent(new Event('change'))});box.querySelectorAll('[data-save]').forEach(function(c){if(c.type==='radio')c.checked=false;else c.value=c.tagName==='SELECT'?c.options[0].value:'';c.dispatchEvent(new Event(c.type==='radio'?'change':'input'))});
  })});
  /* onglets */
  document.querySelectorAll('.tabs[data-tabs]').forEach(function(t){
    var btns=t.querySelectorAll('button'),panels=document.querySelectorAll(t.dataset.tabs+' > [role=tabpanel]');
    function sel(i){btns.forEach(function(b,j){b.setAttribute('aria-selected',i===j)});panels.forEach(function(p,j){p.hidden=i!==j})}
    btns.forEach(function(b,i){b.addEventListener('click',function(){sel(i)})});sel(0);
  });
  /* criticité */
  var g=document.getElementById('g');
  if(g){var upd=function(){var c=(+g.value)*(+document.getElementById('p').value)*(+document.getElementById('e').value);
    var t=c<=8?'faible':c<=24?'à réduire':c<=47?'élevée':'arrêt / maîtrise préalable';
    document.getElementById('score').textContent='Criticité : '+c+' / 64 — '+t};
    ['g','p','e'].forEach(function(i){document.getElementById(i).addEventListener('change',upd)});upd()}
  /* tirant d'air : somme des valeurs de la NOTICE saisies par l'utilisateur */
  var ta=document.getElementById('ta-form');
  if(ta){var f=function(){var s=0,ok=true;['ta1','ta2','ta3','ta4'].forEach(function(id){var v=parseFloat(document.getElementById(id).value.replace(',','.'));if(isNaN(v)){ok=false}else s+=v});
    var lib=parseFloat(document.getElementById('ta5').value.replace(',','.')),out=document.getElementById('ta-out');
    if(!ok){out.textContent='Saisir les 4 valeurs de la notice (m).';return}
    var txt='Tirant d’air nécessaire : '+s.toFixed(2).replace('.',',')+' m';
    if(!isNaN(lib)){txt+=lib>=s?' — hauteur libre disponible suffisante ('+lib.toFixed(2).replace('.',',')+' m), sous réserve des obstacles.':' — INSUFFISANT : '+lib.toFixed(2).replace('.',',')+' m disponibles. Ne pas s’accrocher.'}
    out.textContent=txt};ta.addEventListener('input',f);f()}
  /* facteur de chute */
  var ff=document.getElementById('fc-form');
  if(ff){var h=function(){var H=parseFloat(document.getElementById('fc1').value.replace(',','.')),L=parseFloat(document.getElementById('fc2').value.replace(',','.')),o=document.getElementById('fc-out');
    if(isNaN(H)||isNaN(L)||L<=0){o.textContent='Saisir la hauteur de chute et la longueur de liaison (m).';return}
    var F=H/L;o.textContent='Facteur de chute : '+F.toFixed(2).replace('.',',')+(F>2?' — supérieur à 2 : hors du modèle simple, revoir la configuration.':F>=1?' — facteur élevé : ancrage à placer plus haut si possible.':' — facteur faible (ancrage haut).')};ff.addEventListener('input',h);h()}
  /* QCM */
  var qz=document.getElementById('quiz');
  if(qz&&window.QCM){
    QCM.forEach(function(x,i){var f=document.createElement('fieldset');f.className='q card';
      var l=document.createElement('legend');l.textContent=(i+1)+'. '+x.q;f.appendChild(l);
      x.o.forEach(function(c,j){var lb=document.createElement('label');lb.className='f';lb.style.cssText='display:flex;gap:10px;align-items:center;margin:4px 0;font-weight:600;min-height:44px';
        var r=document.createElement('input');r.type='radio';r.name='q'+i;r.value=j;r.style.cssText='width:22px;height:22px;accent-color:#ec168c;flex:0 0 auto';lb.appendChild(r);lb.appendChild(document.createTextNode(' '+String.fromCharCode(65+j)+'. '+c));f.appendChild(lb)});
      var fb=document.createElement('p');fb.className='feedback';fb.setAttribute('aria-live','polite');fb.style.fontWeight='800';f.appendChild(fb);qz.appendChild(f)});
    document.getElementById('grade').addEventListener('click',function(){var s=0,n=0;
      qz.querySelectorAll('.q').forEach(function(f,i){var c=f.querySelector('input:checked'),fb=f.querySelector('.feedback');
        if(!c){fb.textContent='Réponse manquante.';fb.style.color='#9a5700';return}n++;var ok=+c.value===QCM[i].a;if(ok)s++;
        fb.textContent=(ok?'✓ Correct. ':'✗ À reprendre : ')+QCM[i].e;fb.style.color=ok?'#147a51':'#b3261e'});
      var r=document.getElementById('quiz-result');r.textContent='Résultat : '+s+' / '+QCM.length+(n<QCM.length?' ('+(QCM.length-n)+' sans réponse)':'')+'. Le seuil de réussite est fixé par l’organisme avant la session.'});
    document.getElementById('reset-quiz').addEventListener('click',function(){qz.querySelectorAll('input').forEach(function(i){i.checked=false});qz.querySelectorAll('.feedback').forEach(function(x){x.textContent=''});document.getElementById('quiz-result').textContent=''});
  }
});
})();
