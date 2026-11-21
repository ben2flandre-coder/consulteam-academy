/* Nœuds : choix par usage + recherche, et mode pas-à-pas des cheminements */
(function(){
'use strict';
function norm(s){return (s||'').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g,'')}
document.addEventListener('DOMContentLoaded',function(){
  var box=document.getElementById('choisir');if(!box)return;
  var q=document.getElementById('nq'),chips=box.querySelectorAll('[data-f]'),cards=box.querySelectorAll('.kn'),out=document.getElementById('nres'),f='tous';
  function apply(){var t=norm(q.value),n=0;
    cards.forEach(function(c){var ok=(f==='tous'||c.dataset.u===f)&&(!t||norm(c.textContent+' '+(c.dataset.k||'')).indexOf(t)>-1);c.hidden=!ok;if(ok)n++});
    out.textContent=n+(n>1?' fiches affichées':' fiche affichée')+(n===0?' : essayer un autre mot ou « Tous ».':'.');}
  chips.forEach(function(b){b.addEventListener('click',function(){f=b.dataset.f;chips.forEach(function(x){x.setAttribute('aria-pressed',x===b)});apply()})});
  q.addEventListener('input',apply);apply();
  /* liens vers un onglet de la page */
  box.querySelectorAll('[data-tab]').forEach(function(a){a.addEventListener('click',function(e){e.preventDefault();
    var b=document.querySelectorAll('.tabs[data-tabs] button')[+a.dataset.tab];if(b){b.click();var h=document.getElementById('fiches');if(h)h.scrollIntoView({behavior:'smooth',block:'start'})}})});
  /* pas-à-pas */
  document.querySelectorAll('#fiches ol.check').forEach(function(ol){
    var items=ol.querySelectorAll(':scope > li');if(items.length<2)return;
    var bar=document.createElement('div');bar.className='stepbar noprint';
    var go=document.createElement('button');go.type='button';go.className='btn alt';go.textContent='Voir étape par étape';
    var ctl=document.createElement('div');ctl.className='stepctl';ctl.hidden=true;
    ctl.innerHTML='<button type="button" class="btn alt" data-d="-1">← Précédente</button><span class="stepn" aria-live="polite"></span><button type="button" class="btn" data-d="1">Suivante →</button><button type="button" class="btn alt" data-x="1">Tout afficher</button>';
    bar.appendChild(go);bar.appendChild(ctl);ol.parentNode.insertBefore(bar,ol);
    var i=0,on=false;
    function show(){items.forEach(function(li,j){li.classList.toggle('cur',on&&j===i)});ol.classList.toggle('stepmode',on);ctl.hidden=!on;go.hidden=on;
      ctl.querySelector('.stepn').textContent='Étape '+(i+1)+' / '+items.length;
      ctl.querySelector('[data-d="-1"]').disabled=i===0;ctl.querySelector('[data-d="1"]').disabled=i===items.length-1}
    go.addEventListener('click',function(){on=true;i=0;show()});
    ctl.addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;
      if(b.dataset.x){on=false}else{i=Math.max(0,Math.min(items.length-1,i+(+b.dataset.d)))}show()});
    show();
  });
});
})();
