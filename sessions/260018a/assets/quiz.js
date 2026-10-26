function sh(a){a=a.slice();for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]]}return a}
const box=document.getElementById('quiz');let n=0,ok=0;
sh(Q).forEach((q,i)=>{const d=document.createElement('div');d.className='q';d.setAttribute('role','group');
const opts=sh(q.o.map((t,k)=>({t,k})));const h=document.createElement('p');h.innerHTML='<b>'+(i+1)+'. '+q.q+'</b>';d.appendChild(h);
const fb=document.createElement('p');fb.setAttribute('aria-live','polite');
opts.forEach(o=>{const l=document.createElement('label');const r=document.createElement('input');r.type='radio';r.name='q'+i;
r.onchange=()=>{if(d.dataset.done)return;d.dataset.done=1;n++;if(o.k===q.c){ok++;fb.innerHTML='<span class="ok">Juste.</span> '+q.e}else fb.innerHTML='<span class="ko">Pas tout à fait.</span> '+q.e;
document.getElementById('score').textContent=ok+' bonne(s) réponse(s) sur '+n+' répondue(s).'};
l.appendChild(r);l.append(' '+o.t);d.appendChild(l)});d.appendChild(fb);box.appendChild(d)});
