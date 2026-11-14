# Parcours des trois arbres « Puis-je remplacer ? » : chaque chemin possible mène à une issue, aucun nœud orphelin.
import json,re,sys
from playwright.sync_api import sync_playwright
root=sys.argv[1] if len(sys.argv)>1 else 'http://localhost:8765'
res={'chemins':0,'issues':{},'erreurs':[]}
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox']); pg=b.new_page()
    pg.on('pageerror',lambda e:res['erreurs'].append(str(e)))
    pg.goto(root+'/remplacer.html'); pg.wait_for_selector('#arb')
    N=pg.evaluate('NODES'); R=pg.evaluate('RES'); S=pg.evaluate('START')
    def walk(i,path):
        if i in R:
            res['chemins']+=1; res['issues'][R[i]['k']]=res['issues'].get(R[i]['k'],0)+1; return
        if i not in N: res['erreurs'].append('nœud manquant '+i); return
        for lab,nx in N[i]['o']:
            if nx.startswith(('DO_',)):
                if nx not in R: res['erreurs'].append('issue manquante '+nx)
                res['chemins']+=1; res['issues']['do']=res['issues'].get('do',0)+1; continue
            walk(nx,path+[nx])
    for lab,st in S: walk(st,[st])
    # clic réel : lampe, tout « oui » jusqu'à l'issue
    pg.click('text=Remplacer une lampe')
    for _ in range(8):
        btns=pg.query_selector_all('#arb .opts button')
        if not btns: break
        btns[0].click()
    res['fin_lampe']=pg.inner_text('#arb h2')
    pg.click('text=Recommencer'); pg.click('text=Remplacer un fusible'); pg.query_selector_all('#arb .opts button')[0].click(); pg.query_selector_all('#arb .opts button')[1].click()
    res['fusible_modif']=pg.inner_text('#arb h2')
    b.close()
print(json.dumps(res,ensure_ascii=False))
