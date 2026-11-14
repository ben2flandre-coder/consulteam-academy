import json, re, hashlib, os, html
R='/home/claude/work/a260e2a'
acad=json.load(open('/tmp/academy.json',encoding='utf-8'))
prompts=json.load(open('/tmp/outputs/prompts/prompts-visuels-A260E2A.json',encoding='utf-8'))
# ---------- données ----------
mods=[]
LV={1:["TC"],2:["TC"],3:["TC"],4:["B0","H0","H0V"],5:["BS"],6:["BS","BE"],7:["BE"],8:["TC"]}
for m in acad['modules']:
    qs=[q for q in acad['questions'] if q['module']==m['id']]
    mods.append(dict(id=m['id'],title=m['title'],scope=m['scope'],niveaux=LV[m['id']],statut="repris",
        goal=m['goal'],scenario=m['scenario'],sections=m['sections'],decision=m['decision'],answer=m['answer'],check=m['check'],
        questions=[dict(id=q['id'],q=q['q'],options=q['options'],correct=q['correct'],why=q['why']) for q in qs],
        source="Support A2604MA (repris sans modification de texte ; relecture NF C 18-510 A1/A2 à faire)"))
mods[7]['statut']="à compléter"
mods[7]['note']="Cadre SST (protéger, examiner, faire alerter, secourir) à compléter à partir de l'ED 7000, du guide des données techniques SST et de l'ED 4085, à lire à la source."
NEW=[
(9,"Travaux hors tension B1 · B1V · B2 · B2V",["B1","B1V","B2","B2V"],"Préparer, exécuter, diriger et surveiller des travaux électriques hors tension en basse tension.","Programme Consul Team HE-BTHT-INI-21 : travaux BT B1/B1V et B2/B2V.","Sources à lire : NF C 18-510 (travaux hors tension), INRS ED 6127 ; support A260BNA pour le socle."),
(10,"Intervention générale BR",["BR"],"Réaliser en sécurité une intervention générale en basse tension dans les limites du symbole BR : entretien, dépannage, recherche de défaut, remplacement, connexion, déconnexion, mesurage, essai, manœuvre, consignation pour son propre compte.","Programme Consul Team : intervention générale BR.","Existant à recaler : séquence BR du support A260BNA ; NF C 18-510 A1/A2 à lire."),
(11,"Consignation BC",["BC"],"Appliquer la procédure de consignation et de déconsignation en basse tension.","Programme Consul Team : consignation BC.","Existant à recaler : séquence BC du support A260BNA ; INRS ED 6109 ; NF C 18-510 A1/A2."),
(12,"Travaux hors tension H1 · H1V · H2 · H2V",["H1","H1V","H2","H2V"],"Préparer, exécuter, diriger et surveiller des travaux hors tension dans le domaine HT sélectionné.","Programme Consul Team : travaux HT H1/H1V et H2/H2V.","À créer. Domaine HTA/HTB non précisé : hypothèse de travail, ne rien afficher sans confirmation par le formateur. Source à lire : NF C 18-510."),
(13,"Consignation HC",["HC"],"Appliquer la procédure de consignation et de déconsignation dans le domaine HT concerné.","Programme Consul Team : consignation HC.","À créer. Sources à lire : NF C 18-510, INRS ED 6109."),
(14,"Opération spécifique HE Manœuvre",["HE"],"Réaliser des manœuvres d'exploitation ou de consignation sur ordre dans le domaine HT concerné.","Programme Consul Team : HE Manœuvre.","À créer. Source à lire : NF C 18-510."),
(15,"BE : mesurage · vérification · essai",["BE"],"Réaliser un mesurage, une vérification ou un essai dans les limites des attributs sélectionnés.","Programme Consul Team : opérations spécifiques BE.","À créer. Sources à lire : NF C 18-510 ; notices des appareils utilisés en formation."),
(16,"Travaux pratiques individualisés et évaluations",["Tous"],"Mettre en situation chaque participant selon ses fonctions, symboles et attributs, puis évaluer (théorique et pratique) et formuler l'avis après formation.","Programme Consul Team : TP individualisés (7 h) et évaluations.","Grilles d'observation par symbole à créer ; TP-A à TP-D du support A2604MA à reprendre."),
(17,"Spécificités métier : sécurité incendie (optionnel)",["SSI"],"Situer les opérations propres aux installations de systèmes de sécurité incendie (centrale, alimentation, batteries, boucles, travail en hauteur) dans le cadre de l'habilitation.","Hypothèse de travail pour les stagiaires d'ADI sécurité ; aucune liste de symboles fournie par le client.","À créer à partir de cas fournis par le formateur ; aucune valeur technique sans source."),
]
for i,t,nv,g,sc,so in NEW:
    mods.append(dict(id=i,title=t,scope=", ".join(nv),niveaux=nv,statut="à rédiger",goal=g,scenario="",sections=[],decision="",answer="",check=[],questions=[],source=so,note=sc))
PZ=json.load(open('/tmp/panzani_import.json',encoding='utf-8'))
NOTE_PZ="Repris de la plateforme A260BNA (Panzani), recalé par ses auteurs sur l'arrêté du 9 juillet 2013 et les INRS ED 6127 et ED 6109. La NF C 18-510 n'a pas été lue : à confirmer à la source avant publication."
byid={m['id']:m for m in mods}
for mid in ('10','11'):
    m=byid[int(mid)];z=PZ[mid];m.update(statut="repris",html=z['html'],figures=z['figures'],note=NOTE_PZ,source="Support A260BNA, séquence "+z['titre'])
mods.append(dict(id=18,title="Zones d'environnement et voisinage (H0V · B2V)",scope="H0V, B2V",niveaux=["H0V","B2V"],statut="repris",goal="Situer les zones d'environnement et appliquer l'ordre de protection en voisinage.",scenario="",sections=[],decision="",answer="",check=[],questions=[],html=PZ['18']['html'],figures=PZ['18']['figures'],note=NOTE_PZ,source="Support A260BNA, séquence "+PZ['18']['titre']))
byid={m['id']:m for m in mods}
for q in PZ['questions']:
    byid[q['module']]['questions'].append(dict(id=q['id'],type=q['type'],q=q['q'],options=q['options'],correct=q['correct'],why=q['why']))
import sys; sys.path.insert(0,'/home/claude/work/src')
import modules_tb, sources_new
LEG=" Repères : [S1…S29] = source du registre ; [C] = calcul prouvé par script ; [R] = principe de raisonnement à valider par le formateur."
for m in modules_tb.MODULES:
    m=dict(m); m['note']=m['note']+LEG; mods.append(m)
SCHEMAS=[("F1-facade-tableau.svg","Vue de face d'un tableau de répartition",19),("F2-coupe-disjoncteur.svg","Coupe d'un disjoncteur modulaire",19),("F3-principe-differentiel.svg","Principe d'un interrupteur différentiel",19),("F4-coupe-contacteur.svg","Coupe d'un contacteur",19),("F5-coupe-rail-peigne.svg","Coupe d'une rangée : rail, peigne, raccordements",21),("F6-equilibrage-avant-apres.svg","Équilibrage : avant et après (exemple chiffré)",20),("F7-remplacement-appareil.svg","Remplacer un appareil : les étapes",21),("F8-installation-appareil.svg","Installer un nouvel appareil : les étapes",22)]
for m in mods:
    for q in m['questions']: q.setdefault('type','s')
for m in mods:
    m.setdefault('html','');m.setdefault('figures',[]);m.setdefault('exercices',[])
import csv
SUIVI={x['id']:x for x in csv.DictReader(open('/tmp/up/suivi-visuels-A260E2A.csv',encoding='utf-8-sig'),delimiter=';')}
vis=[dict(id=i['id'],titre=i['titre'],module=i['module'],format=i['format'],legende=i['legende'],controle=i['controle_technique'],fichier=('images/ia/'+i['id']+'.webp'),statut=SUIVI.get(i['id'],{}).get('statut','image à venir'),relecteur=SUIVI.get(i['id'],{}).get('relecteur','')) for i in prompts['images']]
data=dict(session="A260E2A",titre="Habilitation électrique : formation initiale",dates="14, 15 et 16 décembre 2026",lieu="Consul Team Security, La Seyne-sur-Mer",modules=mods,videos=acad['videos'],tps=acad['tps'],sources=acad['sources'],visuels=vis,schemas=[dict(fichier='images/schemas/'+f,titre=ti,module=mo) for f,ti,mo in SCHEMAS],registre=sources_new.SOURCES)
open(f'{R}/data/content.js','w',encoding='utf-8').write("window.A="+json.dumps(data,ensure_ascii=False)+";")
json.dump({"destinataire":"ben2flandre@gmail.com","endpoint":""},open(f'{R}/assets/config.json','w'))
# ---------- CSS ----------
css=r""":root{--n:#102c53;--b:#0b68ae;--y:#f6b63d;--i:#16273d;--m:#53657a;--l:#cbd5e1;--bg:#f3f5f8;--w:#fff;--ok:#16794a;--ko:#b3261e;--r:12px}
body.nuit{--bg:#0d1722;--w:#15253a;--i:#e7eef6;--m:#9fb2c8;--l:#2c4058;--b:#7cc0f5}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--i);font:16px/1.65 system-ui,-apple-system,"Segoe UI",sans-serif}
img{max-width:100%;height:auto}a{color:var(--b)}
header.top{background:var(--n);color:#fff;position:sticky;top:0;z-index:5}
.bar{max-width:1100px;margin:auto;display:flex;flex-wrap:wrap;gap:6px 14px;align-items:center;padding:8px 14px}
.brand{font-weight:700;color:#fff;text-decoration:none;display:flex;align-items:center;gap:8px;min-height:44px}
.brand i{width:28px;height:28px;border-radius:6px;background:var(--y);display:inline-block}
nav{display:flex;flex-wrap:wrap;gap:2px 4px;margin-left:auto}
nav a,nav button{color:#fff;text-decoration:none;padding:10px 12px;min-height:44px;border-radius:8px;background:none;border:0;font:inherit;cursor:pointer;display:inline-flex;align-items:center}
nav a:hover,nav a[aria-current],nav button:hover{background:rgba(255,255,255,.15)}
main{max-width:1100px;margin:auto;padding:18px 14px 60px}
h1{font-size:clamp(1.5rem,5vw,2.2rem);line-height:1.2;color:var(--n);margin:.2em 0}body.nuit h1,body.nuit h2{color:var(--i)}
h2{color:var(--n);font-size:1.3rem;margin-top:1.6em}
.card{background:var(--w);border:1px solid var(--l);border-radius:var(--r);padding:16px;margin:12px 0}
.grid{display:grid;gap:12px;grid-template-columns:repeat(auto-fill,minmax(min(100%,300px),1fr))}
.btn,button.btn{display:inline-flex;align-items:center;justify-content:center;min-height:44px;padding:10px 16px;border-radius:10px;border:1px solid var(--n);background:var(--n);color:#fff;font:600 15px/1.3 inherit;text-decoration:none;cursor:pointer}
.btn.sec{background:var(--w);color:var(--n)}body.nuit .btn.sec{color:var(--i);border-color:var(--l)}
.tag{display:inline-block;font-size:.78rem;font-weight:700;padding:2px 9px;border-radius:99px;background:#e6edf5;color:var(--n);margin:0 4px 4px 0}
.tag.rep{background:#d9f1e4;color:#0f5c37}.tag.cpl{background:#fff1cc;color:#6b4a00}.tag.red{background:#e6edf5}
body.nuit .tag{background:#233b55;color:#e7eef6}
.opt{display:flex;align-items:flex-start;gap:10px;padding:12px;border:1px solid var(--l);border-radius:10px;margin:8px 0;min-height:44px;cursor:pointer;background:var(--w)}
.opt input{width:22px;height:22px;margin-top:2px;flex:none}
.opt.good{border-color:var(--ok);background:rgba(22,121,74,.12)}.opt.bad{border-color:var(--ko);background:rgba(179,38,30,.1)}
.note{border-left:5px solid var(--y);background:rgba(246,182,61,.14);padding:10px 14px;border-radius:0 10px 10px 0}
.small{font-size:.9rem;color:var(--m)}:focus-visible{outline:3px solid var(--y);outline-offset:2px}
.skip{position:absolute;left:-999px}.skip:focus{left:8px;top:8px;background:#fff;color:#000;padding:8px;z-index:9}
.fig{margin:0}.fig img{border-radius:10px;display:block;width:100%}.ph{aspect-ratio:3/2;display:grid;place-items:center;background:repeating-linear-gradient(45deg,#e6edf5,#e6edf5 10px,#f3f5f8 10px,#f3f5f8 20px);border-radius:10px;color:var(--m);font-size:.85rem;text-align:center;padding:8px}
body.nuit .ph{background:#1b2d44}
.deck{position:fixed;inset:0;background:var(--n);color:#fff;display:flex;flex-direction:column;z-index:20}
.deck .slide{flex:1;display:flex;flex-direction:column;justify-content:center;padding:4vw;max-width:1100px;margin:auto;width:100%;overflow:auto}
.deck h1{color:#fff;font-size:clamp(1.6rem,5.5vw,3.2rem)}.deck p{font-size:clamp(1.1rem,3.2vw,1.9rem);line-height:1.5}
.deck .ctl{display:flex;gap:8px;padding:10px;justify-content:center;flex-wrap:wrap;background:rgba(0,0,0,.25)}
.deck .ctl button,.deck .ctl a{min-width:56px;min-height:48px;border-radius:10px;border:1px solid #fff;background:none;color:#fff;font:600 16px inherit;cursor:pointer;display:inline-flex;align-items:center;justify-content:center;text-decoration:none;padding:0 14px}
td a{display:inline-block;padding:11px 0}
table{border-collapse:collapse;width:100%}th,td{border:1px solid var(--l);padding:8px;text-align:left;vertical-align:top}
.scroll{overflow-x:auto}
@media (max-width:600px){main{padding:12px 10px 50px}.card{padding:12px}}
@media print{header.top,.deck .ctl{display:none}}
@media (prefers-reduced-motion:reduce){*{scroll-behavior:auto!important;transition:none!important}}
"""
open(f'{R}/assets/style.css','w').write(css)
# ---------- JS commun ----------
js=r"""'use strict';
(function(){
var A=window.A,CFG={destinataire:'',endpoint:''};
function E(s){return String(s==null?'':s).replace(/[&<>"']/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})}
window.E=E;
try{if(localStorage.getItem('he.nuit')==='1')document.body.classList.add('nuit')}catch(e){}
var pages=[['index.html','Accueil'],['parcours.html','Parcours'],['evaluation.html','Évaluation'],['animation.html','Animation'],['mediatheque.html','Médiathèque'],['registre.html','Sources'],['formateur.html','Formateur']];
var here=location.pathname.split('/').pop()||'index.html';
var h='<a class="skip" href="#main">Aller au contenu</a><header class="top"><div class="bar"><a class="brand" href="index.html"><img src="images/logos/logo-consulteam-groupe.png" alt="Consul Team" width="150" height="31" style="background:#fff;border-radius:6px;padding:4px 8px;height:34px;width:auto"><span>Habilitation électrique</span></a><nav aria-label="Navigation">';
pages.forEach(function(p){h+='<a href="'+p[0]+'"'+(here===p[0]?' aria-current="page"':'')+'>'+p[1]+'</a>'});
h+='<button type="button" id="nuit" aria-pressed="false">Mode nuit</button></nav></div></header>';
document.body.insertAdjacentHTML('afterbegin',h);
var b=document.getElementById('nuit');
function sync(){b.setAttribute('aria-pressed',document.body.classList.contains('nuit'))}sync();
b.onclick=function(){document.body.classList.toggle('nuit');try{localStorage.setItem('he.nuit',document.body.classList.contains('nuit')?'1':'0')}catch(e){}sync()};
window.module=function(id){return A.modules.filter(function(m){return m.id==id})[0]};
window.statTag=function(s){return '<span class="tag '+(s==='repris'?'rep':s==='à compléter'?'cpl':s==='nouveau'?'cpl':'red')+'">'+(s==='repris'?'Contenu repris':s==='à compléter'?'À compléter':s==='nouveau'?'Nouveau, à valider':'En préparation')+'</span>'};
window.shuffle=function(a){a=a.slice();for(var i=a.length-1;i>0;i--){var j=Math.floor(Math.random()*(i+1));var t=a[i];a[i]=a[j];a[j]=t}return a};
if('serviceWorker' in navigator&&location.protocol.indexOf('http')===0){navigator.serviceWorker.register('sw.js').catch(function(){})}
fetch('assets/config.json').then(function(r){return r.json()}).then(function(c){CFG=c;window.CFG=c}).catch(function(){});
window.CFG=CFG;
})();
"""
open(f'{R}/assets/app.js','w').write(js)
# ---------- pages ----------
def page(name,title,body,extra=''):
    s=f'''<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><title>{title} · Consul Team</title><meta name="theme-color" content="#102c53"><link rel="manifest" href="manifest.webmanifest"><link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='6' fill='%23102c53'/%3E%3Cpath d='M18 3L8 18h7l-1 11 11-17h-8z' fill='%23f6b63d'/%3E%3C/svg%3E"><link rel="stylesheet" href="assets/style.css"></head><body>
<main id="main">{body}</main><script src="data/content.js"></script><script src="assets/app.js"></script>{extra}</body></html>'''
    open(f'{R}/{name}','w',encoding='utf-8').write(s)
page('index.html','Accueil','''<h1>Habilitation électrique : formation initiale</h1>
<p class="small" id="meta"></p>
<div class="card"><p>Support de la formation animée en présentiel par le formateur, avec le même contenu pour le suivi à distance. Il s'utilise sur ordinateur, tablette et smartphone, y compris hors connexion une fois chargé.</p>
<p class="note">Lire ce support et réussir les exercices ne valent pas habilitation. L'employeur délivre le titre pour les opérations qu'il confie.</p>
<p><a class="btn" href="parcours.html">Ouvrir le parcours</a> <a class="btn sec" href="evaluation.html">M'évaluer</a></p></div>
<h2>Les niveaux</h2><div class="grid" id="niv"></div>''','''<script>
document.getElementById('meta').textContent=A.dates+' · '+A.lieu;
var n={};A.modules.forEach(function(m){m.niveaux.forEach(function(x){(n[x]=n[x]||[]).push(m)})});
var h='';Object.keys(n).forEach(function(k){h+='<a class="card" style="text-decoration:none;color:inherit" href="parcours.html#niv-'+encodeURIComponent(k)+'"><strong>'+E(k)+'</strong><br><span class="small">'+n[k].length+' module(s)</span></a>'});
document.getElementById('niv').innerHTML=h;</script>''')
page('parcours.html','Parcours','''<h1>Parcours</h1><p class="small">Tous les niveaux sont accessibles. Choisir un module, ou filtrer par niveau.</p>
<p><label for="f">Niveau : </label><select id="f" style="min-height:44px;font:inherit"></select></p><div id="out"></div>''','''<script>
var f=document.getElementById('f'),out=document.getElementById('out');
var lv=['Tous'];A.modules.forEach(function(m){m.niveaux.forEach(function(x){if(lv.indexOf(x)<0)lv.push(x)})});
f.innerHTML=lv.map(function(x){return '<option>'+E(x)+'</option>'}).join('');
function liste(){var v=f.value;var h='<div class="grid">';A.modules.filter(function(m){return v==='Tous'||m.niveaux.indexOf(v)>=0||m.niveaux.indexOf('Tous')>=0||m.niveaux.indexOf('TC')>=0&&false}).forEach(function(m){h+='<a class="card" style="text-decoration:none;color:inherit" href="#m'+m.id+'"><strong>'+m.id+'. '+E(m.title)+'</strong><br>'+statTag(m.statut)+'<span class="tag">'+E(m.scope)+'</span><br><span class="small">'+E(m.goal)+'</span></a>'});out.innerHTML=h+'</div>'}
function mod(id){var m=module(id);if(!m){liste();return}
var h='<p><a href="#">← Tous les modules</a></p><h1>'+m.id+'. '+E(m.title)+'</h1>'+statTag(m.statut)+'<span class="tag">'+E(m.scope)+'</span><div class="card"><strong>Objectif</strong><br>'+E(m.goal)+'</div>';
if(m.note)h+='<p class="note">'+E(m.note)+'</p>';
if(m.scenario)h+='<div class="card"><strong>Situation</strong><br>'+E(m.scenario)+'</div>';
if(m.figures&&m.figures.length)h+='<div class="grid">'+m.figures.map(function(f){return '<figure class="card fig"><img src="'+E(f[0])+'" alt="'+E(f[1])+'" loading="lazy"><figcaption class="small">'+E(f[1])+(/[.]svg$/.test(f[0])?' <a href="'+E(f[0])+'" target="_blank" rel="noopener" style="display:inline-block;padding:11px 0">Ouvrir en grand (zoom)</a>':'')+'</figcaption></figure>'}).join('')+'</div>';
if(m.html)h+='<div class="card">'+m.html+'</div>';
m.sections.forEach(function(s,i){h+='<h2>'+E(s[0])+'</h2><p>'+E(s[1])+'</p>';(m.exercices||[]).forEach(function(x,k){if(x.after===i)h+=exo(x,m.id+'_'+k)})});
if(m.decision)h+='<div class="card"><strong>Décision à prendre</strong><br>'+E(m.decision)+'<details><summary style="min-height:44px;display:flex;align-items:center;cursor:pointer">Voir la réponse</summary><p>'+E(m.answer)+'</p></details></div>';
if(m.check.length)h+='<div class="card"><strong>Avant d\\'agir</strong><ul>'+m.check.map(function(c){return '<li>'+E(c)+'</li>'}).join('')+'</ul></div>';
h+='<p class="small">Source : '+E(m.source)+'</p>';
h+='<p><a class="btn" href="evaluation.html#m'+m.id+'">Évaluer ce module</a> <a class="btn sec" href="animation.html#m'+m.id+'">Mode animation</a></p>';
out.innerHTML=h;scrollTo(0,0)}
function exo(x,id){var t=x.type,h='<div class="card exo" data-id="'+id+'"><strong>Exercice rapide</strong><p>'+E(x.q)+'</p>';
if(t==='o'){var ord=x.options.map(function(o,i){return i}).sort(function(a,b){return (a*7+3)%5-(b*7+3)%5||a-b});h+='<p class="small">Choisissez la position de chaque élément.</p>';ord.forEach(function(i){h+='<label class="opt"><select data-i="'+i+'" aria-label="Position"><option value="">–</option>'+x.options.map(function(_,p){return '<option value="'+p+'">'+(p+1)+'</option>'}).join('')+'</select> <span>'+E(x.options[i])+'</span></label>'})}
else{x.options.forEach(function(o,i){h+='<label class="opt"><input type="'+(t==='m'?'checkbox':'radio')+'" name="x'+id+'" value="'+i+'"> <span>'+E(o)+'</span></label>'})}
return h+'<p><button class="btn sec" type="button" onclick="exoCheck(this,'+x.after+','+(x.__k||0)+')" data-x="'+id+'">Vérifier</button></p><div class="exo-res" aria-live="polite"></div></div>'}
window.exoCheck=function(btn){var c=btn.closest('.exo'),id=c.dataset.id.split('_'),m=module(+id[0]),x=m.exercices[+id[1]],ok=false;
if(x.type==='o'){var v=[];[].slice.call(c.querySelectorAll('select')).forEach(function(s){v[+s.dataset.i]=s.value===''?-1:+s.value});ok=x.options.every(function(_,i){return v[i]===x.correct.indexOf(i)})}
else{var sel=[].slice.call(c.querySelectorAll('input:checked')).map(function(i){return +i.value}).sort();var cor=[].concat(x.correct).sort();ok=sel.length===cor.length&&sel.every(function(v,i){return v===cor[i]})}
c.querySelector('.exo-res').innerHTML='<p class="'+(ok?'ok':'note')+'"><strong>'+(ok?'Juste.':'À revoir.')+'</strong> '+E(x.why)+'</p>'};
function route(){var m=/^#m(\\d+)/.exec(location.hash);if(m)mod(+m[1]);else liste()}
f.onchange=liste;addEventListener('hashchange',route);route();</script>''')
page('evaluation.html','Évaluation','''<h1>Évaluation</h1><p class="small">Les réponses sont mélangées à chaque essai. Ce QCM est un exercice de formation, il ne remplace pas l'évaluation du formateur.</p><div id="out"></div>''','''<script>
var out=document.getElementById('out');
function choix(){var h='<div class="grid">';A.modules.forEach(function(m){h+='<div class="card"><strong>'+m.id+'. '+E(m.title)+'</strong><br><span class="small">'+m.questions.length+' question(s)</span><br>'+(m.questions.length?'<a class="btn" href="#m'+m.id+'">Commencer</a>':'<span class="small">Banque de questions à créer</span>')+'</div>'});
h+='</div><p><a class="btn sec" href="#all">Tout le QCM ('+A.modules.reduce(function(s,m){return s+m.questions.length},0)+' questions)</a></p>';out.innerHTML=h}
function quiz(ids){var qs=[];A.modules.forEach(function(m){if(ids==='all'||m.id==ids)m.questions.forEach(function(q){qs.push(q)})});
qs=shuffle(qs).map(function(q){var t=q.type||'s';var o=q.options.map(function(x,i){return{t:x,i:i,ok:t==='s'?i===q.correct:t==='m'?q.correct.indexOf(i)>=0:false}});return{id:q.id,t:t,q:q.q,why:q.why,c:q.correct,o:shuffle(o),n:o.length}});
var h='<p><a href="#">← Retour</a></p><form id="fm">';
qs.forEach(function(q,i){h+='<fieldset class="card"><legend><strong>'+(i+1)+'. '+E(q.q)+'</strong></legend>';
if(q.t==='o'){h+='<p class="small">Attribuez à chaque étape son rang (1 = première).</p>';q.o.forEach(function(o,j){h+='<label class="opt"><select name="q'+i+'_'+j+'" style="min-height:44px;font:inherit"><option value="">–</option>'+q.o.map(function(x,k){return '<option value="'+k+'">'+(k+1)+'</option>'}).join('')+'</select><span>'+E(o.t)+'</span></label>'})}
else{if(q.t==='m')h+='<p class="small">Plusieurs réponses possibles.</p>';q.o.forEach(function(o,j){h+='<label class="opt"><input type="'+(q.t==='m'?'checkbox':'radio')+'" name="q'+i+'" value="'+j+'"><span>'+E(o.t)+'</span></label>'})}
h+='<p class="small why" hidden>'+E(q.why)+'</p></fieldset>'});
h+='<button class="btn" type="submit">Corriger</button></form><div id="res" class="card" hidden></div>';out.innerHTML=h;
document.getElementById('fm').onsubmit=function(e){e.preventDefault();var s=0,ans=0;
qs.forEach(function(q,i){var fs=document.querySelectorAll('fieldset')[i],ok=false,given=false;
if(q.t==='o'){var all=true;q.o.forEach(function(o,j){var v=fs.querySelector('select[name=q'+i+'_'+j+']').value;if(v!=='')given=true;else all=false;if(v===''||+v!==o.i)all=false});ok=all;fs.querySelectorAll('.opt').forEach(function(l,j){l.classList.add(+fs.querySelector('select[name=q'+i+'_'+j+']').value===q.o[j].i&&fs.querySelector('select[name=q'+i+'_'+j+']').value!==''?'good':'bad')})}
else{var lab=fs.querySelectorAll('.opt'),sel=fs.querySelectorAll('input:checked');given=sel.length>0;var picked=[];sel.forEach(function(x){picked.push(+x.value)});
ok=picked.length>0&&q.o.every(function(o,j){return o.ok===(picked.indexOf(j)>=0)});q.o.forEach(function(o,j){if(o.ok)lab[j].classList.add('good');else if(picked.indexOf(j)>=0)lab[j].classList.add('bad')})}
if(given)ans++;if(ok)s++;fs.querySelector('.why').hidden=false});
var r=document.getElementById('res');r.hidden=false;r.innerHTML='<strong>Score : '+s+' / '+qs.length+'</strong> ('+ans+' question(s) traitée(s))<p class="small">Résultat conservé uniquement si vous l\\'envoyez.</p><a class="btn" href="mailto:'+encodeURIComponent((window.CFG&&CFG.destinataire)||'')+'?subject='+encodeURIComponent('Résultat QCM A260E2A')+'&body='+encodeURIComponent('Score '+s+'/'+qs.length+' - module '+ids)+'">Envoyer mon résultat</a>';r.scrollIntoView()}}
function route(){var h=location.hash;if(h==='#all')quiz('all');else if(/^#m\\d+/.test(h))quiz(+h.slice(2));else choix()}
addEventListener('hashchange',route);route();</script>''')
page('animation.html','Animation','''<div class="deck" id="deck" role="region" aria-label="Mode animation"><div class="slide" id="sl" aria-live="polite"></div><div class="ctl"><button id="pr" aria-label="Précédent">←</button><span id="pg" style="align-self:center"></span><button id="nx" aria-label="Suivant">→</button><select id="ms" aria-label="Module" style="min-height:48px;font:inherit"></select><a href="parcours.html">Quitter</a></div></div>''','''<script>
var sl=document.getElementById('sl'),ms=document.getElementById('ms'),pg=document.getElementById('pg'),L=[],k=0;
ms.innerHTML=A.modules.filter(function(m){return m.statut!=='à rédiger'}).map(function(m){return '<option value="'+m.id+'">'+m.id+'. '+E(m.title)+'</option>'}).join('');
function build(id){var m=module(id);L=[{t:m.title,p:m.goal}];if(m.scenario)L.push({t:'Situation',p:m.scenario});m.sections.forEach(function(s){L.push({t:s[0],p:s[1]})});if(m.decision)L.push({t:'Décision à prendre',p:m.decision});k=0;show()}
function show(){var s=L[k];sl.innerHTML='<h1>'+E(s.t)+'</h1><p>'+E(s.p)+'</p>';pg.textContent=(k+1)+' / '+L.length}
function go(d){k=Math.max(0,Math.min(L.length-1,k+d));show()}
document.getElementById('pr').onclick=function(){go(-1)};document.getElementById('nx').onclick=function(){go(1)};
ms.onchange=function(){location.hash='m'+ms.value;build(ms.value)};
addEventListener('keydown',function(e){if(e.key==='ArrowRight'||e.key===' ')go(1);if(e.key==='ArrowLeft')go(-1)});
var x0=null;sl.addEventListener('touchstart',function(e){x0=e.touches[0].clientX},{passive:true});sl.addEventListener('touchend',function(e){if(x0==null)return;var d=e.changedTouches[0].clientX-x0;if(Math.abs(d)>50)go(d<0?1:-1);x0=null});
var m=/^#m(\\d+)/.exec(location.hash);var id=m&&module(+m[1])&&module(+m[1]).statut!=='à rédiger'?+m[1]:A.modules[0].id;ms.value=id;build(id);</script>''')
page('mediatheque.html','Médiathèque','''<h1>Médiathèque</h1><h2>Schémas et coupes légendés</h2><p class="small">Dessins Consul Team (SVG), schémas de principe non à l'échelle. Chaque schéma indique ses sources en pied.</p><div class="grid" id="sc"></div><h2>Visuels générés par IA</h2><p class="small">Les images générées par IA sont signalées. Un emplacement grisé attend son image.</p><div class="grid" id="g"></div>''','''<script>
document.getElementById('sc').innerHTML=A.schemas.map(function(s){return '<figure class="card fig"><img src="'+E(s.fichier)+'" alt="'+E(s.titre)+'" loading="lazy"><figcaption class="small"><strong>'+E(s.titre)+'</strong><br>Module '+s.module+' · <a href="'+E(s.fichier)+'">ouvrir en grand</a></figcaption></figure>'}).join('');
var g=document.getElementById('g');
g.innerHTML=A.visuels.map(function(v){return '<figure class="card fig"><div class="ph" data-f="'+E(v.fichier)+'">'+E(v.id)+' · image à venir</div><figcaption class="small"><strong>'+E(v.titre)+'</strong><br>'+E(v.legende)+'<br>Image générée par IA · contrôle '+E(v.controle)+(v.relecteur?' · '+E(v.relecteur)+' · '+E(v.statut):' · image à venir')+'</figcaption></figure>'}).join('');
document.querySelectorAll('.ph').forEach(function(d){var im=new Image();im.loading='lazy';im.alt=d.textContent.split(' · ')[0]+' : '+d.parentNode.querySelector('strong').textContent;im.onload=function(){d.replaceWith(im)};im.src=d.dataset.f});</script>''')
page('registre.html','Sources','''<h1>Registre des sources</h1><p class="small">Aucune règle chiffrée n'est publiée sans source lue. Le texte de la NF C 18-510 n'a pas été lu dans les supports : à confirmer avant publication.</p><div class="scroll"><table id="t"><thead><tr><th>Source</th><th>Usage</th></tr></thead><tbody></tbody></table></div><h2>Sources des modules 19 à 22 (appareillage d'un tableau)</h2><p class="small">« lu » : page lue en entier ; « extrait » : seul un extrait a pu être lu. Les limites de chaque source sont indiquées.</p><div class="scroll"><table id="t2"><thead><tr><th>N°</th><th>Source</th><th>Accès</th><th>Fiabilité</th><th>Usage</th><th>Limites</th></tr></thead><tbody></tbody></table></div>''','''<script>
document.querySelector('#t tbody').innerHTML=A.sources.map(function(s){return '<tr><td><a href="'+E(s[1])+'" rel="noopener">'+E(s[0])+'</a></td><td>'+E(s[2])+'</td></tr>'}).join('')+'<tr><td>NF C 18-510 (2012, A1 2020, A2 2023)</td><td>À lire à la source avant publication.</td></tr>';document.getElementById('t2').querySelector('tbody').innerHTML=A.registre.map(function(s){return '<tr><td>'+s.id+'</td><td><a href="'+E(s.url)+'" rel="noopener">'+E(s.titre)+'</a></td><td>'+E(s.acces)+'</td><td>'+E(s.fiabilite)+'</td><td>'+E(s.usage)+'</td><td>'+E(s.limites)+'</td></tr>'}).join('');</script>''')
page('formateur.html','Formateur','''<h1>Espace formateur</h1><p class="note">Contenu chiffré non généré dans ce squelette. Le corrigé et les grilles d'observation seront chiffrés (AES-GCM) avec le mot de passe du formateur, comme sur les autres plateformes.</p><p class="small">Contenus prévus : corrigés, grilles d'observation par symbole, avis après formation, émargement par demi-journée, compte rendu jour par jour.</p>''')
open(f'{R}/manifest.webmanifest','w').write(json.dumps({"name":"Habilitation électrique A260E2A","short_name":"Habilitation","start_url":"index.html","display":"standalone","background_color":"#102c53","theme_color":"#102c53","lang":"fr","icons":[]}))
files=['index.html','parcours.html','evaluation.html','animation.html','mediatheque.html','registre.html','formateur.html','assets/style.css','assets/app.js','assets/config.json','data/content.js','manifest.webmanifest']
import glob
files+=sorted(os.path.relpath(p,R) for p in glob.glob(R+'/images/**/*',recursive=True) if os.path.isfile(p))
ver=hashlib.sha256(b''.join(open(f'{R}/{f}','rb').read() for f in files)).hexdigest()[:10]
open(f'{R}/sw.js','w').write("var V='a260e2a-%s',F=%s;self.addEventListener('install',function(e){e.waitUntil(caches.open(V).then(function(c){return c.addAll(F)}).then(function(){return self.skipWaiting()}))});self.addEventListener('activate',function(e){e.waitUntil(caches.keys().then(function(k){return Promise.all(k.filter(function(x){return x!==V}).map(function(x){return caches.delete(x)}))}).then(function(){return self.clients.claim()}))});self.addEventListener('fetch',function(e){if(e.request.method!=='GET')return;e.respondWith(caches.match(e.request).then(function(r){return r||fetch(e.request).then(function(n){var c=n.clone();caches.open(V).then(function(x){x.put(e.request,c)});return n}).catch(function(){return r})}))});"%(ver,json.dumps(files+['sw.js'][:0])))
print(ver,len(mods),sum(len(m['questions']) for m in mods))
