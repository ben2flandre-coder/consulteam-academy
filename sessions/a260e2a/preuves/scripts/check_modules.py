import re,json,csv,sys,hashlib
sys.path.insert(0,'/home/claude/work/src')
import modules_tb as T, sources_new as SN, modules_ed6127 as E6
T.MODULES=T.MODULES+E6.MODULES; T.VALEURS={**T.VALEURS,**E6.VALEURS}
import q_complements as QCx
QCx.declare(T.VALEURS)
for _m in T.MODULES:
    _m['questions']=list(_m['questions'])+QCx.QC.get(_m['id'],[])
import adi
for _i,_c in adi.CHEZ.items():
    T.MODULES.append(dict(id=str(_i)+'-ADI',title='Chez ADI',goal='',scenario='',decision='',answer='',source='',note='',check=[],sections=[_c['sec']],questions=list(_c['qs'])))
OUT='/home/claude/work/a260e2a/preuves'
ids={s['id'] for s in SN.SOURCES}
def strip(s):
    s=re.sub(r'NF C \d+-\d+','',s); s=re.sub(r'§\s?[\d.]+','',s); s=re.sub(r'pp?\. [\d, -]+','',s); s=re.sub(r'\bED \d+','',s); s=re.sub(r'\b[BH][0-2][VTNX]?\b','',s); s=re.sub(r'\b[SFTCR]\d+(?:[, ]+S\d+)*\b','',s); return s
tok=lambda s:re.findall(r'\d+(?:,\d+)?',strip(s))
rows=[];bad=[];used=set()
def stmts(m):
    for t,x in m['sections']: yield 'section : '+t,x
    yield 'situation',m['scenario']; yield 'réponse',m['answer']
    for q in m['questions']: yield 'question '+q['id']+' (explication)',q['why']
    for k,q in enumerate(m.get('exercices',[]),1): yield 'exercice '+str(k)+' (explication)',q['why']
for m in T.MODULES:
    texts=[m['title'],m['goal'],m['scenario'],m['decision'],m['answer'],m['source'],m['note']]+m['check']+[f[1] for f in m.get('figures',[])]
    texts+= [s[0]+' '+s[1] for s in m['sections']]
    for q in m['questions']+m.get('exercices',[]): texts+= [q['q'],q['why']]+q['options']
    for s in texts:
        for k in tok(s):
            used.add(k)
            if k not in T.VALEURS: bad.append((m['id'],k,s[:80]))
    for loc,x in stmts(m):
        for sent in re.split(r'(?<=[.!?])\s+',x):
            if not sent.strip(): continue
            refs=re.findall(r'\[([^\]]+)\]',sent)
            cited=sorted({r for g in refs for r in re.findall(r'S\d+',g)})
            lv=[l for l in 'CR' if any(l in g.split(',')[-1].strip() or re.fullmatch(r'\s*'+l+r'\s*',g) for g in refs) or any(re.search(r'(^|[ ,])'+l+r'($|[ ,])',g) for g in refs)]
            unknown=[c for c in cited if c not in ids]
            rows.append([m['id'],loc,sent.strip(),' '.join(cited),''.join(sorted(set(lv))) or ('S' if cited else ''),'OK' if (refs and not unknown) or loc.startswith('situation') else 'SANS REFERENCE'+(' '+','.join(unknown) if unknown else '')])
    for i in re.findall(r'\[(S\d+)',json.dumps(m,ensure_ascii=False)):
        if i not in ids: bad.append((m['id'],'source inconnue '+i,''))
w=csv.writer(open(OUT+'/matrice-affirmations-sources.csv','w',encoding='utf-8-sig',newline=''),delimiter=';')
w.writerow(['module','emplacement','affirmation','sources','niveau (S source / C calcul / R principe)','statut']); w.writerows(rows)
unused=sorted(set(T.VALEURS)-used)
res=dict(modules=[m['id'] for m in T.MODULES],affirmations=len(rows),sans_reference=sum(r[5].startswith('SANS') for r in rows),jetons_non_declares=bad,jetons_declares_inutilises=unused,
  valeurs={k:list(v) for k,v in T.VALEURS.items()})
json.dump(res,open(OUT+'/controle-valeurs-chiffrees.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(json.dumps({k:res[k] for k in ('affirmations','sans_reference','jetons_non_declares','jetons_declares_inutilises')},ensure_ascii=False,indent=1))
for r in rows:
    if r[5].startswith('SANS'): print(r[0],r[1],'|',r[2][:110])
