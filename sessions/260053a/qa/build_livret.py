"""Génère le livret depuis les textes HTML courants, sans dépendance externe."""
from pathlib import Path
from html.parser import HTMLParser
import re, json, subprocess, unicodedata
ROOT=Path(__file__).resolve().parents[1]
W,H=841.89,595.28
NAVY=(.031,.169,.271);BLUE=(.029,.357,.608);ROSE=(.702,0,.416);INK=(.067,.184,.263)
class Node:
    def __init__(self,tag='',attrs=(),parent=None):self.tag=tag;self.a=dict(attrs);self.children=[];self.parent=parent
    def text(self):return ' '.join(' '.join(c.text() if isinstance(c,Node) else c for c in self.children).split())
    def all(self,tag):
        for c in self.children:
            if isinstance(c,Node):
                if c.tag==tag:yield c
                yield from c.all(tag)
class Tree(HTMLParser):
    def __init__(self,s):super().__init__();self.root=Node();self.cur=self.root;self.feed(s)
    def handle_starttag(self,t,a):
        n=Node(t,a,self.cur);self.cur.children.append(n)
        if t not in ['area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr']:self.cur=n
    def handle_startendtag(self,t,a):self.handle_starttag(t,a);self.handle_endtag(t)
    def handle_endtag(self,t):
        p=self.cur
        while p.parent and p.tag!=t:p=p.parent
        if p.parent:self.cur=p.parent
    def handle_data(self,d):self.cur.children.append(d)
def normal(s):return s.replace('\u202f',' ').replace('\u00a0',' ').replace('→','').replace('↗','').replace('×','x').replace('≤','<= ').replace('≥','>= ').replace('≠','différent de').replace('☐','[ ]').replace('✓','').replace('✗','').replace('…','...')
def esc(s):return normal(s).encode('cp1252','replace').decode('cp1252').replace('\\','\\\\').replace('(','\\(').replace(')','\\)')
def width(s,size,bold=False):
    narrow='ilI.,:;!\'|';wide='MWmw@%';total=0
    for c in normal(s):
        d=unicodedata.normalize('NFD',c)[0]
        total+=.29 if d in narrow else .86 if d in wide else .29 if d==' ' else .64 if d.isupper() else .56
    return total*size*(1.04 if bold else 1)
def wrap(s,size,maxw,bold=False):
    words=normal(s).split();lines=[];line=''
    for word in words:
        if width(word,size,bold)>maxw:
            chunks=[];part=''
            for char in word:
                if width(part+char,size,bold)>maxw:chunks.append(part);part=char
                else:part+=char
            words2=chunks+[part]
        else:words2=[word]
        for item in words2:
            test=(line+' '+item).strip()
            if line and width(test,size,bold)>maxw:lines.append(line);line=item
            else:line=test
    if line:lines.append(line)
    return lines
class PDF:
    def __init__(self):self.pages=[];self.commands=[];self.col=0;self.y=0;self.chapter='';self.stats=[];self.images={}
    def cmd(self,s):self.commands.append(s)
    def rect(self,x,y,w,h,color):self.cmd('%s rg %.2f %.2f %.2f %.2f re f'%(' '.join(map(str,color)),x,y,w,h))
    def text(self,x,y,s,size=11.2,bold=False,color=INK):
        self.cmd('BT /%s %.2f Tf %s rg 1 0 0 1 %.2f %.2f Tm (%s) Tj ET'%('F2' if bold else 'F1',size,' '.join(map(str,color)),x,y,esc(s)))
        self.stats.append({'page':len(self.pages)+1,'x':x,'y':y,'width':width(s,size,bold),'text':s})
    def page(self,chapter):
        if self.commands:self.pages.append(self.commands)
        self.commands=[];self.chapter=chapter;self.col=0;self.y=490
        self.rect(0,H-53,W,53,NAVY);self.text(32,H-32,'CONSULTEAM  |  TRAVAIL EN HAUTEUR - PORT DU HARNAIS',16,True,(1,1,1))
        self.rect(0,H-57,W,4,ROSE);self.text(32,H-81,chapter,18,True,NAVY)
        self.text(32,23,'SECU37 - 260053A - 30/11/2026 - 7 h - Version 1.8 du 27/11/2026',9,color=BLUE)
        self.text(32,11,'Support en ligne : ben2flandre-coder.github.io/consulteam-academy/sessions/260053a/apprenants.html',7.8,color=BLUE)
        self.text(W-60,23,str(len(self.pages)+1),10,True,NAVY)
    def ensure(self,amount):
        if self.y-amount>=52:return
        if self.col==0:self.col=1;self.y=490
        else:self.page(self.chapter+' (suite)' if not self.chapter.endswith('(suite)') else self.chapter)
    def para(self,s,kind='p'):
        if not s:return
        size=15 if kind=='h2' else 12.5 if kind=='h3' else 11.2
        bold=kind in ['h2','h3'];leading=size*1.4;gap=11 if bold else 7
        lines=wrap(s,size,365,bold);self.ensure(min(len(lines),3)*leading+gap)
        x=32+self.col*405
        if kind=='h2':self.rect(x,self.y+7,32,3,ROSE)
        for line in lines:
            self.ensure(leading);x=32+self.col*405;self.text(x,self.y,line,size,bold,NAVY if bold else INK);self.y-=leading
        self.y-=gap
    def image_page(self,title,path):
        self.page(title);data=path.read_bytes();i=2;w=h=0
        while i<len(data):
            if data[i]!=255:i+=1;continue
            marker=data[i+1];i+=2
            if marker in [216,217]:continue
            n=int.from_bytes(data[i:i+2],'big')
            if marker in [192,193,194]:h=int.from_bytes(data[i+3:i+5],'big');w=int.from_bytes(data[i+5:i+7],'big');break
            i+=n
        if not w:raise ValueError('Invalid JPEG '+str(path))
        name='Im'+str(len(self.images)+1);self.images[name]=(data,w,h)
        scale=min(778/w,420/h);dw,dh=w*scale,h*scale;x=(W-dw)/2;y=70+(420-dh)/2
        self.cmd('q %.2f 0 0 %.2f %.2f %.2f cm /%s Do Q'%(dw,dh,x,y,name))
        self.text(32,52,'Illustration générique : les notices et les textes corrigés du livret restent les références d’emploi.',9,color=BLUE)
    def save(self,path):
        if self.commands:self.pages.append(self.commands);self.commands=[]
        objects=[b'',b'']
        def obj(value):objects.append(value);return len(objects)
        font1=obj(b'<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>')
        font2=obj(b'<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>')
        image_ids={}
        for name,(data,w,h) in self.images.items():
            image_ids[name]=obj(('<< /Type /XObject /Subtype /Image /Width %d /Height %d /ColorSpace /DeviceRGB /BitsPerComponent 8 /Filter /DCTDecode /Length %d >>\nstream\n'%(w,h,len(data))).encode()+data+b'\nendstream')
        xobjects=' /XObject << '+' '.join('/%s %d 0 R'%(name,i) for name,i in image_ids.items())+' >>'
        ids=[]
        for page in self.pages:
            content='\n'.join(page).encode('cp1252');sid=obj(b'<< /Length '+str(len(content)).encode()+b' >>\nstream\n'+content+b'\nendstream')
            pid=obj(('<< /Type /Page /Parent 2 0 R /MediaBox [0 0 %.2f %.2f] /Resources << /Font << /F1 %d 0 R /F2 %d 0 R >>%s >> /Contents %d 0 R >>'%(W,H,font1,font2,xobjects,sid)).encode());ids.append(pid)
        objects[0]=b'<< /Type /Catalog /Pages 2 0 R >>'
        objects[1]=('<< /Type /Pages /Count %d /Kids [%s] >>'%(len(ids),' '.join('%d 0 R'%i for i in ids))).encode()
        data=bytearray(b'%PDF-1.4\n%\xe2\xe3\xcf\xd3\n');offsets=[0]
        for i,v in enumerate(objects,1):offsets.append(len(data));data+=('%d 0 obj\n'%i).encode()+v+b'\nendobj\n'
        xref=len(data);data+=('xref\n0 %d\n0000000000 65535 f \n'%len(offsets)).encode()
        for x in offsets[1:]:data+=('%010d 00000 n \n'%x).encode()
        data+=('trailer\n<< /Size %d /Root 1 0 R >>\nstartxref\n%d\n%%%%EOF\n'%(len(offsets),xref)).encode();path.parent.mkdir(exist_ok=True);path.write_bytes(data)
def blocks(node):
    if not isinstance(node,Node):return
    classes=node.a.get('class','').split()
    if node.tag in ['nav','button','script','style','figure','form'] or any(c in classes for c in ['pl-row','only-f','noprint','kn-embed']):return
    if node.tag in ['h1']:return
    if node.tag in ['h2','h3','p','dt','dd','label']:
        text=node.text()
        if text:yield ('h3' if node.tag=='dt' else node.tag if node.tag in ['h2','h3'] else 'p',text)
        return
    if node.tag in ['ul','ol']:
        for i,c in enumerate(x for x in node.children if isinstance(x,Node) and x.tag=='li'):
            yield ('p', ('%d. '%(i+1) if node.tag=='ol' else '- ')+c.text())
        return
    if node.tag=='table':
        rows=list(node.all('tr'));headers=[]
        if rows:headers=[x.text() for x in rows[0].all('th')]
        for row in rows:
            cells=[x.text() for x in row.children if isinstance(x,Node) and x.tag=='td']
            if cells:yield ('p',' / '.join((headers[i]+': ' if i<len(headers) else '')+t for i,t in enumerate(cells) if t))
        return
    for c in node.children:yield from blocks(c)
def main():
    pdf=PDF()
    for file,title in [('apprenant.html','Comprendre, choisir et contrôler'),('noeuds.html','Atelier au sol : nœuds et contrôles'),('approfondissement.html','Nœuds complémentaires'),('complements.html','Compléments techniques et références')]:
        doc=Tree((ROOT/file).read_text(encoding='utf-8'));main=next(doc.root.all('main'));pdf.page(title)
        if file=='noeuds.html':pdf.para('Les dessins animés montrent un trajet ouvert. Le geste et le serrage se travaillent sur corde réelle au sol, sans personne suspendue. Les contrôles mathématiques des tracés ne constituent pas une validation d’emploi.')
        for kind,text in blocks(main):pdf.para(text,kind)
    for title,name in [('Réglage du harnais : relier les repères au matériel','A-harnais-9-etapes.jpg'),('Contrôle du matériel : zones à examiner','I-controle-visuel.jpg'),('Ancrage et espace libre : deux notions distinctes','D-facteur-chute.jpg'),('Secours : une organisation préparée avant le travail','E-victime-suspendue.jpg')]:pdf.image_page(title,ROOT/'assets/img/gpt'/name)
    pdf.page('Auto-évaluation : dix décisions de prévention')
    js="const fs=require('fs'),vm=require('vm');const c={window:{}};vm.runInNewContext(fs.readFileSync(process.argv[1],'utf8'),c);process.stdout.write(JSON.stringify(c.window.QCM));"
    qcm=json.loads(subprocess.check_output(['node','-e',js,str(ROOT/'js/qcm-data.js')],text=True,encoding='utf-8'))
    for i,q in enumerate(qcm):
        pdf.para(str(i+1)+'. '+q['q'],'h3')
        for j,t in enumerate(q['o']):pdf.para(chr(65+j)+'. '+t)
    pdf.page('Auto-évaluation : correction commentée')
    for i,q in enumerate(qcm):pdf.para(str(i+1)+'. Réponse '+chr(65+q['a'])+' - '+q['e'])
    pdf.page('Sources principales de la révision du 27/11/2026')
    for title,url in [
        ('R.4323-61 : système approprié, chute, non-isolement, notice employeur','https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000018531391/'),
        ('Arrêté du 19 mars 1993, articles 1 et 2 : vérifications des systèmes antichute','https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000179220/'),
        ('R.4224-15 : formation des secouristes, ateliers et chantiers','https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000018532203/'),
        ('INRS : protection individuelle contre les chutes','https://www.inrs.fr/risques/chutes-hauteur/equipements-protection-individuelle-chutes-hauteur'),
        ('Petzl : paramètres et limites du calcul du dégagement','https://www.petzl.com/fr/fr/calculateur-de-degagement/clearancecalculator.html'),
        ('MSA : syndrome du harnais, avril 2025','https://ssa.msa.fr/wp-content/uploads/2025/04/SyndromeDuHarnais_avril2025-1.pdf'),
        ('Sécurité civile : références techniques nationales de secourisme','https://www.securite-civile.interieur.gouv.fr/documentation/secourisme-et-associations/secourisme-references-techniques-nationales.html')]:
        pdf.para(title,'h3');pdf.para(url)
    output=ROOT/'pdf/livret-formation-260053a.pdf';pdf.save(output)
    # Les zones de texte sont vérifiées avant écriture ; l’inspection visuelle complète la recette.
    bad=[x for x in pdf.stats if x['y']<8 or x['y']>H or x['x']+x['width']>W-24]
    report={'pages':len(pdf.pages),'bytes':output.stat().st_size,'lines':len(pdf.stats),'out_of_bounds':bad}
    (ROOT/'qa/livret-layout.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    if bad:raise ValueError('Text outside page bounds')
    print(json.dumps(report,ensure_ascii=False))
if __name__=='__main__':main()
