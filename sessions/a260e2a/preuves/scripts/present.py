
def fmt_sec(x):
    out=[];ol=[]
    for l in str(x).split('\n'):
        mm=re.match(r'^\d+\)\s+(.*)$',l)
        if mm: ol.append('<li>'+esc(mm.group(1))+'</li>')
        else:
            if ol: out.append('<ol>'+''.join(ol)+'</ol>'); ol=[]
            if l.strip(): out.append('<p>'+esc(l)+'</p>')
    if ol: out.append('<ol>'+''.join(ol)+'</ol>')
    return ''.join(out)
# Couche de présentation : charte Panzani (A260BNA), pages statiques + rendu JS des modules.
import json, os, html as H
IMGMAP={1:['TC01','TC09','PC01'],2:['TC02','TC03'],4:['NE01','NE02','NE03','TC08','PC03'],6:['TC04','TC05','TC06','TC07','PC02'],16:['PR01','PR02'],17:['SI01','SI02','SI03','SI04','SI05','SI06'],19:['TB01','TB02','TB03','TB04','TB05','TB09'],20:['TB08'],21:['TB06'],22:['TB07']}
IMGMAP.update({19:IMGMAP[19]+['CPA','CPB','CPC'],20:IMGMAP[20]+['CPE'],22:IMGMAP[22]+['CPD']})
CODE={'BS':5,'B1B2':9,'BR':10,'BC':11,'H1H2':12,'HC':13,'BEX':14,'SST':8}
used=set(i for v in IMGMAP.values() for i in v)
for v in vis:
    if v['module'] in CODE and v['id'] not in used:
        IMGMAP.setdefault(CODE[v['module']],[]).append(v['id']);used.add(v['id'])
IMGMAP[15]=list(IMGMAP.get(14,[]))
for m in data['modules']:
    m['images']=IMGMAP.get(m['id'],[])
orph=[v['id'] for v in vis if v['id'] not in used]
print('images non rattachées:',orph)
open(f'{R}/data/content.js','w',encoding='utf-8').write("window.A="+json.dumps(data,ensure_ascii=False)+";")
nvis=len(vis); nq=sum(len(m['questions']) for m in mods)
css=open('/home/claude/work/tpl/style_pz.css',encoding='utf-8').read()
def _strip_dark(t):
    key='@media(prefers-color-scheme:dark){'; out=''; i=0
    while True:
        j=t.find(key,i)
        if j<0: return out+t[i:]
        out+=t[i:j]; d=1; k=j+len(key)
        while d: d+= (t[k]=='{')-(t[k]=='}'); k+=1
        i=k
css=_strip_dark(css)
FONTS='''@font-face{font-family:"Source Serif 4";font-weight:400;font-style:normal;src:url(fonts/source-serif-4-latin-400-normal.woff2) format("woff2");font-display:swap}
@font-face{font-family:Inter;font-weight:400;src:url(fonts/inter-latin-400-normal.woff2) format("woff2");font-display:swap}
@font-face{font-family:Inter;font-weight:700;src:url(fonts/inter-latin-700-normal.woff2) format("woff2");font-display:swap}
'''
import sys as _s0;_s0.path.insert(0,'/home/claude/work/src');import skin as _skin
EXTRA='''
.rail{display:flex;gap:6px;flex-wrap:wrap;position:sticky;top:0;z-index:5;background:var(--bg,#fff);padding:10px 0;border-bottom:3px solid var(--y);margin:18px 0 8px}
.rail .ph{display:flex;align-items:center;align-self:center;height:46px;min-height:0;gap:8px;line-height:1;border:2px solid var(--l);background:var(--w);color:var(--n);border-radius:999px;padding:8px 16px;font:700 16px var(--ff);cursor:pointer}
.rail .ph .pn{display:inline-grid;place-items:center;width:26px;height:26px;border-radius:50%;background:#e6edf5;font-size:14px}
.rail .ph.on{background:var(--n);color:#fff;border-color:var(--n)}.rail .ph.on .pn{background:var(--y);color:var(--n)}
.rail .ph.done .pn{background:#d9f1e4;color:#0f5c37}.rail .ph.on.done .pn{background:var(--y);color:var(--n)}
.pan h2{margin-top:.6em}.goal{background:#eaf3fb;border-left:7px solid var(--b);border-radius:10px;padding:12px 18px;margin:14px 0}
.next{margin:28px 0 8px;text-align:right}
.ghost{background:transparent!important;color:var(--n)!important;border:2px solid var(--n)!important}
details.sc{background:var(--w);border:1px solid var(--l);border-left:8px solid var(--b);border-radius:10px;padding:2px 20px;margin:12px 0}
details.sc>summary{cursor:pointer;font:700 19px var(--ff);padding:12px 0;color:var(--n)}details.sc .no{display:inline-grid;place-items:center;width:30px;height:30px;border-radius:50%;background:var(--n);color:#fff;font-size:15px;margin-right:8px}
details.leg summary{cursor:pointer;color:var(--b);font-weight:700}
.micro{background:#fff7e0;border:1px solid #f0d58a;border-radius:10px;padding:8px 16px;margin:12px 0 14px}
.pasbox .pbar{margin:10px 0 4px}.pcard{background:var(--w);border:2px solid var(--b);border-radius:12px;padding:16px 20px;margin:10px 0}
.pcard .pn{color:var(--b);font:800 14px var(--ff);text-transform:uppercase;letter-spacing:.04em}.pcard .pt{font-size:19px;margin:8px 0}
.pdots{display:flex;gap:6px;margin-bottom:10px}.pdots i{flex:1;height:7px;border-radius:4px;background:#d5dfeb}.pdots i.d{background:#2e9d62}.pdots i.c{background:var(--y)}
.qc{margin:14px 0}.qa{display:flex;gap:10px;flex-wrap:wrap;margin-top:10px}.tip{background:#eaf3fb;border-left:6px solid var(--b);border-radius:8px;padding:9px 14px;margin-top:10px}
.opt.out{opacity:.4;text-decoration:line-through}fieldset.q.good{border-color:#2e9d62!important}fieldset.q.bad{border-color:#c0392b!important}
.sit{border-left:7px solid var(--y)}.chk{list-style:none;padding:0}.chk li{padding:6px 0}
.chips{display:flex;gap:8px;flex-wrap:wrap;margin:8px 0 16px}.chip{border:2px solid var(--n);background:var(--w);color:var(--n);border-radius:999px;padding:8px 18px;font:700 16px var(--ff);cursor:pointer}.chip.on{background:var(--n);color:#fff}
.bar{height:12px;border-radius:7px;background:#d5dfeb;overflow:hidden}.bar i,.mini i{display:block;height:100%;background:#2e9d62}.mini{display:block;height:6px;border-radius:4px;background:#d5dfeb;margin-top:10px;overflow:hidden}.av{margin-top:4px}
.card.fini{border-color:#2e9d62}.rn{display:inline-block;background:var(--y);color:var(--n);border-radius:6px;padding:0 9px;font:800 13px var(--ff);margin-right:8px;text-transform:uppercase}
@media print{.pan{display:block!important}.rail,.next,.pbar{display:none!important}details.sc{display:block}details.sc>*{display:block}}


/* A260E2A : modules, parcours, animation */
.stat{display:inline-block;border-radius:5px;padding:0 9px;font:700 14px var(--ff);margin:0 6px 4px 0;background:#e6edf5;color:var(--n)}
.stat.rep{background:#d9f1e4;color:#0f5c37}.stat.cpl{background:#fff1cc;color:#6b4a00}.stat.red{background:#fde9e7;color:#7a1d15}
.mhead{display:grid;grid-template-columns:1.5fr .5fr;gap:28px;align-items:stretch}@media(max-width:820px){.mhead{grid-template-columns:1fr}}
.mhead .fiche{background:var(--n);color:#fff;border-radius:14px;padding:22px 24px;border-left:10px solid var(--y)}.mhead .fiche h2{color:#fff;margin:0 0 14px;font-size:21px}.mhead .fiche h2::before{display:none}.mhead .fiche dl{margin:0;display:grid;grid-template-columns:auto 1fr;gap:8px 16px}.mhead .fiche dt{color:#f6b63d;font:600 15px var(--ff)}.mhead .fiche dd{margin:0}
.pager{display:flex;flex-wrap:wrap;gap:10px;justify-content:space-between;margin:28px 0}.pager a{background:var(--w);border:1px solid var(--l);border-radius:10px;padding:10px 16px;text-decoration:none;font:700 16px var(--ff)}
.sec{background:var(--w);border:1px solid var(--l);border-left:8px solid var(--b);border-radius:10px;padding:6px 22px 14px;margin:18px 0}.sec h2{margin-top:.8em}
.sec p{max-width:none}
.opt{display:flex;align-items:flex-start;gap:10px;padding:8px 10px;border-radius:8px;cursor:pointer}.opt:hover{background:#0b68ae14}.opt input{width:20px;height:20px;margin-top:3px;flex:none}
.opt.good{background:#e3f4ea}.opt.bad{background:#fde9e7}
.q legend{font-weight:700;padding:0 4px}.q{min-width:0}
.deck{position:fixed;inset:0;background:var(--n);color:#fff;display:flex;flex-direction:column;z-index:60}
.deck .slide{flex:1;display:flex;flex-direction:column;justify-content:center;padding:4vw 7vw;overflow:auto}
.deck h1{color:#fff;font-size:clamp(1.8rem,5vw,3.4rem)}.deck p{font-size:clamp(1.2rem,2.8vw,2rem);line-height:1.5;max-width:70ch}
.deck .ctl{display:flex;gap:10px;padding:12px;justify-content:center;flex-wrap:wrap;background:#0b2040;border-top:6px solid transparent;border-image:repeating-linear-gradient(135deg,#f6b63d 0 14px,#102c53 14px 28px) 6}
.deck .ctl button,.deck .ctl a{min-width:56px;min-height:48px;border-radius:10px;border:1px solid #fff;background:none;color:#fff;font:700 16px var(--ff);display:inline-flex;align-items:center;justify-content:center;text-decoration:none;padding:0 14px;cursor:pointer}
.deck .ctl select{width:auto;max-width:60vw;min-height:48px}
.deck .slide{position:relative}.deck .tg{display:inline-block;align-self:flex-start;background:#f3b43f;color:#102c53;font-weight:700;border-radius:999px;padding:2px 12px;margin-bottom:8px;font-size:.8rem}.deck .rv{align-self:flex-start;margin-top:14px;background:#f3b43f;color:#102c53;border:0;border-radius:10px;padding:10px 18px;font-weight:700;font-size:1rem;cursor:pointer}.deck .ans{margin-top:10px;background:rgba(255,255,255,.12);padding:10px 14px;border-radius:10px}.deck .qrbox{position:absolute;right:84px;bottom:12px;display:flex;align-items:center;gap:10px;font-size:.8rem;color:#dbe6f5;background:rgba(11,32,64,.85);padding:6px 8px;border-radius:10px}.deck .qrbox img{height:88px;width:88px;max-height:none;margin:0;border-radius:6px;background:#fff}.deck .slide{padding-bottom:120px}@media(max-width:760px){.deck .qrbox{display:none}.deck .slide{padding-bottom:4vw}}.deck .slide img{max-width:100%;object-fit:contain}.deck .slide img{max-height:40vh;width:auto;border-radius:10px;margin-top:14px;align-self:flex-start}
.ph{aspect-ratio:3/2;display:grid;place-items:center;background:repeating-linear-gradient(45deg,#e6edf5,#e6edf5 10px,#f3f5f8 10px,#f3f5f8 20px);color:var(--m);font-size:14px;text-align:center;padding:8px}
.gal figure.ia details{font-size:13px;margin-top:6px}
.logoband{display:inline-block;background:#102c53;border-radius:8px;padding:8px 14px}
.tbl2{width:100%}
.fab{position:fixed;right:16px;bottom:16px;display:flex;flex-direction:column;gap:10px;z-index:80}.fab a,.fab button{width:48px;height:48px;border-radius:50%;border:2px solid #f6b63d;background:#102c53;color:#fff;font:700 22px/1 system-ui,sans-serif;display:grid;place-items:center;text-decoration:none;cursor:pointer;box-shadow:0 3px 12px #0005;padding:0;margin:0}.fab a:hover,.fab button:hover{background:#f6b63d;color:#102c53}.fab .up{opacity:0;pointer-events:none;transition:opacity .2s}.fab .up.on{opacity:1;pointer-events:auto}@media print{.fab{display:none}}

'''
import os as _o0
_o0.makedirs(f'{R}/images/schemas',exist_ok=True)
for _n,_c in _skin.SVGS.items(): open(f'{R}/images/schemas/{_n}','w',encoding='utf-8').write(_c)
open(f'{R}/images/hero-ssi.svg','w',encoding='utf-8').write(_skin.HERO)
open(f'{R}/assets/style.css','w',encoding='utf-8').write(FONTS+css+EXTRA+_skin.CSS)
NAVP=[('index.html','Accueil'),('parcours.html','Parcours'),('cours/','Cours'),('evaluation.html','Évaluation'),('decision.html','Quel symbole ?'),('remplacer.html','Puis-je remplacer ?'),('documents.html','Documents'),('galerie.html','Galerie'),('glossaire.html','Glossaire'),('ressources.html','Ressources'),('credits.html','Crédits'),('suivre.html','Suivre'),('animation.html','Mode animation'),('formateur.html','Espace formateur')]
FAB='''<div class="fab"><a href="index.html" aria-label="Retour à l’accueil" title="Retour à l’accueil">&#8962;</a><button type="button" class="up" aria-label="Remonter en haut de la page" title="Remonter en haut">&#8593;</button></div>
<script>(function(){var b=document.querySelector('.fab .up');if(!b)return;b.addEventListener('click',function(){scrollTo({top:0,behavior:'smooth'})});function t(){b.classList.toggle('on',(pageYOffset||document.documentElement.scrollTop)>300)}addEventListener('scroll',t,{passive:true});t();if('serviceWorker' in navigator&&location.protocol.indexOf('http')===0){navigator.serviceWorker.register('sw.js').catch(function(){})}})();</script>'''
FOOT='''<footer><div class="flogo"><img src="assets/img/logo-consulteam-groupe-valto.png" alt="Consulteam Groupe · Groupe Valto" width="150" height="59" data-nozoom></div>Conception et ingénierie pédagogique : Benoît Deflandre · Contact et informations : formation@consul-team.fr. Édition du 14 novembre 2026, à relire par le formateur avant la session. <a href="REGISTRE-SOURCES.md">Sources et limites</a> · <a href="registre.html">Registre des sources</a> · <a href="QA.md">Contrôles</a><br>Formation, lecture et score ne constituent pas un titre d’habilitation : il est délivré par l’employeur après avis, selon les opérations confiées.</footer>'''
def page(name,title,body,extra='',on=None,scripts=True):
    on=on or name
    nav=''.join(f'<a href="{u}"{" class=on" if u==on else ""}>{t}</a>' for u,t in NAVP)
    s=f'''<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="color-scheme" content="light"><title>{title} — A260E2A</title><meta name="theme-color" content="#102c53"><link rel="manifest" href="manifest.webmanifest"><link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='6' fill='%23102c53'/%3E%3Cpath d='M18 3L8 18h7l-1 11 11-17h-8z' fill='%23f6b63d'/%3E%3C/svg%3E"><link rel="stylesheet" href="assets/style.css"></head><body><a class="skip" href="#main" style="position:absolute;left:-999px">Aller au contenu</a><header class="top"><div class="brand"><img class="logo" src="assets/img/logo-consulteam-groupe.png" alt="Consulteam Groupe" width="190" height="39"><small>Formation initiale A260E2A</small></div><nav>{nav}</nav></header><main id="main">{body}{FOOT}</main><script src="data/content.js"></script><script src="assets/lightbox.js"></script>{extra}{FAB}</body></html>'''
    open(f'{R}/{name}','w',encoding='utf-8').write(s)
SHARED_JS=r'''<script>
'''+_skin.ICONS_JS+r'''
var E=function(s){return String(s==null?'':s).replace(/[&<>"']/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})};
function module(id){return A.modules.filter(function(m){return m.id==id})[0]}
function vis(id){return A.visuels.filter(function(v){return v.id===id})[0]}
function shuffle(a){a=a.slice();for(var i=a.length-1;i>0;i--){var j=Math.floor(Math.random()*(i+1));var t=a[i];a[i]=a[j];a[j]=t}return a}
function statTag(s){var c=s==='repris'?'rep':s==='à compléter'||s==='nouveau'?'cpl':'red';var t=s==='repris'?'Contenu repris':s==='à compléter'?'À compléter':s==='nouveau'?'Nouveau, à valider':'En rédaction';return '<span class="stat '+c+'">'+t+'</span>'}
var GROUPS=[['Socle commun','Tous les stagiaires : mission, danger électrique, rôles, secours.',[1,2,3,8,23]],['B0 · H0 · H0V','Opérations non électriques : zones, voisinage, surveillance.',[4,18]],['Basse tension : BS, BE, BR, BC, B1, B2','Interventions élémentaires, manœuvres, dépannage, consignation, travaux.',[5,6,7,15,10,11,9]],['Appareillage d’un tableau électrique','Reconnaître, équilibrer, remplacer, installer.',[19,20,21,22]],['Haute tension : H1, H2, HC, HE','Domaine HTA/HTB à confirmer avant affichage.',[12,13,14]],['Pratique, évaluation, métier','TP individualisés, avis après formation, installations de sécurité incendie.',[16,17]]];
</script>'''
# ---------- INDEX ----------
nmods=len(mods); nrep=sum(1 for m in mods if m['statut'] in('repris','nouveau'))
body=f'''<div class="herox"><div><p class="lead" style="margin:0">Consulteam × ADI sécurité</p><h1>Habilitation électrique : formation initiale</h1><p class="lead">Trois jours pour intervenir sans danger sur les installations de sécurité incendie : détecter, mettre en sécurité, alimenter, maintenir. Des cas du métier, des schémas à agrandir, des questions flash, et une évaluation à chaque étape.</p><div class="cta"><a href="parcours.html#m17">&#128293; Votre métier : le module ADI</a><a class="alt" href="parcours.html">Mon parcours</a><a class="alt" href="animation.html">Mode animation</a></div></div><img src="images/hero-ssi.svg" alt="Illustration : bâtiment protégé par un système de sécurité incendie" width="520" height="320" data-nozoom></div>
<div class="defi" id="defi"><h2>&#9889; Défi du jour</h2><p id="dq">Chargement…</p><div id="do"></div><button type="button" id="dr" hidden>Voir la réponse</button><button type="button" id="dn">Une autre question</button><div class="ans" id="da" hidden></div></div>
<div class="jours"><div class="jour"><span class="nj">Jour 1 · 14 déc.</span><h3>Comprendre et se situer</h3><ul><li>Mission, titres, danger électrique</li><li>Zones et voisinage</li><li>BS, BE Manœuvre, secours</li></ul></div><div class="jour"><span class="nj">Jour 2 · 15 déc.</span><h3>Le métier ADI en pratique</h3><ul><li>Appareillage, équilibrage</li><li>Remplacer, installer</li><li>BR, consignation BC, SSI</li></ul></div><div class="jour"><span class="nj">Jour 3 · 16 déc.</span><h3>Pratiquer et valider</h3><ul><li>TP individualisés</li><li>Évaluations théorique et pratique</li><li>Avis après formation</li></ul></div></div>
<h2>Sécurité incendie : le métier d’ADI sécurité</h2>
<div class="adiband"><a href="parcours.html#m17"><b><span id="i1"></span>Détecter</b><small>Détecteurs, déclencheurs, ECS</small></a><a href="parcours.html#m17"><b><span id="i2"></span>Mettre en sécurité</b><small>CMSI, portes, clapets, désenfumage</small></a><a href="parcours.html#m17"><b><span id="i3"></span>Alimenter</b><small>Secteur, batterie, AES</small></a><a href="parcours.html#m17"><b><span id="i4"></span>Maintenir</b><small>Visite de vérification, dépannage</small></a></div>
<aside class="fiche"><h2>Fiche de session</h2><dl><dt>Dates</dt><dd>14, 15 et 16 décembre 2026</dd><dt>Lieu</dt><dd>Consul Team Security, La Seyne-sur-Mer (Var)</dd><dt>Client</dt><dd>ADI sécurité</dd><dt>Format</dt><dd>Intra, 3 jours, présentiel, suivi à distance possible</dd><dt>Durée</dt><dd>21 h, dont 7 h de pratique</dd><dt>Participants</dt><dd>4 à 10</dd></dl></aside>
'''+f'''
<div class="band"><div><b>{nmods}</b><span>modules, du socle à la haute tension</span></div><div><b>{nvis}</b><span>images contrôlées, avec fiche de contrôle</span></div><div><b>{nq}+</b><span>questions d’évaluation et du cours</span></div><div><b>21 h</b><span>dont 7 h de pratique</span></div></div>
<h2>Le cours complet</h2>
<p>Le socle électrique et les habilitations de base (B0, H0, H0V, BS, BE Manœuvre) sont dans le cours : chaque rubrique s’ouvre directement.</p>
<div class="grid"><a class="card" href="cours/#foundation">Socle électrique<small>Les bases, du danger au comportement sûr</small></a>
<a class="card" href="cours/#complements">Repères et approfondissements<small>Compléments aux habilitations, limites et vigilances</small></a>
<a class="card" href="cours/#roles">Qui fait quoi ?<small>Rôles, symboles et limites de chacun</small></a>
<a class="card" href="cours/#cases">Cas métiers<small>Situations génériques de maintenance, d’appareillage et de sécurité incendie</small></a>
<a class="card" href="cours/#quiz">Entraînement<small>Questions de réactivation, par séquence</small></a>
<a class="card" href="cours/#tp">Travaux pratiques<small>Ateliers et traces de mise en pratique</small></a>
<a class="card" href="cours/#videos">Vidéothèque<small>Vidéos et supports commentés</small></a>
<a class="card" href="cours/#book">Livret du cours de base<small>Les huit séquences, à lire ou à imprimer</small></a></div>
<h2>Les visuels de la formation</h2>
<div class="gal" id="homegal"></div><p><a href="galerie.html">Voir toute la galerie</a> · <a href="mediatheque.html">Médiathèque</a></p>
<h2>Le parcours A260E2A</h2>
<div class="grid"><a class="card k2" href="parcours.html">Mon parcours par objectif<small>Choisissez votre symbole (B0, BS, BE, BR, BC, B1/B2, H1/H2, HC, HE) : le parcours conseillé se compose. {nmods} modules, tous accessibles.</small></a>
<a class="card k2" href="parcours.html#m19">Appareillage d’un tableau<small>Reconnaître, équilibrer, remplacer, installer : 4 modules et 8 schémas</small></a>
<a class="card k2" href="galerie.html">Galerie<small>{nvis} images et 8 schémas à agrandir</small></a>
<a class="card k2" href="cours/">Ouvrir le cours<small>Accueil du cours complet</small></a></div>
<h2>Aller plus loin en sécurité incendie</h2>
<div class="grid"><a class="card k2" href="parcours.html#m17">Spécificités sécurité incendie<small>Centrale, alimentation, batteries, boucles, travail en hauteur : situer les opérations dans l’habilitation</small></a><a class="card k2" href="parcours.html#m8">Accident, incendie, alerte<small>Protéger, examiner, faire alerter, secourir</small></a></div>
<h2>Vérifier ses acquis</h2>
<div class="grid"><a class="card k3" href="evaluation.html">Évaluation théorique<small>QCM par module ou global, correction immédiate, ordre des réponses mélangé</small></a></div>
<h2>Aller plus loin</h2>
<div class="grid"><a class="card k3" href="livret.html">Livret du participant<small>Les modules rédigés, à imprimer en A4</small></a><a class="card k3" href="suivre.html">Suivre à distance ou hors ligne<small>Téléphone, tablette, installation, sans connexion</small></a><a class="card k3" href="remplacer.html">Puis-je remplacer ?<small>Lampe, fusible, prise : arbres de décision</small></a><a class="card k3" href="glossaire.html">Glossaire<small>Les termes de la formation</small></a><a class="card k3" href="ressources.html">Ressources officielles<small>INRS, Légifrance, Consuel</small></a><a class="card k3" href="mediatheque.html">Médiathèque<small>Images IA contrôlées, schémas légendés</small></a><a class="card k3" href="credits.html">Crédits et limites<small>Origine des contenus, ce qui n’est pas vérifié</small></a></div>
<h2>Animer</h2>
<div class="grid"><a class="card k4" href="animation.html">Mode animation<small>Diapositives plein écran pour la salle, module par module.</small></a><a class="card k4" href="formateur.html">Espace formateur<small>Déroulé, matériel, vigilance, points à valider.</small></a></div>
<h2>Chaque module en cinq phases</h2><ol class="steps"><li><b>Voir</b> : la situation, les visuels à observer, la légende à ouvrir ensuite.</li><li><b>Comprendre</b> : le contenu, les procédures à dérouler pas à pas, un point d’arrêt à chaque étape.</li><li><b>Faire</b> : mise en situation et questions guidées, avec des coups de pouce.</li><li><b>Vérifier</b> : questions de contrôle sans aide, score immédiat.</li><li><b>Retenir</b> : objectif, liste « avant d’agir », impression.</li></ol><div class="note"><b>Cadre.</b> Les mises en pratique, l’évaluation individuelle et l’avis de l’employeur restent indispensables. Le titre d’habilitation et le carnet de prescriptions sont à vérifier avant la session : ce support ne les remplace pas. Les contenus marqués « à valider » n’ont pas encore été relus par le formateur ; la NF C 18-510 n’a pas été lue dans le texte payant.</div>
<p>Les scénarios sont génériques : les installations, les prescriptions et les procédures d’ADI sécurité se précisent avec les participants pendant la session. Aucune donnée nominative n’est publiée ici.</p>'''
page('index.html','Accueil',body,SHARED_JS+'''<script>
(function(){['fire','shield','battery','wrench'].forEach(function(n,i){var e=document.getElementById('i'+(i+1));if(e)e.innerHTML=ico(n)});
var Q=[];A.modules.forEach(function(m){(m.questions||[]).forEach(function(q){if((q.type||'s')==='s')Q.push(q)})});var cur=null;
function tire(){cur=Q[Math.floor(Math.random()*Q.length)];document.getElementById('dq').textContent=cur.q;var o=document.getElementById('do');o.innerHTML='';shuffle(cur.options.map(function(t,i){return{t:t,i:i}})).forEach(function(x){var b=document.createElement('button');b.type='button';b.textContent=x.t;b.onclick=function(){var ok=x.i===cur.correct;var a=document.getElementById('da');a.hidden=false;a.innerHTML=(ok?'&#9989; Bonne réponse. ':'&#10060; Pas tout à fait. Bonne réponse : '+E(cur.options[cur.correct])+'. ')+E(cur.why).replace(/\s*\[[^\]]*\]/g,'')};o.appendChild(b)});document.getElementById('da').hidden=true}
if(Q.length){tire();document.getElementById('dn').onclick=tire}})();
var ids=['TB01','TC06','TC07','BC02','SI01','TB08'],g=document.getElementById('homegal');
g.innerHTML=ids.map(function(i){var v=vis(i);return v?'<figure><img src="'+E(v.fichier)+'" alt="'+E(v.id+' · '+v.titre)+'" loading="lazy"><figcaption>'+E(v.id)+' · '+E(v.titre)+'<br><small style="color:var(--m)">'+E(v.legende)+'</small></figcaption></figure>':''}).join('');</script>''')
# ---------- PARCOURS ----------
page('parcours.html','Parcours','''<small>PARCOURS</small><h1>Parcours de formation</h1><div id="out"></div>''',SHARED_JS+r'''<script>
var out=document.getElementById('out');
'''+open('/home/claude/work/src/studio.js').read()+r'''</script>''')
# ---------- ÉVALUATION ----------
page('evaluation.html','Évaluation','<small>ÉVALUATION</small><h1>Évaluations théoriques</h1><p class="lead">Trois façons d’évaluer : une <b>évaluation générale complète</b> (toute la banque de questions), une <b>évaluation par niveau</b> (symbole visé) et un <b>tirage général de 75 questions</b> pour que deux stagiaires n’aient pas les mêmes. Les réponses sont mélangées à chaque essai. Seuil de réussite de référence : 70 % de bonnes réponses (INRS ED 6127). Ce QCM est un exercice de formation : il ne remplace ni l’évaluation du formateur ni l’observation pratique.</p><div id="out"></div>',SHARED_JS+r'''<script>
var out=document.getElementById('out'),CFG=A.evals_cfg;
function byId(ids){var r=[];A.modules.forEach(function(m){if(ids.indexOf(m.id)>=0)m.questions.forEach(function(q){r.push({q:q,m:m.id})})});return r}
function pick(pool,n,used){var r=[];shuffle(pool).forEach(function(x){if(r.length<n&&!used[x.q.id]){used[x.q.id]=1;r.push(x)}});return r}
function tirage(N){var ms=A.modules.filter(function(m){return m.questions.length}),tot=ms.reduce(function(s,m){return s+m.questions.length},0),Q=ms.map(function(m){return Math.max(1,Math.min(m.questions.length,Math.round(N*m.questions.length/tot)))}),s=Q.reduce(function(a,b){return a+b},0),g=0;
while(s!==N&&g++<500){var i=Math.floor(Math.random()*ms.length);if(s<N&&Q[i]<ms[i].questions.length){Q[i]++;s++}else if(s>N&&Q[i]>1){Q[i]--;s--}}
var r=[];ms.forEach(function(m,i){shuffle(m.questions).slice(0,Q[i]).forEach(function(q){r.push({q:q,m:m.id})})});return r}
function niveau(ev){var N=CFG.n,used={},k=Math.floor(N/4),L=byId(ev.modules);
var r=pick(L,k,used).concat(pick(byId(CFG.zones),k,used),pick(byId(CFG.dangers),k,used),pick(byId(CFG.protec),N-3*k,used));
if(r.length<N)r=r.concat(pick(L.concat(byId(CFG.zones),byId(CFG.dangers),byId(CFG.protec)),N-r.length,used));return r}
function nq(ev){return byId(ev.modules).length}
function choix(){var tot=A.modules.reduce(function(s,m){return s+m.questions.length},0),h='<div class="grid"><a class="card k3" href="#complete"><b>Évaluation générale complète</b><small>Toute la banque : '+tot+' questions, tous niveaux. Pour un bilan de fin de formation.</small></a><a class="card k3" href="#all"><b>Tirage général de 75 questions</b><small>75 questions réparties entre les modules, différentes d’un stagiaire à l’autre.</small></a></div><h2>Par niveau</h2><p class="expl">'+CFG.n+' questions par essai, tirées au hasard : un quart sur les limites du symbole visé, un quart sur les zones et distances, un quart sur les dangers de l’électricité, un quart sur les mesures de protection (thèmes de l’ED 6127 ; QCM de 15 questions minimum tiré d’une base d’au moins cinq fois plus de questions par thème).</p><div class="grid">';
A.evals.forEach(function(ev){var n=nq(ev);h+='<a class="card k3" href="#n-'+ev.id+'">'+E(ev.titre)+'<small>'+E(ev.sym)+' · '+n+' question(s) dans la banque du niveau</small></a>'});
h+='</div><h2>Par module</h2><div class="grid">';A.modules.forEach(function(m){h+=m.questions.length?'<a class="card k3" href="#m'+m.id+'">'+m.id+'. '+E(m.title)+'<small>'+m.questions.length+' question(s)</small></a>':'<div class="card k3" style="opacity:.7">'+m.id+'. '+E(m.title)+'<small>Banque de questions à créer avec le module</small></div>'});out.innerHTML=h+'</div>'}
function quiz(kind,key){var items=[],titre='';
if(kind==='complete'){items=byId(A.modules.map(function(m){return m.id}));titre='Évaluation générale complète'}
else if(kind==='all'){items=tirage(75);titre='Tirage général de 75 questions'}
else if(kind==='n'){var ev=A.evals.filter(function(e){return e.id===key})[0];items=niveau(ev);titre='Évaluation '+ev.titre}
else{A.modules.forEach(function(m){if(m.id==key){m.questions.forEach(function(q){items.push({q:q,m:m.id})});titre='Module '+m.id+' · '+m.title}})}
var qs=shuffle(items).map(function(it){var q=it.q,t=q.type||'s';var o=q.options.map(function(x,i){return{t:x,i:i,ok:t==='s'?i===q.correct:t==='m'?q.correct.indexOf(i)>=0:false}});return{t:t,q:q.q,why:q.why,m:it.m,o:shuffle(o)}});
var h='<p><a href="#">← Retour</a></p><h2>'+E(titre)+'</h2><p class="expl">'+qs.length+' questions. Seuil de référence : '+CFG.seuil+' %.</p><form id="fm">';
qs.forEach(function(q,i){h+='<fieldset class="q" style="border:1px solid var(--l)"><legend>'+(i+1)+'. '+E(q.q)+'</legend>';
if(q.t==='o'){h+='<p class="expl">Attribuez à chaque étape son rang (1 = première).</p>';q.o.forEach(function(o,j){h+='<label class="opt"><select name="q'+i+'_'+j+'"><option value="">–</option>'+q.o.map(function(x,k){return '<option value="'+k+'">'+(k+1)+'</option>'}).join('')+'</select><span>'+E(o.t)+'</span></label>'})}
else{if(q.t==='m')h+='<p class="expl">Plusieurs réponses possibles.</p>';q.o.forEach(function(o,j){h+='<label class="opt"><input type="'+(q.t==='m'?'checkbox':'radio')+'" name="q'+i+'" value="'+j+'"><span>'+E(o.t)+'</span></label>'})}
h+='<p class="expl why" hidden>'+E(q.why)+'</p></fieldset>'});
h+='<button type="submit">Corriger</button></form><div id="res" class="card" hidden></div>';out.innerHTML=h;
document.getElementById('fm').onsubmit=function(e){e.preventDefault();var s=0,ans=0,pm={};
qs.forEach(function(q,i){var fs=document.querySelectorAll('fieldset.q')[i],ok=false,given=false;
if(q.t==='o'){var all=true;q.o.forEach(function(o,j){var sel=fs.querySelector('select[name=q'+i+'_'+j+']');var v=sel.value;if(v!=='')given=true;if(v===''||+v!==o.i)all=false});ok=all;fs.querySelectorAll('.opt').forEach(function(l,j){var v=fs.querySelector('select[name=q'+i+'_'+j+']').value;l.classList.add(v!==''&&+v===q.o[j].i?'good':'bad')})}
else{var lab=fs.querySelectorAll('.opt'),sel=fs.querySelectorAll('input:checked'),picked=[];sel.forEach(function(x){picked.push(+x.value)});given=picked.length>0;
ok=picked.length>0&&q.o.every(function(o,j){return o.ok===(picked.indexOf(j)>=0)});q.o.forEach(function(o,j){if(o.ok)lab[j].classList.add('good');else if(picked.indexOf(j)>=0)lab[j].classList.add('bad')})}
pm[q.m]=pm[q.m]||[0,0];pm[q.m][1]++;if(ok)pm[q.m][0]++;
if(given)ans++;if(ok)s++;fs.classList.add(ok?'good':'bad');fs.querySelector('.why').hidden=false});
var pct=Math.round(100*s/qs.length),r=document.getElementById('res');r.hidden=false;
var rows=Object.keys(pm).sort(function(a,b){return a-b}).map(function(k){var m=module(+k);return '<tr><td>'+k+'. '+E(m.title)+'</td><td>'+pm[k][0]+' / '+pm[k][1]+'</td></tr>'}).join('');
r.innerHTML='<b>Score : '+s+' / '+qs.length+' ('+pct+' %)</b> · '+(pct>=CFG.seuil?'seuil de '+CFG.seuil+' % atteint':'seuil de '+CFG.seuil+' % non atteint')+' ('+ans+' question(s) traitée(s))<p class="expl">Ce score évalue les savoirs seulement : l’évaluation des savoir-faire (pratique) et l’avis après formation relèvent du formateur. Le résultat n’est pas conservé.</p><details open><summary>Résultat par module</summary><table class="tbl"><tbody>'+rows+'</tbody></table></details>';r.scrollIntoView()}}
function route(){var h=location.hash;if(h==='#all')quiz('all');else if(h==='#complete')quiz('complete');else if(/^#n-/.test(h))quiz('n',h.slice(3));else if(/^#m\d+/.test(h))quiz('m',+h.slice(2));else choix()}
addEventListener('hashchange',route);route();</script>''')
import importlib.util as _iu
_sp=_iu.spec_from_file_location('documents','/home/claude/work/src/documents.py');_dm=_iu.module_from_spec(_sp);_sp.loader.exec_module(_dm)
page('documents.html','Documents de session',_dm.CSS+_dm.page_html(),SHARED_JS)
_sp2=_iu.spec_from_file_location('decision','/home/claude/work/src/decision.py');_dc=_iu.module_from_spec(_sp2);_sp2.loader.exec_module(_dc)
page('decision.html','Quel symbole ?',_dc.page_html(),SHARED_JS+_dc.js())
_sp3=_iu.spec_from_file_location('decision_remplacement','/home/claude/work/src/decision_remplacement.py');_dr=_iu.module_from_spec(_sp3);_sp3.loader.exec_module(_dr)
page('remplacer.html','Puis-je remplacer ?',_dr.page_html(),SHARED_JS+_dr.js())
# ---------- QR CODES (suivre sur téléphone) ----------
import segno as _sg, os as _qo
BASE_URL='https://ben2flandre-coder.github.io/consulteam-academy/sessions/a260e2a/'
_qo.makedirs('/home/claude/work/a260e2a/assets/qr',exist_ok=True)
_qr={'home':'','parcours':'parcours.html','evaluation':'evaluation.html','remplacer':'remplacer.html','documents':'documents.html'}
_qr.update({'m%d'%m['id']:'parcours.html#m%d'%m['id'] for m in mods})
for _k,_v in _qr.items(): _sg.make(BASE_URL+_v,error='m').save('/home/claude/work/a260e2a/assets/qr/%s.svg'%_k,scale=4,border=2,dark='#102c53',light='#ffffff')
# ---------- ANIMATION ----------
page('animation.html','Mode animation','''<div class="deck" id="deck" role="region" aria-label="Mode animation"><div class="slide" id="sl" aria-live="polite" tabindex="0"></div><div class="ctl"><button id="pr" aria-label="Précédent">←</button><span id="pg" style="align-self:center"></span><button id="nx" aria-label="Suivant">→</button><select id="ms" aria-label="Module"></select><a href="parcours.html">Quitter</a></div></div>''',SHARED_JS+r'''<script>
var sl=document.getElementById('sl'),ms=document.getElementById('ms'),pg=document.getElementById('pg'),L=[],k=0,cur=0;
var okm=A.modules.filter(function(m){return m.sections.length||m.html});
ms.innerHTML=okm.map(function(m){return '<option value="'+m.id+'">'+m.id+'. '+E(m.title)+'</option>'}).join('');
function strip(h){var d=document.createElement('div');d.innerHTML=h;return d.textContent.replace(/\s+/g,' ').trim()}
function sents(x){return x.split(/(?<=[.!?])\s+(?=[A-ZÀÂÉÈÊÎÔÛÇ«(])/)}
function build(id){cur=+id;var m=module(id);L=[{t:m.title,p:m.goal,i:(m.images||[])[0],tag:'Objectif'}];if(m.scenario)L.push({t:'Situation',p:m.scenario,tag:'Situation de départ'});
if(m.html){var d=document.createElement('div');d.innerHTML=m.html;var np=0;[].slice.call(d.children).forEach(function(el){var tg=el.tagName;
if(tg==='P'){np++;L.push({t:np===1?'Repères':'À retenir',p:strip(el.outerHTML)})}
else if(tg==='OL'||tg==='UL'){[].slice.call(el.children).forEach(function(li,n){var b=li.querySelector('b');var t=b?b.textContent.replace(/[.:]\s*$/,''):'Étape '+(n+1);var txt=strip(li.outerHTML);if(b&&txt.indexOf(b.textContent)===0)txt=txt.slice(b.textContent.length).trim();L.push({t:(tg==='OL'?(n+1)+'. ':'')+t,p:txt})})}
else if(tg==='TABLE'){var rows=[].slice.call(el.querySelectorAll('tr')).map(function(r){return [].slice.call(r.children).map(function(c){return strip(c.outerHTML)}).join(' : ')});L.push({t:'En un coup d’œil',p:rows.join('\n')})}})}
m.sections.forEach(function(s,i){var adi=/^Chez ADI/.test(s[0]);var ss=sents(s[1]);var ch=[];for(var j=0;j<ss.length;j+=2)ch.push(ss.slice(j,j+2).join(' '));ch.forEach(function(c,j){L.push({t:s[0]+(ch.length>1?' ('+(j+1)+'/'+ch.length+')':''),p:c.replace(/\s*\[[^\]]*\]/g,''),i:j===0?(m.images||[])[i+1]:null,tag:adi?'Chez ADI':(/(interdit|jamais|danger|s’arrêt|s'arrêt|dépasse|ne se juge pas|ne met pas|brûlure|chute)/i.test(c)?'Attention':'')})})});
(m.figures||[]).forEach(function(f){L.push({t:f[1],p:'',fig:f[0],tag:'Schéma'})});
if(m.decision)L.push({t:'Décision à prendre',p:m.decision,r:m.answer.replace(/\s*\[[^\]]*\]/g,''),tag:'Décision'});if(m.check.length)L.push({t:'Avant d’agir',p:m.check.map(function(c){return '• '+c}).join('\n')});
var qs=(m.questions||[]).filter(function(q){return (q.type||'s')!=='m'}).slice(0,4);qs.forEach(function(q,n){var c=q.options[q.correct];L.push({t:'Question flash '+(n+1)+'/'+qs.length,p:q.q+'\n\n'+q.options.map(function(o,j){return 'ABCD'.charAt(j)+'. '+o}).join('\n'),r:'Réponse : '+'ABCD'.charAt(q.correct)+'. '+c+'\n'+(q.why||'').replace(/\s*\[[^\]]*\]/g,''),tag:'Question flash'})});
k=0;show()}
function show(){var s=L[k];var v=s.i&&vis(s.i);var dk=document.getElementById('deck');dk.className='deck'+(s.tag==='Attention'?' t-warn':s.tag==='Chez ADI'?' t-adi':s.tag==='Question flash'?' t-flash':s.tag==='Décision'?' t-dec':'');sl.innerHTML='<div class="pbar" style="width:'+Math.round(100*(k+1)/L.length)+'%"></div><span class="wm">'+ico(s.tag==='Attention'?'alert':s.tag==='Chez ADI'?'fire':s.tag==='Question flash'?'spark':icoFor(s.t))+'</span>'+(s.tag?'<small class="tg">'+E(s.tag)+'</small>':'')+'<h1>'+E(s.t)+'</h1><p style="white-space:pre-line">'+E(s.p)+'</p>'+(s.r?'<button class="rv" id="rv">Voir la réponse</button><p class="ans" id="an" style="white-space:pre-line" hidden>'+E(s.r)+'</p>':'')+(s.fig?'<img class="figbig" src="'+E(s.fig)+'" alt="'+E(s.t)+'" data-nozoom>':'')+(v?'<img src="'+E(v.fichier)+'" alt="'+E(v.titre)+'" data-nozoom>':'')+'<div class="qrbox"><img src="assets/qr/m'+cur+'.svg" alt="QR code : ouvrir le module '+cur+' sur son téléphone" data-nozoom><span>Suivre sur votre téléphone :<br>scannez ce code<br>(module '+cur+')</span></div>';pg.textContent=(k+1)+' / '+L.length;var rv=document.getElementById('rv');if(rv)rv.onclick=function(){document.getElementById('an').hidden=false;rv.hidden=true}}
function go(d){k=Math.max(0,Math.min(L.length-1,k+d));show()}
document.getElementById('pr').onclick=function(){go(-1)};document.getElementById('nx').onclick=function(){go(1)};
ms.onchange=function(){location.hash='m'+ms.value;build(ms.value)};
addEventListener('keydown',function(e){if(e.key==='ArrowRight'||e.key===' ')go(1);if(e.key==='ArrowLeft')go(-1)});
var x0=null;sl.addEventListener('touchstart',function(e){x0=e.touches[0].clientX},{passive:true});sl.addEventListener('touchend',function(e){if(x0==null)return;var d=e.changedTouches[0].clientX-x0;if(Math.abs(d)>50)go(d<0?1:-1);x0=null});
var mm=/^#m(\d+)/.exec(location.hash);var id=mm&&okm.some(function(m){return m.id==+mm[1]})?+mm[1]:okm[0].id;ms.value=id;build(id);</script>''')
# ---------- GALERIE / MÉDIATHÈQUE ----------
GAL_JS=SHARED_JS+r'''<script>
var g=document.getElementById('ia');
g.innerHTML=A.visuels.map(function(v){return '<figure class="ia"><div class="ph" data-f="'+E(v.fichier)+'" data-a="'+E(v.id+' · '+v.titre)+'">'+E(v.id)+' · chargement</div><figcaption><b>'+E(v.id)+' · '+E(v.titre)+'</b><br>'+E(v.legende)+'<div class="note">Image générée par IA · contrôle '+E(v.controle)+(v.relecteur?' · '+E(v.relecteur):' · image à venir')+'</div>'+(v.detail?'<details><summary>Contrôle de l’image</summary>'+E(v.detail)+'</details>':'')+'</figcaption></figure>'}).join('');
document.getElementById('sch').innerHTML=A.schemas.map(function(s){return '<figure><img src="'+E(s.fichier)+'" alt="'+E(s.titre)+'" loading="lazy"><figcaption>'+E(s.titre)+'<br><small style="color:var(--m)">Module '+s.module+' · schéma de principe, non à l’échelle</small></figcaption></figure>'}).join('');
function charge(d){var im=new Image();im.alt=d.dataset.a;im.onload=function(){d.replaceWith(im)};im.src=d.dataset.f}
var phs=document.querySelectorAll('.ph');if('IntersectionObserver' in window){var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){io.unobserve(e.target);charge(e.target)}})},{rootMargin:'400px'});phs.forEach(function(d){io.observe(d)})}else{phs.forEach(charge)}</script>'''
GALB='''<small>{k}</small><h1>{t}</h1><p class="lead">Cliquez sur un visuel pour l’agrandir, puis naviguez avec les flèches. Ils illustrent un propos : installations fictives, sans échelle, ils ne désignent aucun matériel agréé et ne remplacent ni une notice ni une prescription.</p>
<h2>Images générées par IA</h2><p>Chaque image porte sa fiche de contrôle. Elles restent à relire par le formateur ; un visuel ne justifie jamais une consigne de sécurité.</p><div class="gal" id="ia"></div>
<h2>Schémas et coupes légendés</h2><div class="gal" id="sch"></div>'''
page('galerie.html','Galerie',GALB.format(k='GALERIE',t='Galerie d’images'),GAL_JS)
page('mediatheque.html','Médiathèque',GALB.format(k='MÉDIATHÈQUE',t='Médiathèque'),GAL_JS,on='galerie.html')
# ---------- GLOSSAIRE ----------
import re
PZH=open('/home/claude/ben2flandre-coder/consulteam-academy/sessions/a260bna/glossaire.html',encoding='utf-8').read()
mm=re.search(r'<h2 id="g0">.*?(?=<h2 id="g5">)',PZH,re.S); pz=mm.group(0)
def term(t,d,s): return f'<div class="card term"><h3 style="margin-top:0">{t}</h3><p style="margin:0">{d}</p><p style="margin:6px 0 0;font-size:14px;color:var(--m)">Source : {s}</p></div>'
APP=[("Disjoncteur divisionnaire","Appareil qui protège un circuit contre la surcharge (bilame) et le court-circuit (bobine magnétique), avec une chambre de coupure pour l’arc.","registre S2, S10 · module 19"),
("Courbe (B, C, D, K, Z)","Indique à partir de quel multiple du calibre le déclencheur magnétique agit. Courbe B : entre 3 et 5 fois le calibre.","registre S19, S20 · module 19"),
("Pouvoir de coupure","Courant de court-circuit maximal que le disjoncteur peut couper ; il doit dépasser le courant de court-circuit présumé à son emplacement.","registre S7 · module 19"),
("Interrupteur différentiel","Compare le courant aller et retour ; un écart signale une fuite vers la terre et provoque le déclenchement. 30 mA en logement. Ne protège pas de la surcharge.","registre S3, S4 · module 19"),
("Contacteur","Ferme ses contacts quand sa bobine est alimentée, les rouvre par ressort sinon ; contacts de puissance et contacts auxiliaires.","registre S5, S17 · module 19"),
("Peigne d’alimentation","Barrette conductrice qui alimente une rangée d’appareils sur rail ; la disposition du tableau se vérifie sur le schéma.","registre S6 · module 19"),
("Déséquilibre de phases","Écart des courants entre phases ; le courant du neutre en est la conséquence avec des charges monophasées résistives.","registre S12, S13 · module 20"),
("VAT (vérification d’absence de tension)","Vérification sur tous les conducteurs actifs, neutre compris, avec un appareil prévu pour cet usage ; la position d’un appareil ne la remplace pas.","registre S16, S22 · module 19")]
gl=pz+'<h2 id="g5">Appareillage d’un tableau</h2><div class="cols2">'+''.join(term(*x) for x in APP)+'</div>'
gl=gl.replace('<h2 id="g0">','<h2 id="g0">',1)
body='<small>GLOSSAIRE</small><h1>Glossaire</h1><p class="lead">Les termes de la formation, en une ou deux phrases, avec leur source. Les définitions complètes et opposables sont dans la norme et le Code du travail.</p><p class="no-print"><input id="q" type="search" placeholder="Chercher un terme (BR, VAT, courbe…)" aria-label="Chercher un terme" style="max-width:420px"></p><nav class="sommaire no-print"><a href="#g0">Tensions et danger</a> <a href="#g1">Habilitations (symboles)</a> <a href="#g2">Voisinage et zones</a> <a href="#g3">Consignation et intervention</a> <a href="#g4">Matériels et protections</a> <a href="#g5">Appareillage d’un tableau</a></nav>'+gl
page('glossaire.html','Glossaire',body,'''<script>document.getElementById('q').addEventListener('input',function(e){var v=e.target.value.toLowerCase();[].forEach.call(document.querySelectorAll('.term'),function(t){t.style.display=t.textContent.toLowerCase().indexOf(v)<0?'none':''})})</script>''')
# ---------- RESSOURCES ----------
SR=sources_new.SOURCES
def rc(s):
    return f'<a class="card k2" href="{H.escape(s["url"])}">{H.escape(s["titre"])}<small>{H.escape(s["usage"])} Accès : {H.escape(s["acces"])}.</small></a>'
body='''<small>RESSOURCES</small><h1>Ressources officielles</h1><p class="lead">Où aller vérifier, après la session, ce qui a été dit en salle. Ces liens sont externes : le contenu en vigueur est celui des sites officiels.</p>
<h2>Réglementation et habilitation</h2><div class="grid">
<a class="card k2" href="https://www.inrs.fr/dam/inrs/CataloguePapier/ED/TI-ED-6127.pdf">INRS ED 6127 · L’habilitation électrique<small>Démarche de prévention (déc. 2020) : BS, BR, BC, limites, recyclage.</small></a>
<a class="card k2" href="https://www.inrs.fr/dam/inrs/CataloguePapier/ED/TI-ED-6109.pdf">INRS ED 6109 · Consignations et déconsignations<small>Les cinq opérations de la consignation électrique, dans l’ordre.</small></a>
<a class="card k2" href="https://sstie.ineris.fr/reglementation/arrete-090713-relatif-dimensions-zone-voisinage-autour-dune-piece-nue-sous-tension">Arrêté du 9 juillet 2013 (INERIS-SSTIE)<small>Dimensions de la zone de voisinage autour d’une pièce nue sous tension.</small></a>
<a class="card k2" href="https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006072050/">Légifrance : Code du travail<small>Articles R. 4544-9 et suivants. Lien vers le code, pas vers l’article.</small></a>
<a class="card k2" href="https://www.inrs.fr/risques/electriques/accidents-origine-electrique.html">INRS : accidents d’origine électrique<small>Chiffres, circonstances typiques, causes principales.</small></a></div>
<h2 id="videos">Vidéos officielles de l’INRS</h2><div class="grid">
<a class="card k2" href="https://www.inrs.fr/media.html?refINRS=DV+0404">Napo dans… Chocs électriques ! (10 min)<small>Film d’animation INRS : contacts direct et indirect, mise en sécurité, court-circuit et arc, maintenance. Pour lancer une discussion en salle.</small></a>
<a class="card k2" href="https://www.inrs.fr/footer/actes-evenements/webinaire-habilitation-electrique.html">Webinaire : comment choisir le symbole d’habilitation ? (1 h)<small>INRS, 12 mars 2019 : le choix du symbole découle de l’analyse de l’activité confiée au travailleur.</small></a>
<a class="card k2" href="https://www.inrs.fr/media.html?refINRS=Anim-132">Le risque électrique : interview d’une experte INRS (1 min 51)<small>Série d’affiches « Pas d’intervention sans habilitation » (A 807 à A 812).</small></a>
<a class="card k2" href="https://www.inrs.fr/risques/electriques/publications-liens-utiles.html">INRS : affiches, application INRS Elec, vidéos<small>Page des publications, outils et liens du dossier Risques électriques.</small></a></div>
<h2>Sources du registre (modules d’appareillage)</h2><div class="grid">'''+''.join(rc(s) for s in SR if s['url'].startswith('http'))+'''</div>
<div class="note"><b>Référentiel.</b> Les limites BS et BR sont celles de l’INRS (ED 6127, FAQ et diaporama INRS), qui fait foi pour la formation. La norme NF C 18-510 (texte compilé de juin 2023, amendement A2) est payante : elle n’est pas reproduite ici.</div>'''
page('ressources.html','Ressources',body)
# ---------- REGISTRE ----------
rows=''.join(f'<tr><td>{s["id"]}</td><td>{("<a href=%s>"%chr(34)+H.escape(s["url"])+"%s</a>"%chr(34)[:0]) if False else ""}{('<a href="'+H.escape(s["url"])+'">'+H.escape(s["titre"])+"</a>") if s["url"].startswith("http") else H.escape(s["titre"])+" <small>("+H.escape(s["url"])+")</small>"}</td><td>{H.escape(s["acces"])}</td><td>{H.escape(s["fiabilite"])}</td><td>{H.escape(s["usage"])}</td><td>{H.escape(s["limites"])}</td></tr>' for s in SR)
page('registre.html','Registre des sources','<small>SOURCES</small><h1>Registre des sources</h1><p class="lead">Aucune règle chiffrée n’est publiée sans source lue. « lu » : page lue en entier ; « extrait » : extrait seulement.</p><table><thead><tr><th>N°</th><th>Source</th><th>Accès</th><th>Fiabilité</th><th>Usage</th><th>Limites</th></tr></thead><tbody>'+rows+'</tbody></table>',on='ressources.html')
# ---------- CRÉDITS ----------
page('credits.html','Crédits et limites',f'''<small>CRÉDITS</small><h1>Crédits et limites</h1><p class="lead">D’où vient chaque élément du support, et ce qui n’a pas été vérifié.</p>
<h2>Origine des contenus</h2><div class="card"><p><b>Cours de base</b> (socle, B0/H0/H0V, BS, BE Manœuvre) : cours Consulteam Academy, support A2604MA.</p><p><b>Séquences BR, BC, voisinage</b> : support A260BNA (Panzani), recalé sur l’arrêté du 9 juillet 2013 et les INRS ED 6127 et ED 6109.</p><p><b>Modules 19 à 22 (appareillage)</b> : rédigés pour cette session à partir de {len(SR)} sources du registre, chaque affirmation étant tracée ([S#], [C] calcul par script, [R] principe à valider).</p><p><b>Images</b> : {nvis} images générées par IA, contrôlées une à une (fiche de contrôle dans chaque légende) ; 8 schémas SVG Consul Team.</p><p>Conception et ingénierie pédagogique : Benoît Deflandre · Contact : formation@consul-team.fr.</p></div>
<h2>Points de vigilance</h2><div class="warn"><ul><li>La norme NF C 18-510 est payante et n’est pas reproduite : le référentiel INRS fait foi.</li><li>Le domaine HTA ou HTB n’est pas précisé par le client : aucun contenu chiffré HT n’est donné sans source.</li><li>Les modules sont relus par le formateur avant la session.</li><li>Les images IA illustrent un propos ; elles ne prouvent aucune règle et peuvent contenir des détails à corriger.</li></ul></div>''')
# ---------- SUIVRE ----------
page('suivre.html','Suivre à distance ou hors ligne','''<small>SUIVRE</small><h1>Suivre à distance ou hors ligne</h1><p class="lead">La même plateforme sert en salle et à distance, sur ordinateur, tablette et téléphone.</p>
<h2>Scanner pour suivre sur téléphone</h2><div class="grid"><div class="card k3"><img src="assets/qr/home.svg" alt="QR code : accueil de la plateforme" width="150" height="150"><b>Accueil</b><small>Adresse : '''+BASE_URL+'''</small></div><div class="card k3"><img src="assets/qr/parcours.svg" alt="QR code : parcours de formation" width="150" height="150"><b>Parcours</b><small>Les 23 modules. Chaque module de la salle porte son propre code en mode animation.</small></div><div class="card k3"><img src="assets/qr/evaluation.svg" alt="QR code : évaluations" width="150" height="150"><b>Évaluations</b><small>QCM par niveau et évaluation générale.</small></div></div><p class="expl">Les codes sont valables une fois la plateforme publiée à l’adresse ci-dessus. Le score reste dans le navigateur.</p>
<h2>Mode d’emploi</h2><ol class="steps"><li>Ouvrez le lien de la plateforme dans le navigateur du téléphone ou de la tablette.</li><li>Parcourez la page d’accueil une première fois avec du réseau : les pages et les images légères se mettent en cache.</li><li>Ajoutez la plateforme à l’écran d’accueil si le navigateur le propose.</li><li>En salle, suivez sur votre appareil le module que le formateur projette (Mode animation).</li><li>À distance, ouvrez le même module et utilisez les exercices et le QCM.</li></ol>
<div class="note"><b>Hors connexion.</b> Après un premier chargement complet, la plateforme fonctionne sans réseau, hors cours de base (fichier lourd) qui demande une première ouverture avec connexion.</div>
<div class="note"><b>Données.</b> Aucune donnée nominative n’est collectée par ce site. Le score du QCM reste dans votre navigateur.</div>''')
# ---------- FORMATEUR ----------
FORM_CLAIR='''<h2>Préparation de la session</h2><p class="lead">Préparation de la session et points à valider avant diffusion.</p>
<h2>Déroulé proposé · 21 h sur 3 jours, dont 7 h de pratique</h2><div class="note">Le déroulé s’adapte aux symboles réellement désignés par ADI sécurité.</div>
<table><thead><tr><th>Jour</th><th>Matin</th><th>Après-midi</th></tr></thead><tbody>
<tr><td>14 déc.</td><td>Accueil, titres et prescriptions, positionnement. Socle : mission, danger, rôles (modules 1 à 3).</td><td>Zones et voisinage (4, 18), BS et BE Manœuvre (5 à 7), secours (8).</td></tr>
<tr><td>15 déc.</td><td>Appareillage d’un tableau : reconnaître, équilibrer (19, 20).</td><td>Remplacer, installer (21, 22) ; BR et consignation BC (10, 11).</td></tr>
<tr><td>16 déc.</td><td>TP individualisés selon symboles et attributs (16).</td><td>Évaluations théorique et pratique, avis après formation, bilan.</td></tr></tbody></table>
<h2>Matériel à prévoir</h2><ul><li>Tableau pédagogique ouvert avec disjoncteurs, différentiel, contacteur, peigne, hors tension.</li><li>VAT bipolaire, cadenas et pancartes de condamnation, pince ampèremétrique.</li><li>EPI et outillage isolé contrôlés ; matériel de sécurité incendie fourni par ADI sécurité si retenu.</li></ul>
<h2>Points à valider par le formateur avant la session</h2><ol class="steps"><li>Relecture technique des modules 9, 12 à 17 et 19 à 23, des schémas, des grilles pratiques et des documents de session.</li><li>Images IA : visages visibles (PR01, BT02, SI03, BT01, NE02, TC09, EX03), gants (TC03), instrument (EX01), images « renforcé » (20).</li><li>Domaine HTA/HTB et symboles réellement concernés chez ADI sécurité.</li></ol>'''
import sys;sys.path.insert(0,'/home/claude/work/src');import lock as _lk,os as _os
_os.makedirs('/home/claude/work/private',exist_ok=True);open('/home/claude/work/private/formateur-clair.html','w',encoding='utf-8').write(FORM_CLAIR)
page('formateur.html','Espace formateur',_lk.lock_body(FORM_CLAIR))
# ---------- LIVRET (statique, imprimable) ----------
def esc(x): return H.escape(str(x))
parts=['<small>LIVRET</small><h1>Livret du participant</h1><p class="lead">Les modules rédigés, à lire ou à imprimer (Imprimer, puis « Enregistrer au format PDF »). Les modules marqués « à valider » attendent la relecture du formateur.</p><p class="no-print"><button type="button" onclick="print()">Imprimer / enregistrer en PDF</button></p>']
for m in mods:
    if not(m['sections'] or m.get('html')): continue
    parts.append(f'<section class="sec"><small>MODULE {m["id"]} · {esc(m["scope"])}</small><h2>{esc(m["title"])}</h2><p class="lead">{esc(m["goal"])}</p>')
    if m.get('scenario'): parts.append(f'<div class="note"><b>Situation de départ.</b> {esc(m["scenario"])}</div>')
    if m.get('html'): parts.append(m['html'])
    for t,x in m['sections']: parts.append(f'<h3>{esc(t)}</h3>'+fmt_sec(x))
    if m.get('decision'): parts.append(f'<div class="card"><b>Décision à prendre :</b> {esc(m["decision"])}<br><b>Réponse :</b> {esc(m["answer"])}</div>')
    if m.get('check'): parts.append('<p><b>Avant d’agir :</b> '+' · '.join(esc(c) for c in m['check'])+'</p>')
    parts.append('</section>')
page('livret.html','Livret du participant',''.join(parts))
