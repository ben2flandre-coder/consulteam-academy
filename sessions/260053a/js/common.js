/* Fonctions communes — menu, mémoire locale sûre, cases à cocher, onglets, calculateurs, QCM */
(function(){
'use strict';
var prefix='h-260053a-';
var store={get:function(k){try{return localStorage.getItem(prefix+k)}catch(e){return null}},set:function(k,v){try{localStorage.setItem(prefix+k,v)}catch(e){}},del:function(k){try{localStorage.removeItem(prefix+k)}catch(e){}}};
window.HStore=store;
document.addEventListener('DOMContentLoaded',function(){
  if(document.documentElement.classList.contains('esp-p'))document.querySelectorAll('a[href="index.html"]').forEach(function(a){a.href='apprenants.html'});
  var mb=document.querySelector('.menu-btn'),nav=document.querySelector('.top nav');
  if(mb&&nav){mb.addEventListener('click',function(){var o=nav.classList.toggle('open');mb.setAttribute('aria-expanded',String(o))});nav.addEventListener('click',function(e){if(e.target.closest('a')){nav.classList.remove('open');mb.setAttribute('aria-expanded','false')}});document.addEventListener('keydown',function(e){if(e.key==='Escape'&&nav.classList.contains('open')){nav.classList.remove('open');mb.setAttribute('aria-expanded','false');mb.focus()}})}
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
    box.querySelectorAll('input[type=checkbox]').forEach(function(c){c.checked=false;c.dispatchEvent(new Event('change'))});box.querySelectorAll('[data-save]').forEach(function(c){store.del('h-'+pg+'-s-'+c.dataset.save+(c.type==='radio'?'-'+c.name:''));if(c.type==='radio')c.checked=false;else c.value=c.tagName==='SELECT'?c.options[0].value:''});
  })});
  /* Onglets : clavier, libellés et liens directs. */
  document.querySelectorAll('.tabs[data-tabs]').forEach(function(t,ti){
    var btns=t.querySelectorAll('button'),panels=document.querySelectorAll(t.dataset.tabs+' > [role=tabpanel]');
    t.setAttribute('role','tablist');
    function sel(i){btns.forEach(function(b,j){b.setAttribute('aria-selected',String(i===j));b.tabIndex=i===j?0:-1});panels.forEach(function(p,j){p.hidden=i!==j})}
    btns.forEach(function(b,i){var p=panels[i];if(!p)return;b.id=b.id||'tab-'+ti+'-'+i;p.id=p.id||'panel-'+ti+'-'+i;
      b.setAttribute('role','tab');b.setAttribute('aria-controls',p.id);p.setAttribute('aria-labelledby',b.id);
      b.addEventListener('click',function(){sel(i)});
      b.addEventListener('keydown',function(e){var n=i;if(e.key==='ArrowRight')n=(i+1)%btns.length;else if(e.key==='ArrowLeft')n=(i-1+btns.length)%btns.length;else if(e.key==='Home')n=0;else if(e.key==='End')n=btns.length-1;else return;e.preventDefault();sel(n);btns[n].focus()});
    });
    function hashTab(){var id;try{id=decodeURIComponent(location.hash.slice(1))}catch(e){return}var target=document.getElementById(id);if(!target)return;panels.forEach(function(p,i){if(p===target||p.contains(target))sel(i)})}
    sel(0);hashTab();window.addEventListener('hashchange',hashTab);
  });
  /* Un score bas ne peut autoriser une exposition mortelle non maîtrisée. */
  var g=document.getElementById('g');
  if(g){var upd=function(){var c=(+g.value)*(+document.getElementById('p').value)*(+document.getElementById('e').value);
    document.getElementById('score').textContent='Indice de priorité : '+c+' / 64. '+(+g.value===4?'Décès possible : protections effectives avant tout travail. ':'Cet indice ne décide pas de l’autorisation de travail. ')+'Une protection, un ancrage ou un secours manquant impose l’arrêt, quel que soit le score.'};
    ['g','p','e'].forEach(function(i){document.getElementById(i).addEventListener('change',upd)});upd()}
  var T=window.HeightTools,ta=document.getElementById('ta-form');
  function fr(n){return n.toFixed(2).replace('.',',')}
  if(ta&&T){var calc=function(){var r=T.clearance(document.getElementById('ta1').value,document.getElementById('ta5').value,document.getElementById('ta-ref').value),out=document.getElementById('ta-out');out.dataset.state=r.state;
    if(r.state==='invalid'){out.textContent='Saisir une valeur de notice strictement positive et une hauteur disponible positive ou nulle, en mètres. Les valeurs négatives et les saisies incomplètes sont refusées.';return}
    if(r.state==='reference'){out.textContent='Choisir le même repère de mesure pour la notice et la hauteur disponible. Des distances mesurées depuis des repères différents ne se comparent pas.';return}
    if(r.state==='insufficient'){out.textContent='ESPACE INSUFFISANT : '+fr(r.available)+' m disponibles pour '+fr(r.required)+' m requis. Déficit : '+fr(-r.delta)+' m. Ne pas utiliser cette configuration.';return}
    out.textContent='Comparaison géométrique : '+fr(r.available)+' m disponibles pour '+fr(r.required)+' m requis (écart : '+fr(r.delta)+' m). Ce résultat ne valide pas le système : vérifier la configuration de la notice, les obstacles, le pendule, les arêtes, les ancrages et le secours.';
  };ta.addEventListener('input',calc);ta.addEventListener('change',calc);calc()}
  var ff=document.getElementById('fc-form');
  if(ff&&T){var factor=function(){var r=T.factor(document.getElementById('fc1').value,document.getElementById('fc2').value),out=document.getElementById('fc-out');
    if(r.state==='invalid'){out.textContent='Saisir une hauteur de chute positive ou nulle et une longueur de liaison strictement positive, en mètres.';return}
    out.textContent='Facteur géométrique : '+fr(r.factor)+(r.state==='outside'?' — supérieur à 2 : hors du modèle simple, revoir les données et la configuration.':' — modèle simplifié. Ce rapport ne donne ni la force de choc, ni le tirant d’air, ni une autorisation d’utilisation.');
  };ff.addEventListener('input',factor);factor()}
  function restorePrint(){document.querySelectorAll('.print-exclude').forEach(function(e){e.classList.remove('print-exclude')})}
  window.addEventListener('afterprint',restorePrint);
  document.querySelectorAll('[data-print-section]').forEach(function(b){b.addEventListener('click',function(){restorePrint();var node=b.closest('section');if(!node)return;while(node&&node!==document.body){Array.prototype.forEach.call(node.parentElement.children,function(s){if(s!==node)s.classList.add('print-exclude')});node=node.parentElement}window.print()})});
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
      var r=document.getElementById('quiz-result');r.textContent='Résultat : '+s+' / '+QCM.length+(n<QCM.length?' ('+(QCM.length-n)+' sans réponse)':'')+'. Auto-évaluation : les résultats pratiques sont appréciés séparément.'});
    document.getElementById('reset-quiz').addEventListener('click',function(){qz.querySelectorAll('input').forEach(function(i){i.checked=false});qz.querySelectorAll('.feedback').forEach(function(x){x.textContent=''});document.getElementById('quiz-result').textContent=''});
  }
});
})();

