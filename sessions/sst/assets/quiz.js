(function(){var Q=window.__Q||[];
function el(t,c,x){var e=document.createElement(t);if(c)e.className=c;if(x!==undefined)e.textContent=x;return e}
function mount(box){var comps=(box.getAttribute('data-comp')||'').split(',').filter(Boolean);
var qs=Q.filter(function(q){return !comps.length||comps.indexOf(q.competence)>-1});
var by={};qs.forEach(function(q){(by[q.competence]=by[q.competence]||[]).push(q)});
var score=el('p','score');score.setAttribute('aria-live','polite');var done={},good={};
function upd(){var n=Object.keys(done).length,g=Object.keys(good).length;score.textContent=n?('Réponses justes : '+g+' sur '+n+' question'+(n>1?'s':'')+' vérifiée'+(n>1?'s':'')+' (sur '+qs.length+').'):'';}
Object.keys(by).forEach(function(c){var s=el('section','qsec');if(!comps.length||comps.length>1){s.appendChild(el('h2',null,c+' — '+(window.__T&&window.__T[c]||'')))}
by[c].forEach(function(q,i){var f=el('fieldset','q');f.appendChild(el('legend',null,(i+1)+'. '+q.question));
q.options.forEach(function(o,k){var l=el('label');var r=el('input');r.type='radio';r.name=q.id;r.value=k;l.appendChild(r);l.appendChild(document.createTextNode(' '+o));f.appendChild(l)});
var b=el('button',null,'Vérifier');b.type='button';var r=el('p','expl');r.setAttribute('aria-live','polite');
b.onclick=function(){var ch=f.querySelector('input:checked');if(!ch){r.textContent='Choisissez une réponse.';return}
var ok=+ch.value===q.bonne;done[q.id]=1;if(ok)good[q.id]=1;else delete good[q.id];f.className='q '+(ok?'good':'bad');
r.textContent='';r.appendChild(el('b',null,ok?'Correct. ':'Pas tout à fait. '));r.appendChild(document.createTextNode(q.correction+' '));
var sm=el('small',null,'Source : '+q.source+'. ');r.appendChild(sm);var a=el('a',null,'Revoir la leçon');a.setAttribute('href','m'+q.competence.slice(1)+'.html#retenir');r.appendChild(a);upd()};
f.appendChild(b);f.appendChild(r);s.appendChild(f)});box.appendChild(s)});
var rb=el('button','alt','Recommencer');rb.type='button';rb.onclick=function(){box.innerHTML='';mount(box)};box.appendChild(score);box.appendChild(rb)}
Array.prototype.forEach.call(document.querySelectorAll('.quiz'),mount)})();