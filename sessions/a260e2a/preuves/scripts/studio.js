/* Studio de module : Voir > Comprendre > Faire > Vérifier > Retenir */
var PH=[['voir','Voir'],['comprendre','Comprendre'],['faire','Faire'],['verifier','Vérifier'],['retenir','Retenir']];
var MEM={};
function sto(k,v){var K='a260e2a.'+k;try{if(v===undefined){var r=localStorage.getItem(K);return r?JSON.parse(r):(MEM[K]||null)}localStorage.setItem(K,JSON.stringify(v))}catch(e){if(v===undefined)return MEM[K]||null;MEM[K]=v}}
function prog(id){return sto('p'+id)||{}}
function mark(id,ph,val){var p=prog(id);p[ph]=val===undefined?1:val;sto('p'+id,p)}
function nDone(id){var p=prog(id);return PH.filter(function(x){return p[x[0]]}).length}
var QS={};
var SYM=[['B0 · H0 · H0V',['B0','H0','H0V']],['BS',['BS']],['BE',['BE']],['BR',['BR']],['BC',['BC']],['B1 · B2',['B1','B1V','B2','B2V']],['H1 · H2',['H1','H1V','H2','H2V']],['HC',['HC']],['HE',['HE']]];
function hit(m,keys){return (m.niveaux||[]).some(function(n){return keys.indexOf(n)>=0})}
function card(m){var n=nDone(m.id),done=n===5;return '<a class="card k2'+(done?' fini':'')+'" href="#m'+m.id+'" data-m="'+m.id+'"><span class="cap"><span class="mico">'+ico(MICO[m.id]||'bolt')+'</span><b>'+m.id+'</b></span>'+E(m.title)+'<small>'+statTag(m.statut)+E(m.goal)+'</small><span class="mini" aria-label="Avancement"><i style="width:'+(n*20)+'%"></i></span><small class="av">'+(done?'Terminé':n?n+' phase(s) sur 5':'À commencer')+'</small></a>'}
function liste(sym){
var fin=A.modules.filter(function(m){return nDone(m.id)===5}).length;
var h='<p class="lead">Choisissez votre objectif : le parcours conseillé se compose pour vous. Tous les niveaux restent accessibles, dans l’ordre que vous voulez.</p>';
h+='<div class="bar" role="img" aria-label="Avancement"><i style="width:'+Math.round(100*fin/A.modules.length)+'%"></i></div><p class="expl">'+fin+' module(s) terminé(s) sur '+A.modules.length+'. L’avancement reste dans ce navigateur : rien n’est envoyé.</p>';
h+='<h2>Mon objectif</h2><div class="chips" role="group" aria-label="Symbole visé">'+SYM.map(function(s,i){return '<button type="button" class="chip'+(sym===i?' on':'')+'" data-sym="'+i+'">'+E(s[0])+'</button>'}).join('')+'<button type="button" class="chip'+(sym==null?' on':'')+'" data-sym="-1">Voir tout</button></div>';
if(sym!=null&&SYM[sym]){var keys=SYM[sym][1],soc=GROUPS[0][2].map(module),cible=A.modules.filter(function(m){return hit(m,keys)&&soc.indexOf(m)<0}),ordre=soc.concat(cible);
h+='<div class="note"><b>Parcours conseillé pour '+E(SYM[sym][0])+'.</b> D’abord le socle commun, puis les modules du symbole. Les autres modules restent consultables plus bas.</div><div class="grid route">'+ordre.map(function(m,i){return card(m).replace('class="card k2','class="card k2 rt').replace('">'+m.id+'. ','"><b class="rn">Étape '+(i+1)+'</b> '+m.id+'. ')}).join('')+'</div><h2>Tous les modules</h2>'}
h+='<nav class="sommaire no-print">'+GROUPS.map(function(g,i){return '<a href="#g'+i+'">'+E(g[0])+'</a>'}).join('')+'</nav>';
GROUPS.forEach(function(g,i){h+='<h2 id="g'+i+'">'+E(g[0])+'</h2><p>'+E(g[1])+'</p><div class="grid">'+g[2].map(function(id){return card(module(id))}).join('')+'</div>'});
h+='<div class="note"><b>Lecture.</b> « Contenu repris » vient des supports Consul Team existants (A2604MA, A260BNA). « Nouveau, à valider » a été rédigé à partir de sources lues et attend la relecture du formateur.</div>';
out.innerHTML=h;scrollTo(0,0)}
/* ---------- questions et exercices ---------- */
function qcard(x,id,o){o=o||{};var t=x.type||'s',opts=x.options.map(function(v,i){return{t:v,i:i,ok:t==='s'?i===x.correct:t==='m'?x.correct.indexOf(i)>=0:false}}),sh=shuffle(opts);
QS[id]={x:x,t:t,o:sh,lvl:0,aids:!!o.aids};
var h='<fieldset class="q qc" data-id="'+id+'"><legend>'+E(x.q)+'</legend>';
if(t==='o'){h+='<p class="expl">Attribuez à chaque étape son rang (1 = première).</p>';sh.forEach(function(p,j){h+='<label class="opt" data-j="'+j+'"><select aria-label="Rang"><option value="">–</option>'+sh.map(function(_,k){return '<option value="'+k+'">'+(k+1)+'</option>'}).join('')+'</select><span>'+E(p.t)+'</span></label>'})}
else{if(t==='m')h+='<p class="expl">Plusieurs réponses possibles.</p>';sh.forEach(function(p,j){h+='<label class="opt" data-j="'+j+'"><input type="'+(t==='m'?'checkbox':'radio')+'" name="'+id+'" value="'+j+'"><span>'+E(p.t)+'</span></label>'})}
if(!o.noBtn)h+='<div class="qa"><button type="button" data-act="chk">Valider</button>'+(o.aids?'<button type="button" class="ghost" data-act="aid">Un coup de pouce</button>':'')+'</div>';
return h+'<div class="qr" aria-live="polite"></div></fieldset>'}
function grade(fs){var r=QS[fs.dataset.id],ok=false,given=false,lab=fs.querySelectorAll('.opt');
[].forEach.call(lab,function(l){l.classList.remove('good','bad')});
if(r.t==='o'){ok=true;[].forEach.call(lab,function(l,j){var v=l.querySelector('select').value;if(v!=='')given=true;var good=v!==''&&+v===r.o[j].i;if(!good)ok=false;l.classList.add(good?'good':'bad')})}
else{var picked=[];[].forEach.call(fs.querySelectorAll('input:checked'),function(x){picked.push(+x.value)});given=picked.length>0;ok=given&&r.o.every(function(p,j){return p.ok===(picked.indexOf(j)>=0)});r.o.forEach(function(p,j){if(p.ok)lab[j].classList.add('good');else if(picked.indexOf(j)>=0)lab[j].classList.add('bad')})}
fs.classList.remove('good','bad');if(given)fs.classList.add(ok?'good':'bad');
fs.querySelector('.qr').innerHTML=given?'<div class="'+(ok?'ok':'note')+'"><b>'+(ok?'Juste.':'À revoir.')+'</b> '+E(r.x.why||'')+'</div>':'<div class="note">Choisissez au moins une réponse.</div>';
return{ok:ok,given:given}}
function aid(fs,mid){var r=QS[fs.dataset.id],m=module(mid),box=fs.querySelector('.qr');r.lvl++;
if(r.lvl===1){var titres=(m.sections||[]).map(function(s){return s[0]});box.innerHTML='<div class="tip"><b>Coup de pouce 1.</b> Objectif du module : '+E(m.goal)+(titres.length?' Relisez, dans « Comprendre » : '+titres.map(function(t){return '« '+E(t)+' »'}).join(', ')+'.':' Relisez la phase « Comprendre ».')+'</div>'}
else if(r.lvl===2){var msg='';
if(r.t==='o'){var f=r.o.filter(function(p){return p.i===0})[0];msg='La première étape est : « '+E(f.t)+' ».'}
else{var wrong=r.o.map(function(p,j){return p.ok?-1:j}).filter(function(j){return j>=0&&!fs.querySelectorAll('.opt')[j].classList.contains('out')});if(wrong.length){var j=wrong[Math.floor(Math.random()*wrong.length)],l=fs.querySelectorAll('.opt')[j];l.classList.add('out');var inp=l.querySelector('input');if(inp){inp.checked=false;inp.disabled=true}msg='Une proposition fausse est barrée.'}}
box.innerHTML='<div class="tip"><b>Coup de pouce 2.</b> '+msg+' Validez pour voir l’explication.</div>'}
else box.innerHTML='<div class="tip">Plus d’aide possible : validez pour voir la réponse expliquée.</div>'}
document.addEventListener('click',function(e){var b=e.target.closest&&e.target.closest('[data-act],[data-sym],[data-ph],[data-pas]');if(!b)return;
if(b.dataset.sym!==undefined){var v=+b.dataset.sym;liste(v<0?null:v);return}
var host=b.closest('.studio'),mid=host?+host.dataset.m:0;
if(b.dataset.ph){if(b.closest('.next')&&b.dataset.ph!=='fin')mark(mid,host.dataset.cur);go(mid,b.dataset.ph);return}
if(b.dataset.act==='chk'){var fs=b.closest('fieldset');grade(fs);return}
if(b.dataset.act==='aid'){aid(b.closest('fieldset'),mid);return}
if(b.dataset.act==='all'){[].forEach.call(host.querySelectorAll('details.sc'),function(d){d.open=true});return}
if(b.dataset.act==='fin'){var fm=host.querySelector('#fv'),s=0,n=0;[].forEach.call(fm.querySelectorAll('fieldset'),function(fs){var g=grade(fs);n++;if(g.ok)s++});var seuil=Math.round(n*0.7);mark(mid,'verifier',{s:s,n:n});host.querySelector('#vres').innerHTML='<div class="'+(s>=Math.ceil(n*0.7)?'ok':'note')+'"><b>Score : '+s+' / '+n+'.</b> '+(s===n?'Sans faute.':'Reprenez les points à revoir dans « Comprendre », puis réessayez après un temps.')+' Repère de formation : 70 % (INRS ED 6127). Cet exercice ne remplace pas l’évaluation finale.</div>';host.querySelector('#vres').scrollIntoView({block:'center'});refresh(mid);return}
if(b.dataset.act==='retry'){go(mid,'verifier',true);return}
if(b.dataset.pas){pas(b);return}
});
/* ---------- pas à pas ---------- */
function pas(b){var host=b.closest('.pasbox'),act=b.dataset.pas,st=host._st;
if(act==='start'){host._ol=host.querySelector('ol');host._ol.hidden=true;st=host._st={k:0,n:host._ol.children.length};}
else if(act==='next')st.k++;else if(act==='prev')st.k=Math.max(0,st.k-1);else if(act==='list'){host._st=null;host.innerHTML=host._orig;return}
drawpas(host)}
function drawpas(host){var st=host._st,steps=[].slice.call(host._ol.children),h='';
if(st.k>=st.n){host.querySelector('.pv').innerHTML='<div class="ok"><b>Procédure déroulée.</b> Relisez l’ordre complet, puis passez à « Faire » pour la mettre en situation.</div><p><button type="button" class="ghost" data-pas="list">Revoir la liste complète</button> <button type="button" class="ghost" data-pas="prev">Revenir à la dernière étape</button></p>';return}
var dots='';for(var i=0;i<st.n;i++)dots+='<i class="'+(i<st.k?'d':i===st.k?'c':'')+'"></i>';
host.querySelector('.pv').innerHTML='<div class="pcard"><div class="pdots" aria-hidden="true">'+dots+'</div><b class="pn">Étape '+(st.k+1)+' sur '+st.n+'</b><div class="pt">'+steps[st.k].innerHTML+'</div><p class="expl">Point d’arrêt : cette étape est-elle faite et vérifiée ? Sinon, ne passez pas à la suivante.</p><p>'+(st.k>0?'<button type="button" class="ghost" data-pas="prev">← Précédente</button> ':'')+'<button type="button" data-pas="next">'+(st.k===st.n-1?'Terminer la procédure':'Étape faite, suivante →')+'</button> <button type="button" class="ghost" data-pas="list">Liste complète</button></p></div>'}
function wrapPas(root){[].forEach.call(root.querySelectorAll('ol:not(.steps)'),function(ol){if(ol.children.length<3||ol.closest('.pasbox'))return;var w=document.createElement('div');w.className='pasbox';ol.parentNode.insertBefore(w,ol);w.appendChild(ol);var bar=document.createElement('p');bar.className='pbar no-print';bar.innerHTML='<button type="button" class="ghost" data-pas="start">▶ Dérouler cette procédure pas à pas</button>';w.insertBefore(bar,ol);var pv=document.createElement('div');pv.className='pv';w.appendChild(pv);w._orig=w.innerHTML})}
/* ---------- visuels à observer ---------- */
function figs(m){var items=[];
(m.images||[]).forEach(function(i){var v=vis(i);if(v)items.push('<figure class="ia"><img src="'+E(v.fichier)+'" alt="'+E(v.id+' · '+v.titre)+'" loading="lazy"><figcaption><b>'+E(v.id)+' · '+E(v.titre)+'</b><details class="leg"><summary>Voir la légende</summary><small>'+E(v.legende)+' Image générée par IA, illustration non contractuelle.</small></details></figcaption></figure>')});
(m.figures||[]).forEach(function(f){items.push('<figure><img src="'+E(f[0])+'" alt="'+E(f[1])+'" loading="lazy"><figcaption>'+E(f[1])+'</figcaption></figure>')});
return items.length?'<p class="expl">À faire : observez chaque visuel. Que reconnaissez-vous ? Que faut-il vérifier avant d’agir ? Ouvrez ensuite la légende pour confronter.</p><div class="gal" style="margin:10px 0 22px">'+items.join('')+'</div>':''}
/* ---------- le studio ---------- */
function minutes(m){var t=(m.html||'').replace(/<[^>]+>/g,' ')+' '+(m.sections||[]).map(function(s){return s[0]+' '+s[1]}).join(' ');return Math.max(2,Math.round(t.split(/\s+/).length/170))}
function split(m){var q=m.questions||[],n=q.length,nf=n>=2?Math.ceil(n/2):0;return{f:q.slice(0,nf),v:q.slice(nf)}}
function FMT(t){var L=String(t).split('\n'),h='',ol=false;L.forEach(function(l){var m=/^\d+\)\s+(.*)$/.exec(l);if(m){if(!ol){h+='<ol>';ol=true}h+='<li>'+E(m[1])+'</li>'}else{if(ol){h+='</ol>';ol=false}if(l.trim())h+='<p>'+E(l)+'</p>'}});if(ol)h+='</ol>';return h}
function ENH(h){
h=h.replace(/<p>([^<]{50,})<\/p>/g,function(_,x){var ss=x.split(/(?<=[.!?])\s+(?=[A-ZÀÂÉÈÊÎÔÛÇ«(])/);return '<p>'+ss.map(function(z,i){var w=/(interdit|jamais|danger|s’arrêt|s'arrêt|on s’arrête|on s'arrête|dépasse|ne se juge pas|ne met pas|sans danger|brûlure|chute)/i.test(z)&&ss.length>1;return w?'<span class="wn">'+ico('alert')+' '+z+'</span>':(i===0&&ss.length>2?'<b class="lead1">'+z+'</b>':z)}).join(' ')+'</p>'});
h=h.replace(/<section class="card"><h3><span class="no">(\d+)<\/span> ([^<]*)<\/h3>/g,function(_,n,t){var a=/^Chez ADI/.test(t);return '<section class="card'+(a?' adi':'')+'"><h3><span class="sico">'+ico(icoFor(t))+'</span><span class="no">'+n+'</span> '+t+'</h3>'});
h=h.replace(/<details class="sc"( open)?><summary><span class="no">(\d+)<\/span> ([^<]*)<\/summary>/g,function(_,o,n,t){var a=/^Chez ADI/.test(t);return '<details class="sc'+(a?' adi':'')+'"'+(o||'')+'><summary><span class="sico">'+ico(icoFor(t))+'</span><span class="no">'+n+'</span> '+t+'</summary>'});
h=h.replace(/<div class="callout card" style="[^"]*"><b>Situation de départ\.<\/b> ([\s\S]*?)<\/div>/g,function(_,x){return '<div class="callout card hook"><span class="hico">'+ico('target')+'</span><div><small>Mise en situation · que feriez-vous ?</small>'+x+'</div></div>'});
h=h.replace(/<div class="card sit"><h3>Mise en situation<\/h3>/g,'<div class="card sit"><h3>'+ico('target')+' À vous de décider</h3>');
h=h.replace(/<h3>Avant d’agir<\/h3>(<ul( class="chk")?>[\s\S]*?<\/ul>)/g,function(_,u){return '<div class="reflex"><h3>'+ico('shield')+' Réflexes avant d’agir</h3>'+u+'</div>'});
return h}
function panel(m,ph){return ENH(panel0(m,ph))}
function panel0(m,ph){var h='',sp=split(m),nx=ph==='tout'?null:PH[PH.map(function(p){return p[0]}).indexOf(ph)+1];
if(ph==='tout'){h+='<h2>Le module en entier</h2><p class="expl">Lecture continue : tout le contenu du module sur une page, sans étape à franchir. Les phases guidées (Voir, Faire, Vérifier) sont dans la barre ci-dessus.</p>';
if(m.scenario)h+='<div class="callout card" style="border-left:7px solid var(--y);background:#fff1d4;color:#16273d"><b>Situation de départ.</b> '+E(m.scenario)+'</div>';
h+='<div class="goal"><b>Objectif :</b> '+E(m.goal)+'</div>';
if(m.html)h+='<div class="sec">'+m.html+'</div>';
m.sections.forEach(function(s,i){h+='<section class="card"><h3><span class="no">'+(i+1)+'</span> '+E(s[0])+'</h3>'+FMT(s[1])+'</section>'});
h+=figs(m);
if(m.decision)h+='<div class="card sit"><h3>Mise en situation</h3><p>'+E(m.decision)+'</p><details><summary>Voir la réponse</summary><p>'+E(m.answer)+'</p></details></div>';
if(m.check&&m.check.length)h+='<h3>Avant d’agir</h3><ul>'+m.check.map(function(c){return '<li>'+E(c)+'</li>'}).join('')+'</ul>';
if(m.note)h+='<div class="note">'+E(m.note)+'</div>';
h+='<p class="expl">Source : '+E(m.source)+'</p><p class="next no-print"><button type="button" data-ph="voir">Suivre la version guidée →</button></p>';
return h}
if(ph==='voir'){h+='<h2>Voir</h2>';if(m.scenario)h+='<div class="callout card" style="border-left:7px solid var(--y);background:#fff1d4;color:#16273d"><b>Situation de départ.</b> '+E(m.scenario)+'</div>';h+='<div class="goal"><b>À la fin de ce module, vous saurez :</b> '+E(m.goal)+'</div>'+figs(m);if(m.note)h+='<div class="note">'+E(m.note)+'</div>';if(!(m.images||[]).length&&!(m.figures||[]).length)h+='<p class="expl">Pas de visuel pour ce module : passez directement à « Comprendre ».</p>'}
else if(ph==='comprendre'){h+='<h2>Comprendre</h2>';
if(m.html)h+='<div class="sec">'+m.html+'</div>';
if(m.sections.length){h+='<p class="no-print"><button type="button" class="ghost" data-act="all">Tout ouvrir</button></p>';m.sections.forEach(function(s,i){h+='<details class="sc"'+(i===0?' open':'')+'><summary><span class="no">'+(i+1)+'</span> '+E(s[0])+'</summary>'+FMT(s[1])+''+(m.exercices||[]).map(function(x,j){return x.after===i?'<div class="micro"><b>Pour vérifier que c’est clair</b>'+qcard(x,'x'+m.id+'_'+j,{aids:true})+'</div>':''}).join('')+'</details>'})}
if(!m.sections.length&&!m.html)h+='<div class="warn"><b>Module en cours de rédaction.</b> Sources prévues : '+E(m.source)+'</div>'}
else if(ph==='faire'){h+='<h2>Faire</h2><p class="expl">Ici, vous pouvez vous tromper : les coups de pouce sont là pour ça. Chaque réponse est expliquée.</p>';
if(m.decision)h+='<div class="card sit"><h3>Mise en situation</h3><p>'+E(m.decision)+'</p><p class="expl">Décidez d’abord, puis ouvrez la réponse.</p><details><summary>Voir la réponse</summary><p>'+E(m.answer)+'</p></details></div>';
if(sp.f.length){h+='<h3>Questions guidées ('+sp.f.length+')</h3>';sp.f.forEach(function(x,i){h+=qcard(x,'f'+m.id+'_'+i,{aids:true})})}
if(!m.decision&&!sp.f.length)h+='<p class="expl">Pas d’exercice guidé pour ce module : passez à « Vérifier ».</p>'}
else if(ph==='verifier'){h+='<h2>Vérifier</h2>';
if(!sp.v.length)h+='<p class="expl">Pas de question de contrôle pour ce module.</p>';
else{var pv=prog(m.id).verifier;h+='<p class="expl">Sans coup de pouce. Répondez à tout, puis corrigez.'+(pv?' Dernier score enregistré dans ce navigateur : '+pv.s+' / '+pv.n+'.':'')+'</p><form id="fv" onsubmit="return false">';sp.v.forEach(function(x,i){h+=qcard(x,'v'+m.id+'_'+i,{noBtn:true})});h+='<p><button type="button" data-act="fin">Corriger mes réponses</button> <button type="button" class="ghost" data-act="retry">Recommencer</button></p></form><div id="vres" aria-live="polite"></div>'}}
else{h+='<h2>Retenir</h2><div class="goal"><b>Objectif :</b> '+E(m.goal)+'</div>';
if(m.check&&m.check.length)h+='<h3>Avant d’agir</h3><ul class="chk">'+m.check.map(function(c,i){var k='c'+m.id+'_'+i,on=sto(k);return '<li><label><input type="checkbox" data-k="'+k+'"'+(on?' checked':'')+'> '+E(c)+'</label></li>'}).join('')+'</ul>';
h+='<p class="expl">Source : '+E(m.source)+'</p><p class="no-print"><a class="btn" href="evaluation.html#m'+m.id+'" style="text-decoration:none;display:inline-block">Évaluer ce module</a> <a class="btn alt" href="animation.html#m'+m.id+'" style="text-decoration:none;display:inline-block;background:#4b5d73">Mode animation</a> <button type="button" class="ghost" onclick="print()">Imprimer le module</button></p>'}
if(nx)h+='<p class="next no-print"><button type="button" data-ph="'+nx[0]+'">Terminer « '+PH[PH.map(function(p){return p[0]}).indexOf(ph)][1]+' » et passer à « '+nx[1]+' » →</button></p>';
else h+='<p class="next no-print"><button type="button" data-ph="fin">Terminer le module ✓</button></p>';
return h}
function railHtml(id,cur){var p=prog(id);return '<nav class="rail no-print" aria-label="Phases du module"><button type="button" class="ph'+(cur==='tout'?' on':'')+'" data-ph="tout"'+(cur==='tout'?' aria-current="step"':'')+'><span class="pn">≡</span>Tout lire</button>'+PH.map(function(x,i){var c=(x[0]===cur?' on':'')+(p[x[0]]?' done':'');return '<button type="button" class="ph'+c+'" data-ph="'+x[0]+'"'+(x[0]===cur?' aria-current="step"':'')+'><span class="pn">'+(p[x[0]]?'✓':(i+1))+'</span>'+x[1]+'</button>'}).join('')+'</nav>'}
function refresh(id){var host=document.querySelector('.studio');if(host&&+host.dataset.m===id){var cur=host.dataset.cur;host.querySelector('.railw').innerHTML=railHtml(id,cur)}}
function go(id,ph,keep){var m=module(id),host=document.querySelector('.studio');if(!host)return;
if(ph==='fin'){mark(id,'retenir');location.hash='#';return}
host.dataset.cur=ph;host.querySelector('.railw').innerHTML=railHtml(id,ph);var pn=host.querySelector('.pan');pn.innerHTML=panel(m,ph);wrapPas(pn);
if(history.replaceState)history.replaceState(null,'','#m'+id+'/'+ph);
(function(){var f=host.querySelector('.rail');if(f&&!keep)f.scrollIntoView({block:'start'})})()}
document.addEventListener('change',function(e){var c=e.target;if(c&&c.dataset&&c.dataset.k)sto(c.dataset.k,c.checked?1:0)});
function mod(id,ph){var m=module(id);if(!m){liste();return}
var ids=A.modules.map(function(x){return x.id}),k=ids.indexOf(m.id),sp=split(m);
var h='<p><a href="#">← Tous les modules</a></p>'+(function(){var v=(m.images||[]).map(vis).filter(Boolean)[0];return v?'<div class="banner"><img src="'+E(v.fichier)+'" alt="'+E(v.titre)+'"></div>':''})()+'<div class="mhead"><div><div class="bigico"><span class="mico">'+ico(MICO[m.id]||'bolt')+'</span><small>MODULE '+m.id+'</small></div><h1>'+E(m.title)+'</h1><p class="lead">'+E(m.goal)+'</p><p>'+statTag(m.statut)+'<span class="stat">'+E(m.scope)+'</span></p></div><aside class="fiche"><h2>En bref</h2><dl><dt>Niveaux</dt><dd>'+E(m.niveaux.join(', '))+'</dd><dt>Lecture</dt><dd>≈ '+minutes(m)+' min</dd><dt>Questions</dt><dd>'+m.questions.length+' ('+sp.f.length+' guidées, '+sp.v.length+' de contrôle)</dd><dt>Visuels</dt><dd>'+((m.images||[]).length+(m.figures||[]).length)+'</dd></dl></aside></div>';
h+='<div class="studio" data-m="'+m.id+'" data-cur=""><div class="railw"></div><div class="pan"></div></div>';
h+='<div class="pager">'+(k>0?'<a href="#m'+ids[k-1]+'">← '+E(A.modules[k-1].title)+'</a>':'<span></span>')+(k<ids.length-1?'<a href="#m'+ids[k+1]+'">'+E(A.modules[k+1].title)+' →</a>':'')+'</div>';
out.innerHTML=h;scrollTo(0,0);var first=(ph&&(ph==='tout'||PH.some(function(p){return p[0]===ph})))?ph:'tout';go(m.id,first,true)}
function route(){var m=/^#m(\d+)(?:\/(\w+))?/.exec(location.hash);if(m)mod(+m[1],m[2]);else liste()}
addEventListener('hashchange',route);route();
