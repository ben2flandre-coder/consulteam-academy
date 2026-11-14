import sys,glob,os,json,hashlib
from playwright.sync_api import sync_playwright
D='/home/claude/work/a260e2a/images/schemas'
os.makedirs('/tmp/svgpng',exist_ok=True)
rep={}
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
    for f in sorted(glob.glob(D+'/*.svg')):
        pg=b.new_page(viewport={'width':960,'height':700})
        pg.goto('file://'+f)
        r=pg.evaluate("""()=>{const svg=document.documentElement;const vb=svg.viewBox.baseVal;
          const T=[...svg.querySelectorAll('text')].map(t=>{const b=t.getBBox();return{t:t.textContent,x:b.x,y:b.y,w:b.width,h:b.height}});
          const out=T.filter(b=>b.x<0||b.y<0||b.x+b.w>vb.width||b.y+b.h>vb.height).map(b=>b.t);
          const ov=[];for(let i=0;i<T.length;i++)for(let j=i+1;j<T.length;j++){const a=T[i],c=T[j];
            const ix=Math.min(a.x+a.w,c.x+c.w)-Math.max(a.x,c.x),iy=Math.min(a.y+a.h,c.y+c.h)-Math.max(a.y,c.y);
            if(ix>2&&iy>2)ov.push([a.t,c.t]);}
          return{w:vb.width,h:vb.height,nb_textes:T.length,hors_cadre:out,chevauchements:ov}}""")
        png='/tmp/svgpng/'+os.path.basename(f).replace('.svg','.png')
        pg.screenshot(path=png,clip={'x':0,'y':0,'width':r['w'],'height':r['h']})
        r['png_sha256']=hashlib.sha256(open(png,'rb').read()).hexdigest()
        r['svg_sha256']=hashlib.sha256(open(f,'rb').read()).hexdigest()
        rep[os.path.basename(f)]=r
        pg.close()
    b.close()
json.dump(rep,open('/home/claude/work/a260e2a/preuves/validation-svg.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
for k,v in rep.items(): print(k,v['nb_textes'],'hors cadre:',v['hors_cadre'],'chevauch.:',v['chevauchements'])
