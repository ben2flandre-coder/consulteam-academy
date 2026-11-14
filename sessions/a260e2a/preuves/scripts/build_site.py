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
mods[7]['sections'].append(["Les trois actions selon l'INRS","Couper le courant sans toucher la victime ; si ce n'est pas possible, la dégager des parties sous tension sans exposer d'autre personne [S31]. Alerter le sauveteur secouriste du travail, puis les secours : 15, 18 ou 112 [S31]. Secourir en restant auprès de la victime jusqu'à l'arrivée des secours [S31]. Les premières minutes sont déterminantes, et toute personne qui travaille près d'installations sous tension doit avoir des notions de secourisme [S31]. Les gestes détaillés du sauveteur secouriste du travail ne sont pas repris ici : ils relèvent de la formation SST [R]."])
mods[7]['sections'].append(["Protéger avant de secourir (cadre SST)","Avant d'approcher la victime, analyser ce qui s'est passé et chercher les dangers persistants : mécanique, électrique, thermique, atmosphère irrespirable [S33]. Si le danger peut être supprimé sans risque, le supprimer ; sinon l'isoler et interdire l'accès à la zone ; sinon seulement, soustraire la victime [S33, S35]. Le dégagement d'urgence reste une manœuvre exceptionnelle, réservée au danger réel, immédiat et non contrôlable qui menace la vie de la victime [S33]. Le sauveteur agit sans risque pour lui-même, afin d'éviter un sur-accident [S35]."])
mods[7]['sections'].append(["Habilitation électrique et SST : deux compétences distinctes","Les gestes acquis à l'habilitation électrique ne remplacent pas ceux de la formation de sauveteur secouriste du travail [S34]. La réglementation n'oblige pas à former les habilités au SST : la décision revient à l'employeur après consultation du médecin du travail [S34]. La double compétence est recommandée [S34]. Seuls les habilités savent dégager la victime d'un accident électrique sans se mettre en danger, en attendant les secours formés au SST [S34]."])
mods[7]['sections'].append(["Brûlure électrique : conduite à tenir","Après la protection et l'examen, arroser la zone brûlée à l'eau courante tempérée, alerter les secours puis surveiller la victime : lui parler, la protéger du froid, de la chaleur et des intempéries [S33]. L'arrosage dure au moins dix minutes, idéalement vingt [S35]. Aucun produit ne s'applique sur une brûlure sans avis médical [S33]."])
mods[7]['note']="Section « trois actions » ajoutée à partir de la page INRS relue le 14/11/2026 [S31]. Cadre SST complété le 14/11/2026 à partir du guide des données techniques SST V5.01/2024, de l'ED 4085 et de TS876 [S33, S34, S35] ; l'ED 7000 reste à lire."
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
LEG=" Repères : [S1…S51] = source du registre ; [C] = calcul prouvé par script ; [R] = principe de raisonnement à valider par le formateur."
import modules_ed6127
for m in modules_tb.MODULES:
    m=dict(m); m['note']=m['note']+LEG; mods.append(m)
for m in modules_ed6127.MODULES:
    m=dict(m); m['note']=m['note']+LEG; m.setdefault('figures',[]); m.setdefault('html',''); m.setdefault('exercices',[])
    for k,x in enumerate(mods):
        if x['id']==m['id']: mods[k]=m; break
    else: mods.append(m)
SCHEMAS=[("F1-facade-tableau.svg","Vue de face d'un tableau de répartition",19),("F2-coupe-disjoncteur.svg","Coupe d'un disjoncteur modulaire",19),("F3-principe-differentiel.svg","Principe d'un interrupteur différentiel",19),("F4-coupe-contacteur.svg","Coupe d'un contacteur",19),("F5-coupe-rail-peigne.svg","Coupe d'une rangée : rail, peigne, raccordements",21),("F6-equilibrage-avant-apres.svg","Équilibrage : avant et après (exemple chiffré)",20),("F7-remplacement-appareil.svg","Remplacer un appareil : les étapes",21),("F8-installation-appareil.svg","Installer un nouvel appareil : les étapes",22)]
import q_complements, adi
for m in mods:
    _c=adi.CHEZ.get(m['id'])
    if _c:
        m['sections']=list(m['sections'])+[_c['sec']]; m['questions']=list(m['questions'])+_c['qs']
for m in mods:
    m['questions'].extend(q_complements.QC.get(m['id'],[]))
for m in mods:
    for q in m['questions']: q.setdefault('type','s')
for m in mods:
    m.setdefault('html','');m.setdefault('figures',[]);m.setdefault('exercices',[])
import skin
SCHEMAS+=skin.SCHEMAS_ADI
for m in mods:
    if m['id']==17: m['figures']=list(m.get('figures',[]))+skin.FIGS_M17
import csv
SUIVI={x['id']:x for x in csv.DictReader(open('/tmp/up/suivi-visuels-A260E2A.csv',encoding='utf-8-sig'),delimiter=';')}
vis=[dict(id=i['id'],titre=i['titre'],module=i['module'],format=i['format'],legende=i['legende'],controle=i['controle_technique'],fichier=('images/ia/'+i['id']+'.webp'),statut=SUIVI.get(i['id'],{}).get('statut','image à venir'),relecteur=SUIVI.get(i['id'],{}).get('relecteur',''),detail=SUIVI.get(i['id'],{}).get('controle_effectue','')) for i in prompts['images']]
COUPES=[('CPA','Coupe d’un disjoncteur modulaire','Coupe de principe : bobine, bilame, contacts et chambre de coupure.','coupe-A'),('CPB','Coupe d’un contacteur','Coupe de principe : bobine, contacts de puissance et ressort de rappel.','coupe-B'),('CPC','Coupe d’un peigne d’alimentation','Coupe de principe : dents du peigne engagées dans une borne.','coupe-C'),('CPD','Coupe d’un appareil sur rail','Coupe de principe : crochet, rail et verrou de fixation.','coupe-D'),('CPE','Coupe d’une pince ampèremétrique','Coupe de principe : le circuit magnétique entoure un seul conducteur.','coupe-E')]
for i,t,l,f in COUPES: vis.append(dict(id=i,titre=t,module='CP',format='coupe 3:2 1536x1024',legende=l,controle='renforcé',fichier='images/coupes/'+f+'.webp',statut='À relire par le formateur',relecteur='Claude (examen visuel du 14/11/2026)',detail='Coupe de principe générée par IA (lot GPT du 14/11/2026) : aucun texte lisible, aucune cote. L’examen visuel ne vaut pas validation technique : organes et proportions à faire confirmer.'))
data=dict(session="A260E2A",titre="Habilitation électrique : formation initiale",dates="14, 15 et 16 décembre 2026",lieu="Consul Team Security, La Seyne-sur-Mer",modules=mods,videos=acad['videos'],tps=acad['tps'],sources=acad['sources'],visuels=vis,schemas=[dict(fichier='images/schemas/'+f,titre=ti,module=mo) for f,ti,mo in SCHEMAS],registre=sources_new.SOURCES)

EVALS=[dict(id='socle',titre='Socle commun',sym='Tous les stagiaires',modules=[1,2,3,8,23]),
 dict(id='b0',titre='B0 · H0 · H0V',sym='B0, H0, H0V',modules=[4,18]),
 dict(id='bs',titre='BS',sym='BS',modules=[5,6]),
 dict(id='bem',titre='BE Manœuvre',sym='BE Manœuvre',modules=[6,7]),
 dict(id='bemve',titre='BE Mesurage · Vérification · Essai',sym='BE Mesurage, Vérification, Essai',modules=[15]),
 dict(id='b1b2',titre='B1 · B1V · B2 · B2V',sym='B1, B1V, B2, B2V',modules=[9,18]),
 dict(id='br',titre='BR',sym='BR',modules=[10,21,22]),
 dict(id='bc',titre='BC',sym='BC',modules=[11]),
 dict(id='h1h2',titre='H1 · H1V · H2 · H2V',sym='H1, H1V, H2, H2V',modules=[12]),
 dict(id='hc',titre='HC',sym='HC',modules=[13]),
 dict(id='he',titre='HE Manœuvre',sym='HE Manœuvre',modules=[14]),
 dict(id='metier',titre='Appareillage, pratique et métier',sym='Tous niveaux (selon mission)',modules=[16,17,19,20])]
data['evals']=EVALS
data['evals_cfg']=dict(zones=[4,18],socle=[1,2,3,8,23],dangers=[2],protec=[6,8,23],n=16,seuil=70)
open(f'{R}/data/content.js','w',encoding='utf-8').write("window.A="+json.dumps(data,ensure_ascii=False)+";")
json.dump({"destinataire":"ben2flandre@gmail.com","endpoint":""},open(f'{R}/assets/config.json','w'))
exec(open('/home/claude/work/present.py',encoding='utf-8').read())
open(f'{R}/manifest.webmanifest','w').write(json.dumps({"name":"Habilitation électrique A260E2A","short_name":"Habilitation","start_url":"index.html","display":"standalone","background_color":"#102c53","theme_color":"#102c53","lang":"fr","icons":[]}))
files=['index.html','parcours.html','evaluation.html','documents.html','decision.html','remplacer.html','animation.html','mediatheque.html','galerie.html','glossaire.html','ressources.html','credits.html','suivre.html','livret.html','registre.html','formateur.html','assets/style.css','assets/lightbox.js','assets/config.json','data/content.js','manifest.webmanifest']
import glob
files+=sorted(os.path.relpath(p,R) for p in glob.glob(R+'/images/**/*',recursive=True) if os.path.isfile(p))
files+=sorted(os.path.relpath(p,R) for p in glob.glob(R+'/assets/qr/*.svg'))
ver=hashlib.sha256(b''.join(open(f'{R}/{f}','rb').read() for f in files)).hexdigest()[:10]
open(f'{R}/sw.js','w').write("var V='a260e2a-%s',F=%s;self.addEventListener('install',function(e){e.waitUntil(caches.open(V).then(function(c){return c.addAll(F)}).then(function(){return self.skipWaiting()}))});self.addEventListener('activate',function(e){e.waitUntil(caches.keys().then(function(k){return Promise.all(k.filter(function(x){return x!==V}).map(function(x){return caches.delete(x)}))}).then(function(){return self.clients.claim()}))});self.addEventListener('fetch',function(e){if(e.request.method!=='GET')return;e.respondWith(caches.match(e.request).then(function(r){return r||fetch(e.request).then(function(n){var c=n.clone();caches.open(V).then(function(x){x.put(e.request,c)});return n}).catch(function(){return r})}))});"%(ver,json.dumps(files+['sw.js'][:0])))
print(ver,len(mods),sum(len(m['questions']) for m in mods))
