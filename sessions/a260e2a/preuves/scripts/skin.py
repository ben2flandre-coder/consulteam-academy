# -*- coding: utf-8 -*-
# Habillage : icônes, encarts, schémas SSI, accueil illustré. Aucun contenu technique nouveau : les schémas reprennent S42, S43, S44, S48.
N='#102c53';Y='#f6b63d';R_='#c0392b';G='#1d7a4d';B='#2a6fb0';L='#eef3f9'
HEAD='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 340" role="img" aria-labelledby="t d"><title id="t">%s</title><desc id="d">%s</desc><style>text{font-family:Inter,Arial,sans-serif;fill:#102c53}.b{font-weight:700}.s{font-size:12.5px}.m{font-size:15px}.w{fill:#fff}</style><rect width="760" height="340" rx="16" fill="#f4f7fb"/>'
def box(x,y,w,h,fill,lab,sub='',tc=None):
    c=' class="w"' if tc=='w' else ''
    s=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{fill}"/><text x="{x+w/2}" y="{y+h/2-(6 if sub else -5)}" text-anchor="middle" class="b m{" w" if tc=="w" else ""}">{lab}</text>'
    if sub: s+=f'<text x="{x+w/2}" y="{y+h/2+14}" text-anchor="middle" class="s{" w" if tc=="w" else ""}">{sub}</text>'
    return s
def arrow(x1,y1,x2,y2,col=N):
    return f'<path d="M{x1} {y1} L{x2} {y2}" stroke="{col}" stroke-width="3" fill="none" marker-end="url(#a)"/>'
DEF='<defs><marker id="a" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="#102c53"/></marker></defs>'

def f9():
    s=HEAD%("Chaîne d'un système de sécurité incendie","Détecteurs et déclencheurs vers l'ECS, puis le CMSI qui commande les DAS ; l'alimentation de sécurité alimente le système.")+DEF
    s+='<text x="30" y="34" class="b m">Du détecteur à la mise en sécurité</text>'
    s+=box(30,70,170,64,Y,'Détecteurs','automatiques')+box(30,160,170,64,Y,'Déclencheurs','manuels')
    s+=arrow(200,102,262,128)+arrow(200,192,262,168)
    s+=box(264,110,150,80,N,'ECS','contrôle et signalisation','w')
    s+=arrow(414,150,478,150)
    s+=box(480,110,130,80,B,'CMSI','mise en sécurité','w')
    s+=arrow(610,130,640,86)+arrow(610,170,640,214)
    s+=box(640,56,100,60,G,'DAS','portes, clapets','w')+box(640,184,100,60,G,'Diffuseurs','sonores','w')
    s+='<rect x="30" y="262" width="580" height="54" rx="12" fill="#fff" stroke="#c0392b" stroke-width="3" stroke-dasharray="8 5"/><text x="320" y="285" text-anchor="middle" class="b m">Alimentation de sécurité (AES) : secteur + batterie</text><text x="320" y="304" text-anchor="middle" class="s">La batterie reste une source quand le secteur est coupé</text>'
    s+='<text x="614" y="278" class="s b" fill="#c0392b">SDI : détection</text><text x="614" y="296" class="s b">SMSI : mise en sécurité</text></svg>'
    return s
def f10():
    s=HEAD%("Catégories de SSI de A à E","Cinq catégories par ordre de sévérité décroissante, de la plus complète A à la plus simple E.")
    s+='<text x="30" y="34" class="b m">Cinq catégories, de la plus complète à la plus simple</text>'
    rows=[('A','Détection automatique + CMSI',N,'w'),('B','CMSI, sans détection automatique',B,'w'),('C','Commande regroupée + signalisation des positions','#4f8fcf','w'),('D','Commandes regroupées',Y,None),('E','Commande locale de chaque DAS','#f8d58f',None)]
    for i,(l,t,c,tc) in enumerate(rows):
        x=30+i*22;w=700-i*44;y=56+i*54
        s+=f'<rect x="{x}" y="{y}" width="{w}" height="44" rx="10" fill="{c}"/><circle cx="{x+26}" cy="{y+22}" r="16" fill="#fff"/><text x="{x+26}" y="{y+28}" text-anchor="middle" class="b m">{l}</text><text x="{x+56}" y="{y+27}" class="b m{" w" if tc else ""}">{t}</text>'
    s+='<text x="30" y="332" class="s">Sévérité décroissante de A à E · schéma de principe</text></svg>'
    return s
def f11():
    s=HEAD%("Une visite de vérification en sept gestes","Préparer, inspecter, déclencheurs, organes reliés, asservissements, alimentation et batterie, compte rendu.")
    s+='<text x="30" y="34" class="b m">Une visite de vérification, geste par geste</text>'
    st=[('Préparer','et consigner'),('Inspecter','détecteurs, câblage, ECS'),('Déclencheurs','manuels'),('Organes','reliés à l\'ECS'),('Asservissements','par détecteurs'),('Alimentation','et batterie AES'),('Compte rendu','dossier à jour')]
    for i,(a,b) in enumerate(st):
        col=i%4;row=i//4;x=30+col*180;y=64+row*130
        c=R_ if i==5 else N
        s+=f'<rect x="{x}" y="{y}" width="160" height="104" rx="14" fill="#fff" stroke="{c}" stroke-width="3"/><circle cx="{x+28}" cy="{y+28}" r="17" fill="{c}"/><text x="{x+28}" y="{y+34}" text-anchor="middle" class="b m w">{i+1}</text><text x="{x+80}" y="{y+66}" text-anchor="middle" class="b m">{a}</text><text x="{x+80}" y="{y+88}" text-anchor="middle" class="s">{b}</text>'
    s+='<rect x="570" y="194" width="160" height="104" rx="14" fill="#fff1d4"/><text x="650" y="236" text-anchor="middle" class="b m">⚠ Risque électrique</text><text x="650" y="258" text-anchor="middle" class="s">repérer la source</text><text x="650" y="276" text-anchor="middle" class="s">avant chaque geste</text></svg>'
    return s
def f12():
    s=HEAD%("Secteur coupé, batterie encore source","Le secteur est coupé mais la batterie d'alimentation de sécurité continue d'alimenter l'ECS.")+DEF
    s+='<text x="30" y="34" class="b m">Couper le secteur ne met pas l\'ECS hors tension</text>'
    s+=box(30,90,170,80,'#ddd','Secteur','COUPÉ')+'<path d="M40 100 L190 160 M190 100 L40 160" stroke="#c0392b" stroke-width="6"/>'
    s+=box(30,210,170,80,Y,'Batterie','AES')+arrow(200,250,300,160,R_)
    s+=box(300,110,170,100,N,'ECS','toujours alimentée','w')
    s+=arrow(470,160,540,160)
    s+='<rect x="540" y="96" width="190" height="128" rx="14" fill="#fff1d4" stroke="#c0392b" stroke-width="3"/><text x="635" y="132" text-anchor="middle" class="b m">Avant d\'ouvrir</text><text x="635" y="158" text-anchor="middle" class="s">1 · identifier chaque source</text><text x="635" y="178" text-anchor="middle" class="s">2 · traiter secteur et batterie</text><text x="635" y="198" text-anchor="middle" class="s">3 · vérifier l\'absence de tension</text></svg>'
    return s
SVGS={'F9-ssi-chaine.svg':f9(),'F10-ssi-categories.svg':f10(),'F11-visite-verification.svg':f11(),'F12-secteur-batterie.svg':f12()}
SCHEMAS_ADI=[("F9-ssi-chaine.svg","Chaîne d'un SSI : détection, ECS, CMSI, DAS, alimentation",17),("F10-ssi-categories.svg","Catégories de SSI de A à E",17),("F11-visite-verification.svg","Une visite de vérification, geste par geste",17),("F12-secteur-batterie.svg","Secteur coupé, batterie encore source",17)]
FIGS_M17=[["images/schemas/F9-ssi-chaine.svg","Schéma de principe : de la détection à la mise en sécurité, avec l'alimentation de sécurité"],["images/schemas/F10-ssi-categories.svg","Schéma de principe : les catégories de SSI, de A la plus complète à E la plus simple"],["images/schemas/F12-secteur-batterie.svg","Schéma de principe : le secteur coupé, la batterie reste une source"],["images/schemas/F11-visite-verification.svg","Schéma de principe : une visite de vérification, geste par geste"]]

HERO='''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 320" role="img" aria-label="Illustration : bâtiment protégé par un système de sécurité incendie, éclair et bouclier"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#1b4a8a"/><stop offset="1" stop-color="#102c53"/></linearGradient></defs><rect width="520" height="320" rx="22" fill="url(#g)"/><circle cx="420" cy="70" r="46" fill="#f6b63d" opacity=".18"/><rect x="70" y="110" width="170" height="170" rx="6" fill="#fff"/><rect x="90" y="130" width="30" height="30" fill="#c9d8ea"/><rect x="145" y="130" width="30" height="30" fill="#c9d8ea"/><rect x="190" y="130" width="30" height="30" fill="#c9d8ea"/><rect x="90" y="180" width="30" height="30" fill="#c9d8ea"/><rect x="145" y="180" width="30" height="30" fill="#f6b63d"/><rect x="190" y="180" width="30" height="30" fill="#c9d8ea"/><rect x="132" y="228" width="46" height="52" fill="#102c53"/><circle cx="155" cy="104" r="16" fill="#c0392b"/><path d="M147 104h16M155 96v16" stroke="#fff" stroke-width="3"/><path d="M255 130c28 0 28 -28 56 -28M255 150c42 0 42 -48 84 -48" stroke="#f6b63d" stroke-width="4" fill="none" stroke-linecap="round"/><path d="M345 70l56 18v62c0 38-26 62-56 76-30-14-56-38-56-76V88z" fill="#f6b63d"/><path d="M352 100l-24 40h18l-6 36 30-48h-20z" fill="#102c53"/><rect x="300" y="248" width="110" height="38" rx="8" fill="#fff"/><rect x="306" y="254" width="82" height="26" rx="4" fill="#1d7a4d"/><rect x="392" y="261" width="12" height="12" rx="2" fill="#1d7a4d"/><text x="260" y="308" text-anchor="middle" font-family="Inter,Arial" font-size="13" font-weight="700" fill="#fff">détecter · sécuriser · alimenter · maintenir</text></svg>'''

I={
'bolt':'<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>','shield':'<path d="M12 2l8 3v6c0 5-3.5 8.5-8 11-4.5-2.5-8-6-8-11V5z"/><path d="M9 12l2 2 4-4"/>','alert':'<path d="M12 3l10 18H2z"/><path d="M12 10v5M12 18v.5"/>',
'fire':'<path d="M12 22c4 0 7-3 7-7 0-4-3-6-4-10-2 2-3 4-3 6-1-1-2-2-2-4-3 3-5 6-5 8 0 4 3 7 7 7z"/>','battery':'<rect x="2" y="7" width="18" height="10" rx="2"/><path d="M22 10v4M8 9l-2 3h4l-2 3"/>',
'lock':'<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 018 0v3"/>','gauge':'<path d="M4 18a9 9 0 1116 0"/><path d="M12 18l4-6"/>','ruler':'<rect x="2" y="8" width="20" height="8" rx="1"/><path d="M6 8v4M10 8v3M14 8v4M18 8v3"/>',
'cross':'<rect x="3" y="3" width="18" height="18" rx="4"/><path d="M12 8v8M8 12h8"/>','badge':'<circle cx="12" cy="9" r="6"/><path d="M8.5 14L7 22l5-3 5 3-1.5-8"/>','users':'<circle cx="9" cy="8" r="3.5"/><path d="M2 21c0-4 3-6 7-6s7 2 7 6M17 5a3.5 3.5 0 010 7M19 15c2 .8 3 2.6 3 5"/>',
'wrench':'<path d="M14 6a4 4 0 005 5l-9 9a2.5 2.5 0 01-4-4l9-9a4 4 0 003-1z"/>','target':'<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/>','book':'<path d="M4 4h7a3 3 0 013 3v14a2 2 0 00-2-2H4zM20 4h-6M20 4v15h-6"/>',
'eye':'<path d="M2 12s4-7 10-7 10 7 10 7-4 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>','plug':'<path d="M9 2v6M15 2v6M6 8h12v4a6 6 0 01-12 0zM12 18v4"/>','bell':'<path d="M6 17V11a6 6 0 0112 0v6l2 2H4zM10 21h4"/>','clip':'<rect x="5" y="4" width="14" height="18" rx="2"/><path d="M9 4h6v3H9zM9 12h6M9 16h4"/>','ladder':'<path d="M7 2v20M17 2v20M7 6h10M7 11h10M7 16h10"/>','hand':'<path d="M12 2v10M8 5v8M16 5v8M5 10v5a7 7 0 0014 0v-5"/>','spark':'<path d="M12 2l2.5 7.5L22 12l-7.5 2.5L12 22l-2.5-7.5L2 12l7.5-2.5z"/>','building':'<rect x="5" y="3" width="14" height="18" rx="1"/><path d="M9 7h2M13 7h2M9 11h2M13 11h2M10 21v-4h4v4"/>','star':'<path d="M12 2l3 7 7 .6-5.3 4.7L18.5 22 12 18l-6.5 4 1.8-7.7L2 9.6 9 9z"/>'}
import json as _j
ICONS_JS="var ICO="+_j.dumps(I,ensure_ascii=False)+";function ico(n,c){return '<svg class=\"ic '+(c||'')+'\" viewBox=\"0 0 24 24\" width=\"24\" height=\"24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\" aria-hidden=\"true\">'+(ICO[n]||ICO.bolt)+'</svg>'}\nvar MICO={1:'target',2:'bolt',3:'users',4:'ruler',5:'hand',6:'gauge',7:'plug',8:'cross',9:'clip',10:'wrench',11:'lock',12:'building',13:'lock',14:'plug',15:'gauge',16:'star',17:'fire',18:'shield',19:'book',20:'gauge',21:'wrench',22:'plug',23:'alert'};\nfunction icoFor(t){t=String(t).toLowerCase();var K=[['chez adi','fire'],['danger','alert'],['risque','alert'],['batter','battery'],['alimentation','battery'],['source','battery'],['consign','lock'],['vérif','gauge'],['mesur','gauge'],['essai','gauge'],['zone','ruler'],['voisinage','ruler'],['distance','ruler'],['secours','cross'],['accident','cross'],['alerte','bell'],['habilit','badge'],['titre','badge'],['symbole','badge'],['rôle','users'],['qui fait','users'],['dépann','wrench'],['maintenance','wrench'],['remplac','wrench'],['décision','target'],['situation','target'],['objectif','target'],['question','spark'],['visite','clip'],['catégor','building'],['catégor','building']];for(var i=0;i<K.length;i++)if(t.indexOf(K[i][0])>=0)return K[i][1];return 'bolt'}"

CSS='''
.ic{width:1.35em;height:1.35em;vertical-align:-.3em;flex:none}
.mico{display:inline-grid;place-items:center;width:46px;height:46px;border-radius:14px;background:#102c53;color:#f6b63d;margin-right:10px;flex:none}.mico .ic{width:26px;height:26px}
.card.k2 .cap{display:flex;align-items:center;gap:6px;margin-bottom:6px}
.mhead .bigico{display:flex;align-items:center;gap:12px;margin-bottom:6px}.mhead .bigico .mico{width:58px;height:58px;border-radius:18px}.mhead .bigico .mico .ic{width:34px;height:34px}
.banner{margin:0 0 18px;border-radius:18px;overflow:hidden;border:2px solid #102c53;max-height:280px}.banner img{width:100%;height:280px;object-fit:cover;display:block}
.card.adi,details.sc.adi{border:2px solid #f6b63d;background:linear-gradient(135deg,#fff8e6,#fff);color:#16273d;position:relative}.card.adi::after,details.sc.adi::after{content:"CHEZ ADI";position:absolute;top:-11px;right:16px;background:#c0392b;color:#fff;font-weight:800;font-size:.72rem;letter-spacing:.08em;padding:3px 12px;border-radius:999px}
section.card h3 .sico,details.sc summary .sico{color:#c0392b;margin-right:4px}
.lead1{font-weight:700;font-size:1.06em}
.wn{display:block;background:#fdecea;color:#6b1b12;border-left:6px solid #c0392b;border-radius:8px;padding:8px 12px;margin:8px 0;font-weight:600}.wn .ic{color:#c0392b}
.hook{display:flex;gap:16px;align-items:flex-start;border-left:7px solid #f6b63d;background:#fff1d4;color:#16273d}.hook .hico{display:grid;place-items:center;width:54px;height:54px;border-radius:50%;background:#102c53;color:#f6b63d;flex:none}.hook .hico .ic{width:30px;height:30px}.hook small{display:block;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:#8a5a00;margin-bottom:4px}
.card.sit{border-top:6px solid #1d7a4d}.card.sit h3 .ic{color:#1d7a4d}
.reflex{background:#102c53;color:#fff;border-radius:16px;padding:14px 20px;margin:18px 0}.reflex h3{color:#f6b63d;margin-top:0}.reflex li,.reflex label{color:#fff}.reflex ul{list-style:none;padding-left:0}.reflex li{padding:6px 0;border-bottom:1px dashed rgba(255,255,255,.25)}.reflex li:before{content:"✔ ";color:#f6b63d;font-weight:800}.reflex li:has(input):before{content:""}
.gbar{display:flex;gap:10px;flex-wrap:wrap;margin:10px 0 18px}.gbar .jr{flex:1 1 200px;border-radius:14px;padding:12px 14px;background:#102c53;color:#fff}.gbar .jr b{color:#f6b63d;display:block}.gbar .jr small{color:#dbe6f5}
.herox{display:grid;grid-template-columns:1.2fr 1fr;gap:24px;align-items:center;margin:8px 0 22px}.herox>*{min-width:0}.herox img{width:100%;height:auto;border-radius:22px;box-shadow:0 10px 30px rgba(16,44,83,.25)}@media(max-width:820px){.herox{grid-template-columns:minmax(0,1fr)}}
.cta{display:flex;gap:10px;flex-wrap:wrap;margin-top:14px}.cta a{display:inline-flex;align-items:center;gap:8px;text-decoration:none;font-weight:800;padding:12px 18px;border-radius:12px;background:#f6b63d;color:#102c53;border:2px solid #102c53}.cta a.alt{background:#fff}
.jours{padding-top:12px;display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:14px;margin:12px 0 24px}.jour{border-radius:18px;padding:16px;background:#fff;border:2px solid #102c53;color:#16273d;position:relative}.jour .nj{position:absolute;top:-14px;left:16px;background:#f6b63d;color:#102c53;font-weight:900;border-radius:999px;padding:3px 14px}.jour h3{margin:6px 0 4px;color:#102c53}.jour ul{margin:6px 0 0;padding-left:18px}
.defi{border-radius:20px;background:linear-gradient(135deg,#102c53,#1b4a8a);color:#fff;padding:18px 22px;margin:18px 0}.defi h2{color:#f6b63d;margin:0 0 8px}.defi button{background:#f6b63d;color:#102c53;border:0;border-radius:10px;padding:10px 16px;font-weight:800;cursor:pointer;margin:6px 8px 0 0}.defi .ans{background:rgba(255,255,255,.14);border-radius:10px;padding:10px 14px;margin-top:10px}
.adiband{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:12px;margin:12px 0 22px}.adiband a{text-decoration:none;color:#16273d;background:#fff8e6;border:2px solid #f6b63d;border-radius:16px;padding:14px;display:block}.adiband a b{display:flex;align-items:center;gap:8px;color:#102c53}.adiband .ic{color:#c0392b}.adiband small{display:block;margin-top:4px;color:#445}
.deck .slide{transition:opacity .25s}.deck .pbar{position:absolute;left:0;top:0;height:6px;background:#f6b63d;border-radius:0 6px 6px 0;transition:width .3s}.deck .wm{position:absolute;right:28px;top:22px;opacity:.16;color:#fff}.deck .wm .ic{width:140px;height:140px}
.deck.t-warn .slide{background:linear-gradient(135deg,#8c1d13,#3b0d09)}.deck.t-warn .wm{opacity:.28}.deck.t-adi .slide{background:linear-gradient(135deg,#7a1f16,#102c53)}.deck.t-flash .slide{background:linear-gradient(135deg,#1b4a8a,#102c53)}.deck.t-dec .slide{background:linear-gradient(135deg,#0f5c37,#102c53)}.deck .figbig{max-height:62vh;max-width:100%;width:auto;background:#fff;border-radius:14px;padding:8px;align-self:center;margin-top:10px}
@media print{.herox svg,.banner{break-inside:avoid}}
'''
CSS+='''
main>.fiche{background:#102c53;color:#fff;border-radius:18px;padding:16px 22px;border-left:10px solid #f6b63d;margin:12px 0 22px;display:block}main>.fiche h2{color:#fff;margin-top:0}main>.fiche dl{display:grid;grid-template-columns:auto 1fr;gap:6px 18px;margin:0}main>.fiche dt{color:#f6b63d;font-weight:700}main>.fiche dd{margin:0;color:#fff}
'''
CSS+='''
@media(max-width:900px){header.top{position:static;padding:8px 14px;gap:4px 12px}header.top .brand small{display:none}header.top .logo{height:30px;width:auto}header.top nav{flex-wrap:nowrap;overflow-x:auto;margin-left:0;width:100%;-webkit-overflow-scrolling:touch;scrollbar-width:thin;padding-bottom:4px}header.top nav a{white-space:nowrap;flex:none;padding:6px 10px;font-size:14px}.herox h1{font-size:1.9rem}}
'''
