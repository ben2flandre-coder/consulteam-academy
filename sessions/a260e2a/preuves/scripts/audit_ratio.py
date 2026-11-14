# Contrôle du ratio ED 6127 (§ évaluation des savoirs) : QCM de 15 questions minimum, base d'au moins 5 fois plus de questions par thème.
import re,json,sys
R=sys.argv[1] if len(sys.argv)>1 else '/home/claude/work/a260e2a'
t=open(R+'/data/content.js',encoding='utf-8').read()
A=json.loads(re.match(r'window\.A=(.*?);\s*(window\.|$)',t,re.S).group(1))
C=A['evals_cfg']; n=C['n']; k=n//4
mq={m['id']:{q['id'] for q in m['questions']} for m in A['modules']}
def pool(ids): return set().union(*[mq[i] for i in ids])
themes={'dangers':pool(C['dangers']),'zones':pool(C['zones']),'protections':pool(C['protec'])}
res={'qcm_questions':n,'minimum_ed6127':15,'ok_taille':n>=15,'tirage_par_theme':k,'themes':{},'niveaux':{},'defauts':[]}
for th,p in themes.items():
    res['themes'][th]=dict(base=len(p),exigence=5*k,ok=len(p)>=5*k)
    if len(p)<5*k: res['defauts'].append(th)
for e in A['evals']:
    p=pool(e['modules']); res['niveaux'][e['id']]=dict(titre=e['titre'],base_limites=len(p),exigence=5*k,ok=len(p)>=5*k)
    if len(p)<5*k: res['defauts'].append(e['id'])
json.dump(res,open(R+'/preuves/controle-ratio-questions.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(json.dumps({'n':n,'defauts':res['defauts'],'themes':res['themes'],'niveaux':{k:v['base_limites'] for k,v in res['niveaux'].items()},'total':sum(len(v) for v in mq.values())},ensure_ascii=False))
