"""Contrôle des éditions, liens et questions communes. Ne certifie aucun geste."""
from pathlib import Path
import json,re,subprocess,unicodedata
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parents[1]
def norm(s):return ''.join(c for c in unicodedata.normalize('NFKD',s).lower() if c.isalnum())
def read(p):return (ROOT/p).read_text(encoding='utf-8')
pdf=PdfReader(str(ROOT/'pdf/livret-formation-260053a.pdf'))
pdftext=' '.join(p.extract_text() for p in pdf.pages)
book=read('livret.html')
questions=json.loads(subprocess.check_output(['node','-e',"global.window={};require('./js/qcm-data.js');process.stdout.write(JSON.stringify(window.QCM));"],cwd=ROOT,text=True,encoding='utf-8'))
results=[]
def check(label,ok):results.append({'controle':label,'conforme':bool(ok)})
check('Livret PDF : 32 pages',len(pdf.pages)==32)
check('Livret HTML : 32 sections paginées',len(re.findall(r'<section[^>]*class="[^"]*page',book))==32)
check('Version 2.1 indiquée dans le PDF et le HTML','version 2.1' in pdftext.lower() and 'version 2.1' in book.lower())
check('Pagination PDF n / 32',all(f'{n} / 32' in pdf.pages[n-1].extract_text() for n in range(2,32)))
check('Dix questions communes',len(questions)==10)
for i,q in enumerate(questions):
 check('QCM '+str(i+1)+' : énoncé présent dans le PDF',norm(q['q']) in norm(pdftext))
 check('QCM '+str(i+1)+' : réponse juste présente dans le PDF',norm(q['o'][q['a']]) in norm(pdftext))
for p in ['index.html','apprenants.html','apprenant.html']:
 check(p+' : libellé courant 32 pages', '32 pages' in read(p) and '28 pages' not in read(p))
check('67 vues de projection : 57 statiques + 10 QCM',len(re.findall(r'<section[^>]*class="slide\b',read('animation.html')))==57)
check('Source du QCM partagée par cours et projection',all('js/qcm-data.js' in read(p) for p in ['animation.html','apprenant.html']))
check('Périmètre de session inchangé',all('260053A' in read(p) for p in ['index.html','programme.html','livret.html']))
report={'date':'2026-11-28','edition':'2.1','resultats':results,'limite':'Contrôle éditorial automatisé ciblé ; la concordance technique complète fait aussi l’objet d’une revue documentaire et la pratique reste soumise au contrôle humain.'}
(ROOT/'qa/coherence-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'controles':len(results),'echecs':[x['controle'] for x in results if not x['conforme']]},ensure_ascii=True))
assert all(x['conforme'] for x in results)
