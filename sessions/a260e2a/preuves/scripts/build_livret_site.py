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
def pdfof(pg,url,html=None,print_css=True):
    if html is not None:
        tmp=R+'/_t.html'; open(tmp,'w',encoding='utf-8').write(html); url='file://'+tmp
    pg.goto(url); pg.wait_for_timeout(1200)
    if print_css:
        pg.add_style_tag(content=PRINT_CSS)
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
        r=pdfof(pg,'file://%s/%s'%(R,f)); blocks.append((t,r)); print(f,len(r.pages))
    # sommaire à deux passes
    def assemble(nums):
        som=pdfof(pg,None,sommaire([(t,nums.get(t,'')) for t,_ in blocks]),False)
        pages=list(cov.pages)+list(som.pages)
        start={}
        for t,r in blocks: start[t]=len(pages)+1; pages+=list(r.pages)
        return pages,start
    pages,start=assemble({})
    pages,start2=assemble(start)
    w=stamp(pages,'Habilitation électrique · formation initiale',1)
    w.add_metadata({'/Title':'Livret du site — A260E2A','/Author':'Consulteam · Benoît Deflandre'})
    w.write(OUT+'/site.pdf'); print(len(pages),'pages')
    b.close()
