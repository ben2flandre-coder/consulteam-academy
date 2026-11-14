import os, re, io, sys, json
sys.path.insert(0,'/home/claude/work/src')
from playwright.sync_api import sync_playwright
from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
import pdfplumber
import livrets as LV
R='/home/claude/work/a260e2a'; OUT='/home/claude/work/livrets'
PAGES=[('index.html','Accueil de la formation'),('livret.html','Livret du participant : les 23 modules'),('documents.html','Documents de session'),('glossaire.html','Glossaire'),('ressources.html','Ressources officielles'),('credits.html','Crédits et limites'),('suivre.html','Suivre à distance ou hors ligne')]
PRINT_CSS='''
@page{size:A4;margin:17mm 14mm 17mm 14mm}
html{-webkit-print-color-adjust:exact;print-color-adjust:exact}
*{font-feature-settings:"calt" 0,"case" 0;font-variant-ligatures:none}
header.top,nav,footer,.fab,.flogo,.cta,.hint,.skip,button,.ctl,#installbtn,.toolbar,[data-noprint]{display:none!important}
body{background:#fff!important}
main{max-width:none!important;padding:0!important;margin:0!important}
.card,.fiche,figure,table,.callout,tr,.mod,.jour,.defi,.adiband,.band,.herox,.fiche,.doc,.gr>*,.grid>*,.note,.gal>*,.k3,li{break-inside:avoid}
.herox,.adiband,.defi{margin-bottom:6mm}
h1,h2,h3{break-after:avoid}
details{display:block}details>*{display:block}
img{max-width:100%}
'''
def cover(title,kick):
    return ('<!doctype html><html lang="fr"><head><meta charset="utf-8"><style>%s</style></head><body>'
      '<section class="cover"><div class="bandes"></div><div class="in"><img class="logo" src="assets/img/logo-consulteam-groupe.png"><div class="kick">%s · %s</div><h1>%s</h1><div class="sub">%s</div></div><div class="when"><b>%s</b><br>%s</div><div class="qr"><img src="assets/qr/home.svg"><b>Le site de la formation</b></div><div class="legal">Conception et ingénierie pédagogique : Benoît Deflandre · Contact et informations : formation@consul-team.fr · %s</div></section></body></html>'
      % (LV.CSS,kick,LV.CODE,title,LV.SOUS,LV.DATES,LV.LIEU,LV.EDITION))
def sommaire(rows):
    li=''.join('<li><span class="n" style="background:%s">%d</span><span class="l">%s</span><span class="p">%s</span></li>'%(LV.COLORS[i%10],i+1,t,p) for i,(t,p) in enumerate(rows))
    return '<!doctype html><html lang="fr"><head><meta charset="utf-8"><style>%s@page{size:A4;margin:17mm 14mm}</style></head><body><div class="kicker">Dans ce livret</div><h2 class="t">Sommaire</h2><ul class="toc">%s</ul><p style="margin-top:8mm;color:#53657a;font-size:9pt">Document de la formation. Liens, QCM, arbres de décision et visuels interactifs : consulter le site en ligne, %s</p></body></html>'%(LV.CSS,li,LV.BASE.replace('https://',''))
def pdfof(pg,url,html=None,print_css=True,zoom=1.0):
    if html is not None:
        tmp=R+'/_t.html'; open(tmp,'w',encoding='utf-8').write(html); url='file://'+tmp
    pg.goto(url); pg.wait_for_timeout(1200)
    if print_css:
        pg.add_style_tag(content=PRINT_CSS+('html{zoom:%s}'%zoom if zoom!=1.0 else ''))
        pg.evaluate('''()=>{document.querySelectorAll('a[href*="animation.html"],a[href*="formateur.html"]').forEach(a=>{var c=a.closest('.card,.k3,li,.fab')||a;c.remove()});document.querySelectorAll('h2').forEach(h=>{if(/^Animer/.test(h.textContent.trim())){var n=h.nextElementSibling;if(n&&!n.children.length)h.remove();}})}''')
    pg.emulate_media(media='print')
    b=pg.pdf(prefer_css_page_size=True,print_background=True)
    if html is not None: os.remove(tmp)
    return PdfReader(io.BytesIO(b))
def stamp(reader_pages,title,n_cover):
    N=len(reader_pages); w=PdfWriter()
    for i,p in enumerate(reader_pages):
        if i==0 or i==N-1 and False:
            w.add_page(p); continue
        buf=io.BytesIO(); c=canvas.Canvas(buf,pagesize=A4); W,H=A4
        c.setFont('Helvetica-Bold',6.5); c.setFillColor(HexColor('#53657a')); c.drawString(14*2.835,H-10*2.835,'LIVRET DU SITE · '+title.upper())
        c.setFillColor(HexColor('#0b68ae')); c.setFont('Helvetica-Bold',7); c.drawRightString(W-14*2.835,H-10*2.835,LV.CODE)
        c.setFillColor(HexColor('#53657a')); c.setFont('Helvetica',7)
        c.drawString(14*2.835,9*2.835,'Consul Team · support pédagogique · '+LV.BASE.replace('https://','').rstrip('/'))
        c.drawRightString(W-14*2.835,9*2.835,'%d / %d'%(i+1,N)); c.save(); buf.seek(0)
        p.merge_page(PdfReader(buf).pages[0]); w.add_page(p)
    return w
with sync_playwright() as pw:
    b=pw.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
    pg=b.new_page(viewport=dict(width=1100,height=1400))
    cov=pdfof(pg,None,cover('Livret du site','LIVRET DU SITE'),False)
    blocks=[]
    for f,t in PAGES:
        r=None
        for z in (1.0,0.96,0.92,0.88,0.84):
            r=pdfof(pg,'file://%s/%s'%(R,f),zoom=z)
            b_=io.BytesIO(); w_=PdfWriter()
            for p_ in r.pages: w_.add_page(p_)
            w_.write(b_); b_.seek(0)
            with pdfplumber.open(b_) as P_:
                last=P_.pages[-1]; bot=max([c['bottom'] for c in last.chars] or [0])/last.height
            if len(r.pages)==1 or bot>=0.2: break
        blocks.append((t,r)); print(f,len(r.pages),'zoom',z,'bas dernière page',round(bot,2))
    # sommaire à deux passes
    def assemble(nums):
        som=pdfof(pg,None,sommaire([(t,nums.get(t,'')) for t,_ in blocks]),False)
        pages=list(cov.pages)+list(som.pages)
        start={}
        for t,r in blocks: start[t]=len(pages)+1; pages+=list(r.pages)
        return pages,start
    def vide(r):
        for pg_ in r.pages:
            pass
        return False
    import pdfplumber as _pp
    for t,r in list(blocks):
        keep=[]
        buf=io.BytesIO(); w0=PdfWriter()
        for p_ in r.pages: w0.add_page(p_)
        w0.write(buf); buf.seek(0)
        with _pp.open(buf) as P0:
            for p_,q_ in zip(r.pages,P0.pages):
                if len((q_.extract_text() or '').strip())<4 and not q_.images: continue
                keep.append(p_)
        r.__dict__['_keep']=keep
    blocks=[(t,type('R',(),{'pages':r._keep})()) for t,r in blocks]
    pages,start=assemble({})
    pages,start2=assemble(start)
    w=stamp(pages,'Habilitation électrique · formation initiale',1)
    w.add_metadata({'/Title':'Livret du site — A260E2A','/Author':'Consulteam · Benoît Deflandre'})
    w.write(OUT+'/site.pdf'); print(len(pages),'pages')
    b.close()
