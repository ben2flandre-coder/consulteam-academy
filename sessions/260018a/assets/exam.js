function sh(a){a=a.slice();for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]]}return a}
const root=document.getElementById('exam');let items=[],t0,tick;
function start(){const pr=sh(QB.filter(q=>q.p)).slice(0,3),np=sh(QB.filter(q=>!q.p)).slice(0,27);
items=sh(pr.concat(np)).map(q=>({q,o:sh([q.c].concat(q.d).map((t,k)=>({t,k}))),a:null}));
root.innerHTML='<p class="timer" id="tm" role="timer"></p>';
items.forEach((it,i)=>{const d=document.createElement('div');d.className='q'+(it.q.p?' prio':'');
d.innerHTML='<p><b>'+(i+1)+'. '+it.q.q+'</b>'+(it.q.p?' <span class="chip">question prioritaire</span>':'')+'</p>';
it.o.concat([{t:'Je ne sais pas',k:-1}]).forEach(o=>{const l=document.createElement('label');const r=document.createElement('input');r.type='radio';r.name='e'+i;r.onchange=()=>{it.a=o.k};l.appendChild(r);l.append(' '+o.t);d.appendChild(l)});root.appendChild(d)});
const b=document.createElement('button');b.textContent='Terminer et voir mon résultat';b.onclick=finish;root.appendChild(b);
t0=Date.now();tick=setInterval(()=>{const s=Math.max(0,3600-Math.floor((Date.now()-t0)/1000));document.getElementById('tm').textContent='Temps restant : '+Math.floor(s/60)+' min '+String(s%60).padStart(2,'0')+' s';if(s===0)finish()},500)}
function finish(){clearInterval(tick);let pts=0,right=0,wrong=0,dk=0;
items.forEach(it=>{if(it.a===null||it.a===-1){dk++;return}if(it.a===0){pts+=2;right++}else{pts+=it.q.p?-5:-1;wrong++}});
const ok=pts>=36;let h='<h2>Résultat d\'entraînement</h2><p class="lead"><b>'+pts+' / 60</b> · seuil 36 · '+(ok?'<span class="ok">seuil atteint</span>':'<span class="ko">seuil non atteint</span>')+'</p><p>'+right+' bonne(s) · '+wrong+' mauvaise(s) · '+dk+' sans réponse ou « je ne sais pas ». Entraînement sans valeur de certification.</p><h2>Correction</h2>';
items.forEach((it,i)=>{const mine=it.a===null||it.a===-1?'sans réponse':(it.a===0?'juste':'faux');
h+='<details'+(mine==='juste'?'':' open')+'><summary>'+(i+1)+'. '+it.q.q+' — '+mine+'</summary><p>Bonne réponse : <b>'+it.q.c+'</b></p><p>'+it.q.e+'</p><p class="s"><span class="chip">Source</span> '+it.q.s+'</p></details>'});
h+='<p class="noprint"><button onclick="start()">Recommencer</button></p>';root.innerHTML=h;scrollTo(0,0)}
document.getElementById('go').onclick=()=>{document.getElementById('intro').hidden=true;start()};
