"""Livret A4 portrait : même contenu éditorial en HTML et PDF.

Python : reportlab, Pillow, pypdf. Polices Segoe UI et Georgia (Windows),
ou dossier de polices fourni via LIVRET_FONT_DIR. Aucun téléchargement.
"""
from pathlib import Path
from html import escape
import os,json,re
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.utils import ImageReader
from reportlab.platypus import Paragraph,Table,TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.graphics.barcode.qr import QrCodeWidget
from reportlab.graphics.shapes import Drawing
from reportlab.graphics import renderPDF
from pypdf import PdfReader
from PIL import Image,ImageOps,ImageDraw
from livret_content import ROOT,PAGES

URL='https://ben2flandre-coder.github.io/consulteam-academy/sessions/260053a/apprenants.html?e=p'
W,H=595.276,841.89
N=len(PAGES)+2
NAVY=colors.HexColor('#102c53');BLUE=colors.HexColor('#0b68ae');AMBER=colors.HexColor('#f6b63d');INK=colors.HexColor('#1b2a3c');MUTED=colors.HexColor('#5a6b7e');PALE=colors.HexColor('#f4f6f9');LINE=colors.HexColor('#d3dbe5')
FONT=Path(os.environ.get('LIVRET_FONT_DIR','C:/Windows/Fonts'))
for name,file in [('Sans','segoeui.ttf'),('SansB','segoeuib.ttf'),('Serif','georgia.ttf'),('SerifB','georgiab.ttf'),('SerifI','georgiai.ttf')]:pdfmetrics.registerFont(TTFont(name,str(FONT/file)))
pdfmetrics.registerFontFamily('Serif',normal='Serif',bold='SerifB',italic='SerifI',boldItalic='SerifB')
pdfmetrics.registerFontFamily('Sans',normal='Sans',bold='SansB',italic='Sans',boldItalic='SansB')
STYLES={
 'p':ParagraphStyle('p',fontName='Serif',fontSize=10,leading=14,textColor=INK,spaceAfter=7),
 'h':ParagraphStyle('h',fontName='SansB',fontSize=11,leading=14,textColor=NAVY,spaceAfter=6,spaceBefore=5),
 'small':ParagraphStyle('small',fontName='Sans',fontSize=7.6,leading=10,textColor=MUTED,spaceAfter=6),
 'cell':ParagraphStyle('cell',fontName='Sans',fontSize=9,leading=12,textColor=INK),
 'th':ParagraphStyle('th',fontName='SansB',fontSize=8.6,leading=11,textColor=colors.white),
 'title':ParagraphStyle('title',fontName='SansB',fontSize=25,leading=28,textColor=NAVY),
 'lead':ParagraphStyle('lead',fontName='SerifI',fontSize=11,leading=15,textColor=MUTED),
}
REPORT=[]
def para(c,text,x,y,w,kind='p'):
    q=Paragraph(text,STYLES[kind]);_,height=q.wrap(w,1000);q.drawOn(c,x,y-height)
    return y-height-STYLES[kind].spaceAfter
def qr(c,x,y,size):
    q=QrCodeWidget(URL);a,b,d,e=q.getBounds();draw=Drawing(size,size,transform=[size/(d-a),0,0,size/(e-b),0,0]);draw.add(q);renderPDF.draw(draw,c,x,y)
def cover(c,back=False):
    c.setFillColor(NAVY);c.rect(0,0,W,H,fill=1,stroke=0);c.setFillColor(AMBER);c.rect(0,0,19,H,fill=1,stroke=0)
    c.drawImage(str(ROOT/'assets/img/logo-consulteam-blanc.png'),62,748,width=177,height=38,preserveAspectRatio=True,mask='auto')
    if not back:
        c.setStrokeColor(colors.HexColor('#4a5350'));c.setLineWidth(8);c.circle(512,285,166,stroke=1,fill=0);c.setStrokeColor(colors.HexColor('#2e486b'));c.setLineWidth(5);c.circle(512,285,110,stroke=1,fill=0)
        c.setFillColor(AMBER);c.setFont('SansB',9);c.drawString(62,568,'LIVRET DE FORMATION APPRENANT · 260053A')
        style=ParagraphStyle('cover',fontName='SansB',fontSize=32,leading=35,textColor=colors.white)
        q=Paragraph('Travail en hauteur<br/>et port du harnais',style);q.wrap(470,160);q.drawOn(c,62,480)
        c.setFillColor(colors.HexColor('#cfe0f4'));c.setFont('Serif',13);c.drawString(62,448,'Prévenir · contrôler · pratiquer · préparer le secours')
        c.setFillColor(colors.white);c.setFont('SansB',11)
        for i,t in enumerate(['Formation présentielle · 7 h','Lundi 30 novembre 2026','Consulteam Security · La Seyne-sur-Mer']):c.drawString(62,180-i*17,t)
        q=Paragraph('Conception et ingénierie pédagogique : Benoît Deflandre · Contact : formation@consul-team.fr<br/>Édition du 28/11/2026 · version 2.0 · validation Consulteam en attente',ParagraphStyle('footC',fontName='Sans',fontSize=7,leading=10,textColor=colors.HexColor('#a9c4e4')));q.wrap(470,60);q.drawOn(c,62,59)
    else:
        c.setFillColor(colors.white);c.roundRect(62,519,136,136,8,fill=1,stroke=0);qr(c,65,522,130)
        c.setFont('SansB',19);c.drawString(62,480,'Pour aller plus loin')
        q=Paragraph('Le site de la formation : fiches, nœuds, animations, vidéos et auto-évaluation.<br/>Scanner le QR code ou ouvrir le lien ci-dessous.',ParagraphStyle('back',fontName='Sans',fontSize=11,leading=16,textColor=colors.HexColor('#cfe0f4')));q.wrap(460,70);q.drawOn(c,62,423)
        c.setFillColor(AMBER);c.setFont('SansB',10);c.drawString(62,398,'Accéder à mon espace apprenant');c.linkURL(URL,(62,391,440,413),relative=0)
        c.setFillColor(colors.HexColor('#cfe0f4'));c.setFont('Sans',8);c.drawString(62,377,'ben2flandre-coder.github.io/consulteam-academy/sessions/260053a/')
        for i,n in enumerate([8,13]):
            thumb=ROOT/'qa/render-livret'/('page-%02d.png'%n)
            if thumb.exists():c.drawImage(str(thumb),62+i*135,144,width=112,height=158,preserveAspectRatio=True,mask='auto')
        q=Paragraph('Support pédagogique : les textes en vigueur, les notices et les consignes du site prévalent.<br/>Consulteam Groupe · SECU37 · 260053A · Benoît Deflandre · formation@consul-team.fr',ParagraphStyle('backfoot',fontName='Sans',fontSize=7.2,leading=11,textColor=colors.HexColor('#a9c4e4')));q.wrap(470,60);q.drawOn(c,62,60)
    c.setFont('Sans',7);c.setFillColor(colors.HexColor('#a9c4e4'));c.drawRightString(W-28,19,str(N if back else 1)+' / '+str(N))
def block(c,b,x,y,w):
    kind=b['type']
    if kind in ['p','h']:return para(c,b['text'],x,y,w,kind)
    if kind=='list' or kind=='options':
        for item in b['items']:
            if kind=='options':c.setStrokeColor(NAVY);c.setLineWidth(.7);c.rect(x+1,y-10,7,7,stroke=1,fill=0)
            else:c.setFillColor(BLUE);c.circle(x+4,y-6.5,1.7,fill=1,stroke=0)
            y=para(c,item,x+15,y,w-15)
        return y-2
    if kind=='alert':
        q=Paragraph(b['text'],STYLES['p']);_,hh=q.wrap(w-23,1000);height=hh+18
        c.setFillColor(colors.HexColor('#fff6dd'));c.rect(x,y-height,w,height,fill=1,stroke=0);c.setFillColor(AMBER);c.rect(x,y-height,4,height,fill=1,stroke=0);q.drawOn(c,x+12,y-9-hh)
        return y-height-11
    if kind=='table':
        rows=[[Paragraph(escape(s),STYLES['th']) for s in b['headers']]]+[[Paragraph(escape(str(s)),STYLES['cell']) for s in r] for r in b['rows']]
        ratios=([.33,.67] if len(b['headers'])==2 else [.3,.35,.35]);t=Table(rows,colWidths=[w*r for r in ratios],hAlign='LEFT')
        t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),NAVY),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,PALE]),('LINEBELOW',(0,1),(-1,-1),.4,LINE),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7)]))
        _,height=t.wrap(w,1000);t.drawOn(c,x,y-height);return y-height-12
    if kind=='notes':
        y=para(c,b['label'],x,y,w,'h');c.setStrokeColor(LINE);c.setLineWidth(.5)
        for i in range(b['lines']):y-=17;c.line(x,y,x+w,y)
        return y-14
    if kind=='image':
        file=ROOT/b['file'];im=Image.open(file);iw,ih=im.size;scale=min(w/iw,b['height']/ih);dw,dh=iw*scale,ih*scale
        c.drawImage(str(file),x+(w-dw)/2,y-dh,dw,dh,mask='auto');y-=dh+7
        return para(c,b['caption'],x,y,w,'small')-4
    if kind=='link':
        y=para(c,'<b>'+escape(b['text'])+'</b>',x,y,w,'p');y=para(c,'<link href="'+escape(b['url'],quote=True)+'" color="#0b68ae">'+escape(b['url'])+'</link>',x,y,w,'small');return y-4
    raise ValueError(kind)
def build_pdf():
    path=ROOT/'pdf/livret-formation-260053a.pdf';c=canvas.Canvas(str(path),pagesize=(W,H),pageCompression=1)
    c.setTitle('Livret de formation apprenant · Travail en hauteur et port du harnais · 260053A');c.setAuthor('Benoît Deflandre · Consulteam Groupe');c.setSubject('Fiches, ateliers au sol, notes et plan d’action · version 2.0')
    cover(c);c.showPage()
    for n,page in enumerate(PAGES,2):
        c.bookmarkPage('page'+str(n));c.addOutlineEntry(page['title'],'page'+str(n),0,False)
        x=46;w=W-92;y=785
        c.setFillColor(MUTED);c.setFont('SansB',7);c.drawString(x,H-24,'LIVRET DE FORMATION APPRENANT · TRAVAIL EN HAUTEUR');c.setFillColor(BLUE);c.drawRightString(W-46,H-24,'260053A')
        c.setFillColor(BLUE);c.setFont('SansB',8);c.drawString(x,y,page['kicker'].upper());y-=18
        y=para(c,page['title'],x,y,w,'title')-8;y=para(c,page['lead'],x,y,w,'lead')-10
        c.setFillColor(AMBER);c.rect(x,y,85,3,fill=1,stroke=0);y-=16
        for b in page['blocks']:y=block(c,b,x,y,w)
        REPORT.append({'page':n,'title':page['title'],'bottom':round(y,2),'overflow':y<52})
        if y<52:raise ValueError('Débordement page '+str(n)+' '+page['title']+' : '+str(y))
        c.setStrokeColor(LINE);c.setLineWidth(.5);c.line(x,39,W-46,39)
        c.setFont('Sans',7);c.setFillColor(MUTED);c.drawString(x,26,'Livret de formation apprenant · 260053A · Consulteam · version 2.0');c.drawRightString(W-46,26,str(n)+' / '+str(N));c.showPage()
    cover(c,True);c.save();return path

def html_block(b):
    t=b['type']
    if t in ['p','h']:return '<'+('p' if t=='p' else 'h3')+'>'+b['text']+'</'+('p' if t=='p' else 'h3')+'>'
    if t in ['list','options']:return '<ul class="'+t+'">'+''.join('<li>'+('□ ' if t=='options' else '')+s+'</li>' for s in b['items'])+'</ul>'
    if t=='table':return '<table><thead><tr>'+''.join('<th>'+escape(s)+'</th>' for s in b['headers'])+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+escape(str(s))+'</td>' for s in r)+'</tr>' for r in b['rows'])+'</tbody></table>'
    if t=='alert':return '<p class="warn">'+b['text']+'</p>'
    if t=='notes':return '<div class="notes"><h3>'+b['label']+'</h3><div style="height:'+str(b['lines']*6)+'mm"></div></div>'
    if t=='image':return '<figure><img src="'+b['file']+'" style="max-height:'+str(b['height']/2.83465)+'mm" alt="'+escape(b['caption'],quote=True)+'"><figcaption>'+b['caption']+'</figcaption></figure>'
    if t=='link':return '<p class="source"><b>'+b['text']+'</b><br><a href="'+escape(b['url'],quote=True)+'">'+escape(b['url'])+'</a></p>'
def build_html():
    css=(Path(__file__).parent/'livret-style.css').read_text(encoding='utf-8');(ROOT/'css/livret.css').write_text(css,encoding='utf-8')
    coverhtml='<section class="lv-page lv-cover"><div class="cbar"></div><img class="cover-logo" src="assets/img/logo-consulteam-blanc.png" alt="Consulteam Groupe"><div class="cover-main"><p class="kick">Livret de formation apprenant · 260053A</p><h1>Travail en hauteur<br>et port du harnais</h1><p>Prévenir · contrôler · pratiquer · préparer le secours</p></div><div class="cover-meta"><b>Formation présentielle · 7 h<br>Lundi 30 novembre 2026<br>Consulteam Security · La Seyne-sur-Mer</b><small>Conception et ingénierie pédagogique : Benoît Deflandre · formation@consul-team.fr<br>Version 2.0 du 28/11/2026 · validation Consulteam en attente</small></div><span class="pn">1 / '+str(N)+'</span></section>'
    sections=[]
    for n,pg in enumerate(PAGES,2):sections.append('<section class="lv-page" id="page-'+str(n)+'"><header>LIVRET DE FORMATION APPRENANT <span>260053A</span></header><p class="kick">'+pg['kicker']+'</p><h2>'+pg['title']+'</h2><p class="lead">'+pg['lead']+'</p><div class="amber"></div>'+''.join(html_block(b) for b in pg['blocks'])+'<footer>Livret de formation apprenant · 260053A · Consulteam · version 2.0<span>'+str(n)+' / '+str(N)+'</span></footer></section>')
    back='<section class="lv-page lv-cover lv-back"><div class="cbar"></div><img class="cover-logo" src="assets/img/logo-consulteam-blanc.png" alt="Consulteam Groupe"><div class="back-main"><img class="qr" src="assets/img/qr-apprenants.svg" alt="QR code de l’espace apprenant"><h2>Pour aller plus loin</h2><p>Fiches, nœuds, animations, vidéos et auto-évaluation.</p><a href="'+URL+'">Accéder à mon espace apprenant</a><div class="previews"><img src="assets/img/livret-apercu-1.jpg" alt="Aperçu de la fiche de contrôle"><img src="assets/img/livret-apercu-2.jpg" alt="Aperçu de la fiche cabestan"></div></div><div class="cover-meta"><small>Les textes en vigueur, les notices et les consignes du site prévalent sur cet aide-mémoire.<br>Consulteam Groupe · SECU37 · Benoît Deflandre · formation@consul-team.fr</small></div><span class="pn">'+str(N)+' / '+str(N)+'</span></section>'
    html='<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>Livret apprenant · 260053A · Travail en hauteur</title><link rel="stylesheet" href="css/livret.css?v=2.0"></head><body><nav class="lv-bar" aria-label="Livret"><a href="pdf/livret-formation-260053a.pdf" download>Télécharger le PDF</a><button type="button" onclick="window.print()">Imprimer</button><a href="apprenants.html?e=p">Espace apprenant</a><a href="#page-3">Sommaire</a></nav><main>'+coverhtml+''.join(sections)+back+'</main></body></html>'
    html=html.replace('</head>','<link rel="stylesheet" href="css/pilotage.css?v=2.0.1"></head>').replace('</body>','<script src="js/pilotage.js?v=2.0.1"></script></body>')
    (ROOT/'livret.html').write_text(html,encoding='utf-8')
def render(path):
    import pypdfium2 as pdfium
    out=ROOT/'qa/render-livret';out.mkdir(exist_ok=True)
    doc=pdfium.PdfDocument(str(path));thumbs=[]
    for i in range(len(doc)):
        im=doc[i].render(scale=1.35).to_pil().convert('RGB');im.save(out/('page-%02d.png'%(i+1)))
        th=ImageOps.contain(im,(165,235));tile=Image.new('RGB',(185,260),'#e3e9ef');tile.paste(th,((185-th.width)//2,8));ImageDraw.Draw(tile).text((8,243),str(i+1),fill='#102c53');thumbs.append(tile)
    sheet=Image.new('RGB',(185*7,260*((len(thumbs)+6)//7)),'white')
    for i,th in enumerate(thumbs):sheet.paste(th,((i%7)*185,(i//7)*260))
    sheet.save(out/'contact.png')
    for n,j in [(8,1),(13,2)]:Image.open(out/('page-%02d.png'%n)).resize((360,509)).save(ROOT/('assets/img/livret-apercu-'+str(j)+'.jpg'),quality=88)
    # Le QR est vectoriel, créé avec le même encodeur que celui du PDF.
    from reportlab.graphics import renderSVG
    q=QrCodeWidget(URL);a,b,d,e=q.getBounds();dr=Drawing(180,180,transform=[180/(d-a),0,0,180/(e-b),0,0]);dr.add(q);renderSVG.drawToFile(dr,str(ROOT/'assets/img/qr-apprenants.svg'))

if __name__=='__main__':
    pdf=build_pdf();render(pdf);REPORT.clear();pdf=build_pdf();render(pdf);build_html()
    reader=PdfReader(str(pdf));assert len(reader.pages)==N
    text='\n'.join(pg.extract_text() for pg in reader.pages)
    assert '\ufffd' not in text
    for n in range(2,N):assert str(n)+' / '+str(N) in reader.pages[n-1].extract_text()
    report={'pages':N,'bytes':pdf.stat().st_size,'format':'A4 portrait','overflow':[],'page_layout':REPORT,'fonts':'Segoe UI et Georgia incorporées','html':'livret.html','pdf':'pdf/livret-formation-260053a.pdf'}
    (ROOT/'qa/livret-layout.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k!='page_layout'},ensure_ascii=True))
