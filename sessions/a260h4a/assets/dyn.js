/* Couche dynamique de la plateforme A260H4A : défi du jour, questions flash, progression, apparition douce.
   Les questions viennent de qbank.js (les mêmes que l'évaluation théorique). Rien n'est transmis : tout reste dans le navigateur. */
(function(){'use strict';
var CODE='a260h4a',QB=window.QB||[];
function $(s,r){return (r||document).querySelector(s)}
function ls(k,v){try{if(v===undefined){var x=localStorage.getItem(k);return x?JSON.parse(x):null}localStorage.setItem(k,JSON.stringify(v))}catch(e){return null}}
function rng(seed){var s=seed>>>0||1;return function(){s=(s*1664525+1013904223)>>>0;return s/4294967296}}
function shuffle(a,r){a=a.slice();for(var i=a.length-1;i>0;i--){var j=Math.floor(r()*(i+1)),t=a[i];a[i]=a[j];a[j]=t}return a}
function today(){var d=new Date();return d.getFullYear()+'-'+('0'+(d.getMonth()+1)).slice(-2)+'-'+('0'+d.getDate()).slice(-2)}
function dayNum(){var d=new Date();return Math.floor(Date.UTC(d.getFullYear(),d.getMonth(),d.getDate())/864e5)}
function esc(t){return String(t).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
function card(qi,seed,onDone){
  var q=QB[qi],r=rng(seed),idx=shuffle(q.o.map(function(_,i){return i}),r),box=document.createElement('div');box.className='dq-card';
  var h='<p class="dq-q"><b>'+esc(q.q)+'</b></p><div class="dq-opts" role="group" aria-label="Réponses">';
  idx.forEach(function(j){h+='<button type="button" class="dq-o" data-j="'+j+'">'+esc(q.o[j])+'</button>'});
  h+='</div><div class="dq-fb" role="status" aria-live="polite" hidden></div>';box.innerHTML=h;
  box.addEventListener('click',function(e){var b=e.target.closest('.dq-o');if(!b||box.dataset.done)return;box.dataset.done='1';
    var j=+b.dataset.j,ok=j===q.c;[].forEach.call(box.querySelectorAll('.dq-o'),function(x){x.disabled=true;if(+x.dataset.j===q.c)x.classList.add('good');else if(x===b)x.classList.add('bad')});
    var fb=$('.dq-fb',box);fb.hidden=false;fb.className='dq-fb '+(ok?'ok':'ko');fb.innerHTML='<b>'+(ok?'Bonne réponse.':'Pas tout à fait.')+'</b> '+esc(q.e);
    if(onDone)onDone(ok,box)});
  return box}
function defi(){
  var host=$('#defi');if(!host||!QB.length)return;
  var t=today(),st=ls('h4a.defi')||{days:{},best:0},n=dayNum(),qi=n%QB.length,extra=0;
  host.innerHTML='<div class="dq-head"><h2>⚡ Défi du jour</h2><span class="dq-streak" id="dqs"></span></div><p class="dq-sub">Une question pour s’échauffer, avec la réponse expliquée. Le résultat reste dans votre navigateur.</p><div id="dqb"></div><div class="dq-actions"><button type="button" class="dq-btn" id="dqn" hidden>Une autre question</button> <a class="dq-link" href="flash.html">Série de 5 questions flash →</a></div>';
  function streak(){var s=0,d=new Date();for(;;){var k=d.getFullYear()+'-'+('0'+(d.getMonth()+1)).slice(-2)+'-'+('0'+d.getDate()).slice(-2);if(st.days[k]!==undefined){s++;d.setDate(d.getDate()-1)}else if(s===0&&k===t){d.setDate(d.getDate()-1)}else break}return s}
  function show(){var s=streak();$('#dqs').textContent=s>1?'🔥 '+s+' jours de suite':(Object.keys(st.days).length?'Déjà '+Object.keys(st.days).length+' défi(s) relevé(s)':'')}
  function put(i,seed,first){var b=$('#dqb');b.innerHTML='';b.appendChild(card(i,seed,function(ok){if(first){st.days[t]=ok?1:0;ls('h4a.defi',st);show()}$('#dqn').hidden=false}))}
  put(qi,n,true);show();
  $('#dqn').addEventListener('click',function(){extra++;this.hidden=true;put((qi+extra*7)%QB.length,n+extra,false)})}
function flash(){
  var host=$('#flash');if(!host||!QB.length)return;var N=5,r=Math.random,order,pos,score,res;
  function start(){order=shuffle(QB.map(function(_,i){return i}),r).slice(0,N);pos=0;score=0;res=[];next()}
  function next(){if(pos>=N)return end();var w=document.createElement('div');w.innerHTML='<div class="fl-bar"><div style="width:'+(pos/N*100)+'%"></div></div><p class="fl-n">Question '+(pos+1)+' sur '+N+(score?' · '+score+' juste'+(score>1?'s':''):'')+'</p>';
    var c=card(order[pos],Math.floor(r()*1e9),function(ok){if(ok)score++;res.push([order[pos],ok]);var b=document.createElement('button');b.className='dq-btn';b.type='button';b.textContent=pos+1<N?'Question suivante':'Voir mon résultat';b.addEventListener('click',function(){pos++;next()});c.appendChild(b);b.focus()});
    w.appendChild(c);host.innerHTML='';host.appendChild(w)}
  function end(){var st=ls('h4a.flash')||{best:0,n:0};st.n++;if(score>st.best)st.best=score;ls('h4a.flash',st);
    var m=score===N?'Sans faute.':score>=4?'Très bien.':score>=3?'Correct : relisez les explications des erreurs.':'À reprendre : le socle électrique et le parcours vous aident à revoir les notions.';
    var h='<div class="fl-end"><p class="fl-score">'+score+' / '+N+'</p><p>'+m+'</p><ul class="fl-rev">';
    res.forEach(function(x){h+='<li class="'+(x[1]?'ok':'ko')+'">'+(x[1]?'✔ ':'✘ ')+esc(QB[x[0]].q)+(x[1]?'':'<br><small>'+esc(QB[x[0]].o[QB[x[0]].c])+'</small>')+'</li>'});
    h+='</ul><p class="fl-best">Meilleur score : '+st.best+' / '+N+' · '+st.n+' série(s) jouée(s)</p><p><button class="dq-btn" id="flr" type="button">Rejouer 5 questions</button> <a class="dq-link" href="parcours.html">Retour au parcours</a> · <a class="dq-link" href="evaluation.html">Évaluation complète (40 questions)</a></p><p class="dq-sub">Cet entraînement ne remplace ni l’évaluation de la session ni l’habilitation, délivrée par l’employeur.</p></div>';
    host.innerHTML=h;$('#flr').addEventListener('click',start);var f=$('#flr');if(f)f.focus()}
  start()}
function progress(){
  var host=$('#prog');if(!host)return;var done=ls('pp.'+CODE+'.done'),n=0;
  if(done&&typeof done==='object')n=Array.isArray(done)?done.length:Object.keys(done).filter(function(k){return done[k]}).length;
  var T=9,p=Math.round(n/T*100),d=ls('h4a.defi')||{days:{}},f=ls('h4a.flash')||{best:0,n:0};
  host.innerHTML='<div class="pg-ring" style="--p:'+p+'"><span>'+n+'/'+T+'</span></div><div><h2>Votre progression</h2><p>'+(n?n+' séquence'+(n>1?'s':'')+' terminée'+(n>1?'s':'')+' sur '+T+'.':'Aucune séquence terminée pour le moment.')+' <a href="parcours.html">'+(n?'Reprendre le parcours':'Commencer le parcours')+'</a></p><p class="dq-sub">Défis relevés : '+Object.keys(d.days).length+' · Meilleur score flash : '+f.best+' / 5. Ces repères restent dans ce navigateur.</p></div>'}
function reveal(){
  if(!('IntersectionObserver' in window)||matchMedia('(prefers-reduced-motion: reduce)').matches)return;
  var els=[].slice.call(document.querySelectorAll('main .card,main .seq,main .q,main .sit'));
  els.forEach(function(e){e.classList.add('rv')});
  var io=new IntersectionObserver(function(es){es.forEach(function(x){if(x.isIntersecting){x.target.classList.add('rv-in');io.unobserve(x.target)}})},{rootMargin:'0px 0px -6% 0px'});
  els.forEach(function(e){io.observe(e)});
  setTimeout(function(){els.forEach(function(e){e.classList.add('rv-in')})},2500)}
function init(){defi();flash();progress();reveal()}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init()
})();
