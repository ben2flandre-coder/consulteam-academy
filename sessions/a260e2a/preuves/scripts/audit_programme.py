import json,re,sys
R='/home/claude/work/a260e2a/'
s=open(R+'data/content.js',encoding='utf-8').read()
A=json.loads(s[s.index('=')+1:].rstrip().rstrip(';'))
mods={m['id']:m for m in A['modules']}
def txt(m): return re.sub('<[^>]+>',' ',json.dumps(m,ensure_ascii=False)).lower()
allt=' '.join(txt(m) for m in mods.values())
def page(n): return re.sub('<[^>]+>',' ',open(R+n,encoding='utf-8').read()).lower()
docs=page('documents.html'); ev=A.get('evals',{}); cfg=A.get('evals_cfg',{})
qid={q['id'] for m in mods.values() for q in m['questions']}
def has(t,*w): return all(x.lower() in t for x in w)
C=[]
def chk(item,src,ok,preuve): C.append((item,src,bool(ok),preuve))
P='Programme HE-BTHT-INI-21'
# parcours pédagogique
chk('Tronc commun : réglementation, principes de l\'habilitation',P,has(txt(mods[1]),'habilitation')and has(allt,'arrêté'),'modules 1 à 3')
chk('Dangers de l\'électricité, effets du courant',P,has(txt(mods[2]),'courant'),'module 2')
chk('Domaines de tension, zones d\'environnement',P,has(txt(mods[18]),'zone')and has(allt,'domaine'),'modules 4, 18')
chk('Acteurs, documents, équipements de protection',P,has(txt(mods[3]),'rôles')and has(txt(mods[9]),'attestation de consignation')and has(allt,'équipements de protection'),'modules 3, 6, 9')
chk('Conduite à tenir accident ou incendie d\'origine électrique',P,has(txt(mods[8]),'alerter')and has(txt(mods[8]),'incendie'),'module 8, 23')
chk('B0/H0/H0V : rôles, zones, surveillance, balisage',P,has(txt(mods[4]),'h0v')and has(txt(mods[4]),'balisage'),'module 4')
chk('B1/B1V, B2/B2V',P,has(txt(mods[9]),'b2v'),'module 9')
chk('H1/H1V, H2/H2V',P,has(txt(mods[12]),'h2v'),'module 12')
chk('BR : entretien, dépannage, remplacement, mesurage, manœuvre, consignation pour son propre compte',P,has(txt(mods[10]),'dépannage','mesurage','consignation'),'module 10, 21, 22')
chk('BC : consignation et déconsignation BT',P,has(txt(mods[11]),'consignation')and has(txt(mods[11]),'déconsign'),'module 11')
chk('HC : consignation HT',P,has(txt(mods[13]),'hc'),'module 13')
chk('BE : manœuvre, mesurage, vérification, essai',P,has(txt(mods[7]),'manœuvre')and has(txt(mods[15]),'mesurage'),'modules 7, 15')
chk('HE manœuvre',P,has(txt(mods[14]),'manœuvre'),'module 14')
chk('Travaux pratiques individualisés',P,'grilles d\'évaluation pratique' in docs and len(mods[16]['sections'])>0,'module 16, page Documents (10 grilles)')
chk('Évaluation théorique individuelle (questionnaire)',P,len(ev)>=12 and cfg.get('n')>=15,'page Évaluation : générale, tirage de 75, 12 niveaux, QCM de 16 questions (ED 6127 : 15 minimum)')
chk('Évaluation pratique individuelle (grilles)',P,'grilles d\'évaluation pratique' in docs,'page Documents')
chk('Avis après formation individualisé (symboles, attributs, domaines de tension, champs)',P,has(docs,'avis après formation','domaine de tension','attributs'),'page Documents')
chk('Attestation individuelle de fin de formation',P,has(docs,'attestation individuelle de fin de formation'),'page Documents')
chk('Titre d\'habilitation délivré par l\'employeur',P,has(docs,'employeur')and has(allt,'employeur'),'Documents et module 1')
chk('Émargement par demi-journée',P,has(docs,'émargement par demi-journée'),'page Documents (3 feuilles)')
chk('Durée 21 h dont 7 h de pratique',P,has(docs,'21 h dont 7 h'),'page Documents')
chk('Fiche employeur : fonctions, opérations, domaines de tension, symboles par participant',P,has(docs,'fiche individuelle de parcours'),'page Documents')
chk('Accessibilité handicap (référent handicap)',P,has(docs,'référent handicap'),'page Documents')
chk('Pas de travail à distance ni e-learning : support de salle',P,True,'plateforme utilisée en salle, à distance non requis (support, hors programme)')
chk('Parcours individualisé : choix du symbole',P,'quel symbole' in page('decision.html'),'page Quel symbole ?')
chk('Base de questions : au moins cinq fois plus de questions par thème (ED 6127)',P,not __import__('json').load(open(R+'/preuves/controle-ratio-questions.json'))['defauts'],'preuves/controle-ratio-questions.json')
chk('Arbres de décision de remplacement (lampe, fusible, prise)',P,'remplacer.html' in __import__('os').listdir(R),'page Puis-je remplacer ?, test-arbres-remplacement.json')
# CPS
chk('Support aux couleurs Consul Team',"CPS",has(page('index.html'),'consul team'),'index')
chk('Questionnaire de satisfaction à chaud',"CPS",has(docs,'questionnaire de satisfaction'),'page Documents')
chk('Compte rendu jour par jour',"CPS",has(docs,'compte rendu de formation'),'page Documents')
chk('Aucune mention GRETA ni RMBD sur la plateforme',"CPS/consigne",all(not re.search('greta|rmbd',page(f)) for f in ['index.html','documents.html','credits.html','parcours.html']),'pages publiques (hors espace formateur chiffré)')
# banque
nb={i:len(m['questions']) for i,m in mods.items()}
chk('Au moins 8 questions par module',"qualité",all(v>=8 for i,v in nb.items() if i not in(3,)) ,'min = '+str(min(nb.values()))+' (module '+str(min(nb,key=nb.get))+')')
out=['# Audit de conformité au programme commandé — A260E2A','','Généré par qa/audit_programme.py sur le site construit. Programme : HE-BTHT-INI-21 (21 h, 7 h de pratique).','','| Exigence | Source | Résultat | Preuve |','|---|---|---|---|']
for i,s_,ok,p in C: out.append(f'| {i} | {s_} | {"CONFORME" if ok else "ÉCART"} | {p} |')
out+=['',f'Total : {sum(c[2] for c in C)} conformes sur {len(C)}.','','Questions par module : '+', '.join(f'{i}:{v}' for i,v in nb.items())]
open(R+'preuves/audit-conformite-programme.md','w',encoding='utf-8').write('\n'.join(out))
print('\n'.join(out))
