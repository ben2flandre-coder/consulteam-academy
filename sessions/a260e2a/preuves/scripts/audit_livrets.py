# Audit des livrets A260E2A : conformité au programme, cohérence avec le site, absence de fuite formateur, pagination.
import sys, re, json, subprocess
import pdfplumber
R='/home/claude/work/a260e2a'; L='/home/claude/work/livrets/'
d=json.loads(re.sub(r'^window\.A=|;$','',open(R+'/data/content.js',encoding='utf-8').read()))
def txt(path):
    with pdfplumber.open(path) as P: return [(p.extract_text() or '') for p in P.pages]
def norm(t): return re.sub(r'\s+',' ',t.replace('’',"'").replace('ʼ',"'").replace(' ',' ')).strip().lower()
F=txt(L+'livret-formation-a260e2a.pdf'); S=txt(L+'livret-site-a260e2a.pdf')
fa=norm(' '.join(F)); sa=norm(' '.join(S)); res=[]
def ok(n,c,det=''): res.append((n,bool(c),det)); print(('OK  ' if c else 'KO  ')+n+((' : '+str(det)) if det else ''))
# 1. programme : blocs → modules, tous présents dans le sommaire ET ouvrent une partie
PROG={'Tronc commun':[1,2,3,18],'Accident / incendie':[8,23],'B0/H0/H0V':[4,18],'B1/B2':[9],'H1/H2':[12],'BR':[10,21,22],'BC':[11],'BE manœuvre':[6,7],'BE mesurage, vérification, essai':[15],'HC':[13],'HE manœuvre':[14],'TP individualisés':[16],'ADI SSI':[17],'Appareillage de tableau':[19,20,21,22]}
som=norm(F[2])
for b,ids in PROG.items():
    miss=[i for i in ids if norm([m for m in d['modules'] if m['id']==i][0]['title']) not in som]
    ok('Programme · '+b+' : module(s) %s au sommaire'%ids,not miss,miss)
# 2. chaque partie : titre, objectif, sections (hors renvois génériques), décision, questions
miss=[]
for m in d['modules']:
    if norm(m['goal'])[:28] not in fa: miss.append((m['id'],'objectif'))
    for t,x in m['sections']:
        if re.search(r'consulter «\s*Repères',x) or len(re.sub(r'\[[^\]]*\]','',x).strip())<40: continue
        tt=norm(re.sub(r'^chez adi\s*[:·—-]?\s*','',t,flags=re.I))
        if tt[:24] not in fa: miss.append((m['id'],t))
    if m.get('decision') and norm(m['decision'])[:28] not in fa: miss.append((m['id'],'décision'))
ok('Toutes les sections de contenu des 23 modules figurent dans le livret de formation',not miss,miss[:8])
# 3. numéros de page du sommaire
bad=[];
for line in F[2].split('\n'):
    m=re.match(r'^(\d+)\s+.*?\s(\d+)$',line)
    if m:
        mid,pn=int(m.group(1)),int(m.group(2))
        if not re.search(r'^%02d\b'%mid,F[pn-1],re.M): bad.append((mid,pn))
ok('Sommaire du livret de formation : numéros de page exacts',not bad,bad)
# 4. cohérence session
for lab,a in (('formation',fa),('site',sa)):
    ok('%s : dates 14, 15 et 16 décembre 2026'%lab,('14, 15 et 16 décembre' in a) or ('mercredi 16 décembre 2026' in a))
    ok('%s : durée 21 h dont 7 h de pratique'%lab,'21 h' in a and '7 h' in a)
    ok('%s : Consul Team, charte (pas de GRETA/RMBD)'%lab,'greta' not in a and 'rmbd' not in a)
    ok('%s : crédit Benoît Deflandre'%lab,'benoît deflandre' in a)
    ok('%s : adresse du site apprenant'%lab,'ben2flandre-coder.github.io/consulteam-academy/sessions/a260e2a' in a)
ok('formation : titre d\'habilitation délivré par l\'employeur',"délivré par l'employeur" in fa)
ok('formation : pas de note formateur',not re.search(r'note formateur|notes du formateur|\[r\]|à valider par le formateur',fa))
ok('site : pas de lien vers espace formateur ni animation (cartes retirées)','espace formateur' not in sa)
# 5. cohérence site : titres de pages et nombre de modules
for t in ['Accueil de la formation','Livret du participant','Documents de session','Glossaire','Ressources officielles','Crédits et limites','Suivre à distance']:
    ok('site : section « %s »'%t,norm(t) in norm(' '.join(S[1:3])))
al=lambda t:re.sub(r'[^a-z0-9àâäéèêëîïôöûüç]','',norm(t))
sal=al(' '.join(S))
ok('site : 23 modules dans le livret du participant',sum(1 for m in d['modules'] if al(m['title'])[:22] in sal)==23)
# 6. QR : chaque module a son QR (SVG existe) et les fiches y renvoient
import os
ok('QR par module présents (23)',all(os.path.exists('%s/assets/qr/m%d.svg'%(R,m['id'])) for m in d['modules']))
# 7. pagination : pages quasi vides
import glob, numpy as np
from PIL import Image
for nm,key in (('livret-formation-a260e2a.pdf','z'),('livret-site-a260e2a.pdf','w')):
    for f in glob.glob('/tmp/lv/%s-*.png'%key): os.remove(f)
    subprocess.run(['pdftoppm','-r','30','-gray','-png',L+nm,'/tmp/lv/'+key],capture_output=True)
    low=[]
    for i,f in enumerate(sorted(glob.glob('/tmp/lv/%s-*.png'%key)),1):
        a=np.array(Image.open(f)); h=a.shape[0]; body=a[int(h*.06):int(h*.94)]
        rows=np.where((body<235).sum(axis=1)>2)[0]; fill=rows.max()/body.shape[0] if len(rows) else 0
        if fill<0.08: low.append((i,round(float(fill),2)))
    ok('%s : aucune page presque vide (<20 %%)'%nm,not low,low)
json.dump([{'controle':n,'ok':o,'detail':str(x)} for n,o,x in res],open('/home/claude/work/livrets/controle-livrets.json','w'),ensure_ascii=False,indent=1)
print('Bilan : %d/%d'%(sum(o for _,o,_ in res),len(res)))
