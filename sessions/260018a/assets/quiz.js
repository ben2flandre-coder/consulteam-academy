function sh(a){a=a.slice();for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]]}return a}
const box=document.getElementById('quiz');let n=0,ok=0;
const list=sh(QB).slice(0,20);
list.forEach((q,i)=>{const d=document.createElement('div');d.className='q';
const opts=sh([q.c].concat(q.d).map((t,k)=>({t,k})));
d.innerHTML='<p><b>'+(i+1)+'. '+q.q+'</b></p>';const fb=document.createElement('p');fb.setAttribute('aria-live','polite');
opts.forEach(o=>{const l=document.createElement('label');const r=document.createElement('input');r.type='radio';r.name='q'+i;
r.onchange=()=>{if(d.dataset.done)return;d.dataset.done=1;n++;const good=o.k===0;if(good)ok++;fb.innerHTML=(good?'<span class="ok">Juste.</span> ':'<span class="ko">Pas tout à fait.</span> Bonne réponse : '+q.c+'. ')+q.e+' <span class="chip">'+q.s+'</span>';
document.getElementById('score').textContent=ok+' bonne(s) réponse(s) sur '+n+' répondue(s).'+(n===list.length?(ok/list.length>=0.7?' Seuil pédagogique de 70 % atteint.':' Seuil pédagogique de 70 % non atteint : relisez les pages concernées, puis recommencez.')+' Repère pédagogique sans valeur de certification.':'')};
l.appendChild(r);l.append(' '+o.t);d.appendChild(l)});d.appendChild(fb);box.appendChild(d)});
