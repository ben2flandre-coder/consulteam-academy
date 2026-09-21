(()=>{'use strict';
const $=(s)=>document.querySelector(s);
const menu=$('.menu-toggle');menu?.addEventListener('click',()=>{const open=$('#navigation').classList.toggle('open');menu.setAttribute('aria-expanded',String(open))});
const theme=$('#theme'),themeKey='consulteam-adonis-theme';
const setTheme=mode=>{const night=mode==='night';document.body.classList.toggle('night',night);document.documentElement.dataset.theme=mode;document.querySelectorAll('h1,h2,h3,p,li,td,th,label,.sidebar a,.brandline b').forEach(e=>e.style.color=night?'#f3f7fc':'');document.querySelectorAll('.card,.lesson,details,.module-toolbar,.journey,.quick-tools,.aside-pulse').forEach(e=>{e.style.backgroundColor=night?'#182a40':'';e.style.borderColor=night?'#5c7590':''});document.body.style.backgroundColor=night?'#0d1726':'';if(theme){theme.setAttribute('aria-pressed',String(night));theme.innerHTML=night?'☀️ <span>Mode jour</span>':'🌙 <span>Mode nuit</span>'}};
try{setTheme(localStorage.getItem(themeKey)==='night'?'night':'day')}catch{setTheme('day')}
theme?.addEventListener('click',()=>{const mode=document.body.classList.contains('night')?'day':'night';try{localStorage.setItem(themeKey,mode)}catch{}setTheme(mode)});
document.querySelectorAll('.print').forEach(b=>b.addEventListener('click',()=>window.print()));
let closed=[];window.addEventListener('beforeprint',()=>{closed=[...document.querySelectorAll('details:not([open])')];closed.forEach(d=>d.open=true)});window.addEventListener('afterprint',()=>closed.forEach(d=>d.open=false));
$('#expand')?.addEventListener('click',()=>{const ds=[...document.querySelectorAll('details.deep')];const open=ds.some(d=>!d.open);ds.forEach(d=>d.open=open);$('#expand').textContent=open?'Fermer les approfondissements':'Ouvrir les approfondissements'});
const normal=s=>s.normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase();
$('#search')?.addEventListener('input',e=>{let n=0;const t=normal(e.target.value.trim());document.querySelectorAll('.lesson').forEach(l=>{l.hidden=!normal(l.textContent).includes(t);if(!l.hidden)n++});$('#search-status').textContent=t?`${n} séquence(s) trouvée(s).`:''});
document.querySelectorAll('.check-micro').forEach(b=>b.addEventListener('click',()=>{const f=b.closest('.micro'),v=f.querySelector('input:checked'),o=f.querySelector('.feedback');if(!v){o.textContent='Choisissez une réponse avant de vérifier.';o.className='feedback ko';return}const ok=v.value===f.dataset.answer;o.textContent=(ok?'Correct. ':'À reprendre. ')+f.dataset.feedback;o.className='feedback '+(ok?'ok':'ko')}));
const zoom=$('#zoom');let origin=null;
document.querySelectorAll('.zoom-image').forEach(b=>b.addEventListener('click',()=>{origin=b;const im=b.querySelector('img');zoom.querySelector('img').src=im.src;zoom.querySelector('img').alt=im.alt;zoom.querySelector('p').textContent=im.alt;zoom.showModal()}));
zoom?.querySelector('.close').addEventListener('click',()=>zoom.close());zoom?.addEventListener('close',()=>origin?.focus());zoom?.addEventListener('click',e=>{if(e.target===zoom)zoom.close()});
$('#export-notes')?.addEventListener('click',()=>{const t=[...document.querySelectorAll('[data-note]')].map(x=>x.dataset.note+'\n'+x.value).join('\n\n');download('notes-adonis.txt',t,'text/plain;charset=utf-8')});
function download(name,text,type){const url=URL.createObjectURL(new Blob([text],{type}));const a=document.createElement('a');a.href=url;a.download=name;a.click();setTimeout(()=>URL.revokeObjectURL(url),1000)}
})();
// Les calculateurs PMS/HSE (criticité HACCP, cotation EvRP, audits, évaluation)
// sont désormais des outils complets : voir assets/tools-engine.js.
