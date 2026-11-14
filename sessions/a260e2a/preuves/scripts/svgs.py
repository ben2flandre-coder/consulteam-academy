import json, html, os
OUT='/home/claude/work/a260e2a/images/schemas'
N='#102c53';B='#0b68ae';Y='#f6b63d';I='#16273d';M='#53657a';L='#cbd5e1';OK='#16794a';KO='#b3261e';PALE='#eef3f9'
def esc(s): return html.escape(s,quote=True)
class S:
    def __init__(s,w,h,title,desc): s.w,s.h,s.t,s.d,s.b=w,h,title,desc,[]
    def add(s,x): s.b.append(x)
    def rect(s,x,y,w,h,fill=PALE,stroke=N,sw=2,rx=0,dash=None,extra=''):
        s.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"'+(f' stroke-dasharray="{dash}"' if dash else '')+f' {extra}/>')
    def line(s,x1,y1,x2,y2,c=N,sw=2,dash=None,extra=''):
        s.add(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c}" stroke-width="{sw}"'+(f' stroke-dasharray="{dash}"' if dash else '')+f' {extra}/>')
    def poly(s,pts,c=N,sw=3,fill='none',dash=None,extra=''):
        p=' '.join(f'{x},{y}' for x,y in pts)
        s.add(f'<polyline points="{p}" fill="{fill}" stroke="{c}" stroke-width="{sw}" stroke-linejoin="round" stroke-linecap="round"'+(f' stroke-dasharray="{dash}"' if dash else '')+f' {extra}/>')
    def poly_closed(s,pts,fill=PALE,c=N,sw=2):
        p=' '.join(f'{x},{y}' for x,y in pts); s.add(f'<polygon points="{p}" fill="{fill}" stroke="{c}" stroke-width="{sw}"/>')
    def circle(s,x,y,r,fill='#fff',c=N,sw=2): s.add(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{c}" stroke-width="{sw}"/>')
    def ellipse(s,x,y,rx,ry,fill='none',c=N,sw=2): s.add(f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{fill}" stroke="{c}" stroke-width="{sw}"/>')
    def text(s,x,y,t,size=14,weight=400,anchor='start',fill=I,cls='lbl'):
        s.add(f'<text class="{cls}" x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" fill="{fill}">{esc(t)}</text>')
    def call(s,n,tx,ty,lx,ly):
        s.line(tx,ty,lx,ly,c=M,sw=1.5)
        s.circle(tx,ty,2.5,fill=M,c=M,sw=1)
        s.circle(lx,ly,12,fill=N,c=N,sw=1)
        s.add(f'<text class="num" x="{lx}" y="{ly+5}" font-size="14" font-weight="700" text-anchor="middle" fill="#fff">{n}</text>')
    def legend(s,x,y,items,title='Légende',lh=30,wrap=34):
        s.text(x,y,title,16,700,fill=N); y+=24
        for n,t in items:
            s.circle(x+12,y-5,12,fill=N,c=N,sw=1)
            s.add(f'<text class="num" x="{x+12}" y="{y}" font-size="14" font-weight="700" text-anchor="middle" fill="#fff">{n}</text>')
            words=t.split(' ');lines=[];cur=''
            for w_ in words:
                if len(cur)+len(w_)+1>wrap and cur: lines.append(cur);cur=w_
                else: cur=(cur+' '+w_).strip()
            lines.append(cur)
            for k,l in enumerate(lines): s.text(x+32,y+k*18,l,14)
            y+=max(lh,len(lines)*18+10)
        return y
    def save(s,name):
        sty='<style>.lbl,.num{font-family:system-ui,-apple-system,"Segoe UI",Arial,sans-serif}</style>'
        svg=(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {s.w} {s.h}" width="{s.w}" height="{s.h}" role="img" aria-labelledby="t d">'
             f'<title id="t">{esc(s.t)}</title><desc id="d">{esc(s.d)}</desc>{sty}<rect width="{s.w}" height="{s.h}" fill="#ffffff"/>'+''.join(s.b)+'</svg>')
        open(f'{OUT}/{name}','w',encoding='utf-8').write(svg)
def head(s,t,sub): 
    s.text(24,34,t,20,700,fill=N); s.text(24,56,sub,13,400,fill=M)
def foot(s,t): s.text(24,s.h-16,t,12,400,fill=M)

# ---------- F2 coupe disjoncteur ----------
def f_disj():
    s=S(960,580,"Coupe d'un disjoncteur modulaire magnétothermique","Schéma de principe en coupe : borne amont, bilame, bobine avec noyau, mécanisme, poignée, contacts, chambre de coupure, borne aval et clip de fixation sur rail.")
    head(s,"Coupe d'un disjoncteur modulaire magnétothermique","Schéma de principe, non à l'échelle")
    s.rect(40,90,600,400,fill='#f4f7fb',sw=3,rx=16)
    s.rect(250,490,150,20,fill=L,rx=3); s.text(325,505,"clip de fixation",12,anchor='middle')
    # poignée + mécanisme
    s.rect(340,52,60,50,fill=Y,rx=8); s.circle(370,108,6,fill=N)
    s.rect(310,118,140,64,fill='#fff',dash='6 4',rx=6); s.line(325,150,435,150,c=M,sw=1.5); s.line(380,128,380,172,c=M,sw=1.5)
    # circuit
    s.rect(48,265,52,30,fill=L,rx=3); s.line(60,280,88,280,c=N,sw=3)   # borne amont (vis)
    s.poly([(100,280),(112,280)],c=B)
    s.rect(112,270,112,6,fill='#d9822b',stroke=N,sw=1); s.rect(112,276,112,6,fill='#8aa0b8',stroke=N,sw=1)   # bilame
    s.poly([(112,288),(224,290)],c='none')
    s.add(f'<path d="M112 270 Q168 252 224 262" fill="none" stroke="{KO}" stroke-width="1.5" stroke-dasharray="5 4"/>')  # position fléchie
    s.poly([(224,279),(240,279),(246,270),(252,288),(258,279)],c=B,sw=2)   # tresse
    s.rect(262,242,100,76,fill='#fff',rx=8)   # bobine
    for x in range(274,356,12): s.ellipse(x,280,5,32,c=I,sw=1.5)
    s.rect(296,196,32,48,fill=L,rx=3); s.line(312,196,330,182,c=KO,sw=2); s.poly([(326,186),(334,180),(332,190)],c=KO,sw=2)   # noyau mobile + percuteur
    s.poly([(362,279),(380,279)],c=B)
    # contact mobile (fermé) et ouvert (pointillé)
    s.line(380,279,462,279,c=N,sw=5); s.circle(380,279,6,fill=Y)
    s.line(380,279,456,240,c=KO,sw=3,dash='7 5'); 
    s.line(400,182,414,274,c=M,sw=2.5)   # bielle
    s.rect(464,262,24,34,fill=L,rx=3)  # contact fixe
    s.poly([(470,252),(476,242),(472,238),(480,226)],c=KO,sw=2.5)   # arc
    # chambre de coupure
    for k in range(7): s.rect(496+k*14,222,5,112,fill=B,stroke=B,sw=1)
    s.poly([(488,279),(488,400),(612,400)],c=B)
    s.rect(592,384,48,32,fill=L,rx=3); s.line(604,400,630,400,c=N,sw=3)   # borne aval
    # callouts
    s.call(1,74,265,74,226); s.call(2,170,270,170,226); s.call(3,312,220,312,226)
    s.call(4,380,122,470,100); s.call(5,400,60,470,60); s.call(6,476,279,560,184)
    s.call(7,540,224,600,150); s.call(8,616,386,616,330); s.call(9,262,500,200,540)
    s.legend(670,90,[(1,"Borne amont (arrivée)"),(2,"Bilame : se déforme à la chaleur d'une surcharge (organe thermique)"),(3,"Bobine et noyau mobile : agit sur un court-circuit (organe magnétique)"),(4,"Mécanisme à déclenchement : ouvre les contacts"),(5,"Manette de manœuvre"),(6,"Contacts fixe et mobile (ouverts en pointillé, arc en rouge)"),(7,"Chambre de coupure : divise l'arc"),(8,"Borne aval (départ)"),(9,"Clip de fixation sur le rail")],wrap=33)
    foot(s,"Ordre des éléments d'après S10 ; organes d'après S2. Disposition simplifiée : elle varie selon les fabricants.")
    s.save('F2-coupe-disjoncteur.svg')

# ---------- F3 différentiel ----------
def f_diff():
    s=S(960,600,"Principe d'un interrupteur différentiel","Schéma de principe : les conducteurs de phase et de neutre traversent un tore ; un enroulement alimente un relais sensible qui commande le mécanisme ; un circuit d'essai avec bouton test dérive un courant hors du tore.")
    head(s,"Principe d'un interrupteur différentiel","Schéma de principe, non à l'échelle")
    s.rect(40,90,600,430,fill='#f4f7fb',sw=3,rx=16)
    s.text(60,125,"Amont",14,700,fill=M); s.text(580,125,"Aval (circuits protégés)",14,700,anchor='end',fill=M)
    # conducteurs
    yL,yN=190,300
    s.poly([(40,yL),(200,yL)],c=KO,sw=4); s.poly([(40,yN),(200,yN)],c=B,sw=4)
    s.text(48,yL-10,"Phase",13,700,fill=KO); s.text(48,yN-10,"Neutre",13,700,fill=B)
    # contacts de coupure
    for y,c in((yL,KO),(yN,B)):
        s.circle(130,y,5,fill='#fff',c=c); s.line(130,y,166,y-18,c=c,sw=3)
    s.line(166,yL-18,166,yN-18,c=M,sw=2,dash='4 3')   # liaison mécanique
    s.poly([(176,yL),(330,yL)],c=KO,sw=4); s.poly([(176,yN),(330,yN)],c=B,sw=4)
    # tore
    s.ellipse(330,245,30,95,fill='#fff',c=N,sw=3); s.ellipse(330,245,14,55,fill=PALE,c=N,sw=2)
    s.poly([(330,yL),(580,yL)],c=KO,sw=4); s.poly([(330,yN),(580,yN)],c=B,sw=4)
    s.poly([(580,yL),(620,yL)],c=KO,sw=4); s.poly([(580,yN),(620,yN)],c=B,sw=4)
    # enroulement + relais
    s.poly([(318,160),(318,130),(420,130),(420,150)],c=M,sw=2)
    s.rect(380,150,90,52,fill='#fff',rx=6); s.line(392,176,458,176,c=I,sw=2); s.text(425,194,"relais",11,anchor='middle')
    s.poly([(318,330),(318,360),(420,360),(420,330)],c=M,sw=2)
    s.line(420,202,420,225,c=M,sw=2); s.line(420,225,166,225,c=M,sw=2,dash='6 4'); s.poly([(166,225),(176,219),(176,231)],c=M,sw=2,fill=M)
    # circuit d'essai
    s.poly([(200,yL),(200,430),(500,430)],c=OK,sw=2.5,dash='8 4')
    s.rect(230,414,50,32,fill=Y,rx=6); s.text(255,436,"T",16,700,anchor='middle')
    s.rect(330,416,60,28,fill='#fff',rx=3); s.line(340,430,380,430,c=I,sw=2)
    s.poly([(500,430),(500,yN),(580,yN)],c=OK,sw=2.5,dash='8 4')
    # fuite
    s.poly([(560,yL),(560,380),(560,470)],c=KO,sw=2,dash='3 3'); s.poly([(552,458),(560,474),(568,458)],c=KO,sw=2,fill=KO)
    s.line(540,478,580,478,c=N,sw=3); s.line(547,486,573,486,c=N,sw=3); s.line(554,494,566,494,c=N,sw=3)
    s.rect(560-14,210,0,0)
    # callouts
    s.call(1,100,yL,100,150); s.call(2,330,157,360,115); s.call(3,318,345,270,395)
    s.call(4,470,176,520,150); s.call(5,296,225,296,60); s.call(6,130,yN,100,345)
    s.call(7,255,414,255,375); s.call(8,360,444,360,490); s.call(9,560,420,610,420)
    s.legend(670,90,[(1,"Conducteurs aller (phase) et retour (neutre) vers les circuits"),(2,"Tore magnétique traversé par tous les conducteurs actifs"),(3,"Enroulement détecteur autour du tore"),(4,"Relais sensible : réagit à l'écart de courant"),(5,"Mécanisme de déclenchement"),(6,"Contacts de coupure (tous les pôles, liés mécaniquement)"),(7,"Bouton test T"),(8,"Résistance du circuit d'essai"),(9,"Fuite vers la terre (défaut d'isolement)")],wrap=33)
    s.text(40,548,"Courant aller = courant retour : aucun signal dans l'enroulement.",13,700,fill=OK)
    s.text(40,568,"Fuite à la terre : écart ≥ sensibilité (30 mA en logement, S3) → déclenchement.",13,700,fill=KO)
    foot(s,"Comparaison des courants : S3. Tore et circuit d'essai hors du tore : S4 (extrait). Disposition simplifiée.")
    s.save('F3-principe-differentiel.svg')

# ---------- F4 contacteur ----------
def f_cont():
    s=S(960,640,"Coupe d'un contacteur électromagnétique","Schéma de principe en coupe, au repos : bobine sur le circuit magnétique fixe, armature mobile, entrefer, ressort de rappel, spire de déphasage, pont de contacts mobile, contacts fixes avec bornes de puissance et bloc de contacts auxiliaires.")
    head(s,"Coupe d'un contacteur électromagnétique (au repos)","Schéma de principe, non à l'échelle")
    s.rect(40,90,600,480,fill='#f4f7fb',sw=3,rx=16)
    # contacts de puissance en haut
    s.rect(100,120,60,26,fill=L,rx=3); s.rect(300,120,60,26,fill=L,rx=3); s.rect(480,120,60,26,fill=L,rx=3)   # contacts fixes (3 pôles)
    s.rect(112,150,36,12,fill=Y,rx=2);s.rect(312,150,36,12,fill=Y,rx=2);s.rect(492,150,36,12,fill=Y,rx=2) # contacts mobiles
    s.line(100,110,100,120,c=N,sw=3);s.line(160,110,160,120,c=N,sw=3)
    for x in (130,330,510): s.line(x,162,x,200,c=M,sw=2)
    s.rect(110,196,430,16,fill=L,rx=4)   # porte-contacts (pont)
    s.line(325,212,325,260,c=M,sw=4)     # tige
    # armature mobile
    s.rect(180,262,290,30,fill='#fff',stroke=N,sw=2.5,rx=3)
    # entrefer
    s.rect(180,292,290,16,fill='none',stroke=KO,sw=1.5,dash='5 4',rx=0); 
    # circuit magnétique fixe (forme en E)
    s.poly_closed([(180,308),(470,308),(470,520),(396,520),(396,380),(254,380),(254,520),(180,520)],fill='#e1e8f1')
    s.rect(300,308,50,150,fill='#e1e8f1',sw=2); 
    s.rect(266,330,118,110,fill='#fff',stroke=N,sw=2,rx=6)   # bobine autour de la jambe centrale
    for y in range(340,436,12): s.line(270,y,296,y,c=I,sw=2); s.line(354,y,380,y,c=I,sw=2)
    # spire de déphasage
    s.rect(306,312,16,8,fill=Y,stroke=N,sw=1)
    # ressort de rappel
    pts=[(210,308)]
    for k in range(7): pts+=[(200 if k%2==0 else 220, 308-8*(k+1)*0.0 ) ]
    s.poly([(210,262),(198,252),(222,244),(198,236),(222,228),(198,220),(210,212)],c=M,sw=2)
    s.line(210,308,210,292,c=M,sw=2)
    # bornes bobine
    s.line(285,520,285,548,c=N,sw=3); s.line(365,520,365,548,c=N,sw=3)
    s.text(285,566,"A1",14,700,anchor='middle'); s.text(365,566,"A2",14,700,anchor='middle')
    s.poly([(285,520),(285,440)],c=B,sw=2); s.poly([(365,520),(365,440)],c=B,sw=2)
    # contacts auxiliaires
    s.rect(500,260,120,100,fill='#fff',stroke=N,sw=2,rx=6); s.rect(515,285,40,18,fill=Y,rx=2); s.rect(565,285,40,18,fill=Y,rx=2); s.line(535,303,535,330,c=M,sw=2); s.line(585,303,585,330,c=M,sw=2)
    s.line(470,277,500,277,c=M,sw=3,dash='4 3')
    # flèche de course
    s.poly([(250,268),(250,300)],c=OK,sw=2.5); s.poly([(244,292),(250,304),(256,292)],c=OK,sw=2.5,fill=OK)
    s.text(262,300,"course",11,fill=OK)
    s.call(1,320,388,230,440+60); s.call(2,196,480,150,440+30)
    s.call(3,440,277,560,240); s.call(4,200,300,120,300); s.call(5,198,236,110,236)
    s.call(6,314,316,420,330); s.call(7,130,203,70,203); s.call(8,100,122,70,160)
    s.call(9,560,360,560,400)
    s.legend(670,90,[(1,"Bobine (bornes A1 et A2) : crée le champ magnétique"),(2,"Circuit magnétique fixe, feuilleté"),(3,"Armature (partie mobile du circuit magnétique)"),(4,"Entrefer : se ferme quand la bobine est alimentée"),(5,"Ressort de rappel : rouvre les contacts à la désexcitation"),(6,"Spire de déphasage : limite les vibrations en alternatif"),(7,"Pont de contacts mobiles (circuit de puissance)"),(8,"Contacts fixes et bornes de puissance"),(9,"Bloc de contacts auxiliaires (commande, signalisation)")],wrap=33)
    s.text(40,592,"Bobine alimentée : l'armature est attirée, les contacts se ferment. Bobine coupée : le ressort rouvre.",12,700,fill=N)
    foot(s,"Constitution et fonctionnement : S5. Contacts principaux et auxiliaires : S17. Spire de déphasage : S18 (source faible, à confirmer).")
    s.save('F4-coupe-contacteur.svg')

# ---------- F5 rail et peigne ----------
def f_rail():
    s=S(960,600,"Coupe d'une rangée de tableau : appareil clipsé sur rail et peigne","Vue de profil : plaque de fond, rail, griffe de fixation, appareil modulaire, peigne d'alimentation en haut, bornes amont et aval, conducteur aval, plastron et manette ; outil de dépose en pointillé.")
    head(s,"Coupe d'une rangée : appareil sur rail, peigne et raccordements","Vue de profil, schéma de principe, non à l'échelle")
    s.rect(40,90,600,450,fill='#f4f7fb',sw=3,rx=16)
    s.rect(70,110,36,410,fill=L,sw=2)   # plaque de fond
    # rail (profil)
    s.poly_closed([(106,300),(130,300),(130,306),(124,306),(124,336),(130,336),(130,342),(106,342)],fill='#9fb2c8')
    # appareil
    s.poly_closed([(130,170),(420,170),(420,470),(130,470)],fill='#fff',c=N,sw=3)
    s.rect(130,170,290,40,fill='#e1e8f1',sw=0); s.line(130,210,420,210,c=N,sw=1.5)
    s.rect(356,230,52,110,fill=Y,rx=8,sw=2)   # manette
    # griffe
    s.poly_closed([(130,306),(150,306),(150,336),(130,336)],fill=L); s.poly_closed([(130,470),(150,470),(150,500),(130,500),(130,470)],fill=L)
    s.line(140,336,140,500,c=M,sw=2)
    # bornes amont (haut) et peigne
    s.rect(160,130,100,40,fill=L,rx=4); s.circle(190,150,9,fill='#fff'); s.line(184,150,196,150,c=N,sw=2)
    s.rect(150,100,280,22,fill='#d9822b',stroke=N,sw=2,rx=3); s.line(190,122,190,142,c=B,sw=3)
    # bornes aval (bas) et conducteur
    s.rect(160,470,100,40,fill=L,rx=4); s.circle(190,490,9,fill='#fff'); s.line(184,490,196,490,c=N,sw=2)
    s.poly([(190,510),(190,545),(330,545),(330,570)],c=B,sw=5); s.poly([(190,514),(190,530)],c='#fff',sw=2)
    # plastron
    s.rect(340,150,100,330,fill='none',stroke=OK,sw=2.5,dash='8 5',rx=6)
    # outil de dépose
    s.poly([(120,520),(150,480),(180,455)],c=KO,sw=3,dash='7 5'); s.poly([(176,448),(184,460),(172,462)],c=KO,sw=2,fill=KO)
    s.call(1,88,200,60,170); s.call(2,118,321,80,321+40)
    s.call(3,140,490,100,540); s.call(4,260,300,300,260+0)
    s.call(5,290,111,200,76+0); s.call(6,200,150,230,70+0)
    s.call(7,330,560,420,560); s.call(8,230,490,330,526+0)
    s.call(9,440,300,500,300); s.call(10,380,285,500,240)
    s.legend(670,90,[(1,"Plaque de fond"),(2,"Rail de fixation"),(3,"Griffe de fixation (clip) : on la libère avec un outil"),(4,"Appareil modulaire (boîtier isolant)"),(5,"Peigne d'alimentation (haut)"),(6,"Borne amont (à vis ou automatique)"),(7,"Conducteur aval"),(8,"Borne aval"),(9,"Plastron : cache les parties actives, laisse passer les manettes"),(10,"Manette")],wrap=33)
    s.text(670,490,"Flèche rouge : levier sur la griffe pour sortir",12,fill=KO); s.text(670,508,"l'appareil (S8).",12,fill=KO)
    foot(s,"Pose, peigne, bornes et levier : S8, S9 ; composition d'un tableau : S6. Disposition simplifiée.")
    s.save('F5-coupe-rail-peigne.svg')

# ---------- F1 façade tableau ----------
def f_tab():
    s=S(960,640,"Vue de face d'un tableau de répartition à deux rangées","Façade légendée : disjoncteur de branchement en amont, interrupteurs différentiels de tête de rangée, disjoncteurs divisionnaires, parafoudre, contacteur, télérupteur, minuterie, emplacements libres et bornier de terre.")
    head(s,"Vue de face d'un tableau de répartition (2 rangées)","Façade type logement, schéma de principe, non à l'échelle")
    s.rect(40,90,660,470,fill='#f4f7fb',sw=3,rx=14)
    s.rect(52,100,100,34,fill=L,rx=4)   # disjoncteur de branchement (hors coffret)
    s.text(102,122,"branchement",11,anchor='middle')
    def row(y,items):
        s.rect(60,y,620,165,fill='#fff',stroke=L,sw=1.5,rx=6)
        s.rect(70,y+8,570,12,fill='#d9822b',stroke=N,sw=1,rx=2)    # peigne
        x=80
        for kind,w in items:
            if kind=='id':  s.rect(x,y+30,w,100,fill=L,rx=4); s.rect(x+w/2-12,y+48,24,16,fill=Y,rx=2); s.text(x+w/2,y+110,"30 mA",11,anchor='middle')
            elif kind=='d': s.rect(x,y+30,w,100,fill='#e1e8f1',rx=4); s.rect(x+w/2-8,y+42,16,30,fill='#fff',rx=3); s.text(x+w/2,y+112,"In",11,anchor='middle')
            elif kind=='p': s.rect(x,y+30,w,100,fill='#e1e8f1',rx=4); s.rect(x+10,y+44,w-20,22,fill=OK,rx=3); s.text(x+w/2,y+112,"parafoudre",10,anchor='middle')
            elif kind=='c': s.rect(x,y+30,w,100,fill='#e1e8f1',rx=4); s.rect(x+10,y+50,w-20,36,fill='#fff',rx=3); s.text(x+w/2,y+112,"contact.",10,anchor='middle')
            elif kind=='t': s.rect(x,y+30,w,100,fill='#e1e8f1',rx=4); s.circle(x+w/2,y+62,10,fill=Y); s.text(x+w/2,y+112,"télérupt.",10,anchor='middle')
            elif kind=='m': s.rect(x,y+30,w,100,fill='#e1e8f1',rx=4); s.circle(x+w/2,y+62,12,fill='#fff'); s.text(x+w/2,y+112,"minut.",10,anchor='middle')
            elif kind=='r': s.rect(x,y+30,w,100,fill='none',stroke=M,sw=1.5,dash='6 4',rx=4)
            x+=w+4
    row(150,[('id',54),('d',36),('d',36),('d',36),('d',36),('p',72),('c',54),('r',36),('r',36),('r',36)])
    row(320,[('id',54),('d',36),('d',36),('d',36),('t',44),('m',36),('r',36),('r',36),('r',36),('r',36),('r',36)])
    s.rect(60,505,150,50,fill=OK,rx=4); s.text(135,535,"bornier de terre",12,700,anchor='middle',fill='#fff')
    s.rect(260,505,160,50,fill='#4a90d9',rx=4); s.text(340,535,"bornier de neutre",12,700,anchor='middle',fill='#fff')
    def bd(n,x,y,tx,ty): s.call(n,tx,ty,x,y)
    bd(1,190,117,152,117)
    bd(2,107,297,107,278); bd(3,156,297,156,278); bd(4,334,297,334,278); bd(5,401,297,401,278); bd(8,450,297,450,278)
    bd(6,280,467,280,448); bd(7,324,467,324,448)
    bd(10,664,164,640,164)
    bd(9,235,530,210,530); bd(11,445,530,420,530)
    s.legend(768,80,[],title='')
    items=[(1,"Disjoncteur de branchement, en amont"),(2,"Interrupteur différentiel (tête de rangée)"),(3,"Disjoncteurs divisionnaires"),(4,"Parafoudre"),(5,"Contacteur"),(6,"Télérupteur"),(7,"Minuterie"),(8,"Emplacements libres (réserve)"),(9,"Bornier de terre"),(10,"Peigne d'alimentation"),(11,"Bornier de neutre")]
    s.legend(758,90,items,wrap=22,lh=34)
    foot(s,"Appareils et rôles : S6 ; réserve de 20 % (logement) : S14. Disposition type, elle varie selon les tableaux et les usages.")
    s.save('F1-facade-tableau.svg')

# ---------- F6 équilibrage (valeurs lues dans preuves/calcul-equilibrage.json) ----------
def f_equi():
    import json
    c=json.load(open('/home/claude/work/a260e2a/preuves/calcul-equilibrage.json',encoding='utf-8'))
    av,ap=c['avant'],c['apres_methode']
    s=S(960,640,"Équilibrage des phases : avant et après","Barres du courant par phase L1, L2, L3 avant et après répartition des circuits monophasés, avec la moyenne, le courant dans le neutre et le déséquilibre calculés.")
    head(s,"Équilibrer un tableau triphasé : exemple chiffré fictif","8 circuits monophasés de 16, 16, 10, 10, 8, 6, 6 et 4 A, charges résistives")
    sc=7.0; base=470
    mean=av['moyenne_A']
    def panel(x0,d,label):
        s.rect(x0,90,300,470,fill='#f4f7fb',sw=3,rx=14)
        s.text(x0+150,118,label,16,700,anchor='middle',fill=N)
        for i,(ph,col) in enumerate([('L1','#7a4a1e'),('L2','#222'),('L3','#6b6b6b')]):
            v=d['courants_par_phase'][ph]; h=v*sc; bx=x0+30+i*90
            s.rect(bx,base-h,60,h,fill=[ '#b3261e','#d9a300','#0b68ae'][i],stroke=N,sw=1.5,rx=3)
            s.text(bx+30,base-h+22,f"{v} A",14,700,anchor='middle',fill='#fff' if i!=1 else I)
            s.text(bx+30,base+22,ph,14,700,anchor='middle')
        my=base-mean*sc
        s.line(x0+15,my,x0+285,my,c=OK,sw=2,dash='6 4')
        s.text(x0+150,142,f"moyenne {str(mean).replace('.',',')} A (ligne verte)",12,700,anchor='middle',fill=OK)
        if x0==40:
            s.circle(x0+270,my-16,12,fill=N,c=N,sw=1); s.add(f'<text class="num" x="{x0+270}" y="{my-11}" font-size="14" font-weight="700" text-anchor="middle" fill="#fff">2</text>')
            s.circle(x0+30,base-42*sc-30,12,fill=N,c=N,sw=1); s.add(f'<text class="num" x="{x0+30}" y="{base-42*sc-25}" font-size="14" font-weight="700" text-anchor="middle" fill="#fff">1</text>')
        s.rect(x0+20,500,260,48,fill='#fff',stroke=N,sw=1.5,rx=6)
        s.text(x0+30,520,f"Courant dans le neutre : {str(d['courant_neutre_A']).replace('.',',')} A",13,700)
        s.text(x0+30,539,f"Déséquilibre : {str(d['desequilibre_pct']).replace('.',',')} %",13,400)
        if x0==40:
            s.circle(x0+262,540,12,fill=N,c=N,sw=1); s.add(f'<text class="num" x="{x0+262}" y="545" font-size="14" font-weight="700" text-anchor="middle" fill="#fff">4</text>')
            s.circle(x0+262,512,12,fill=N,c=N,sw=1); s.add(f'<text class="num" x="{x0+262}" y="517" font-size="14" font-weight="700" text-anchor="middle" fill="#fff">3</text>')
    panel(40,av,"Avant")
    panel(360,ap,"Après")
    items=[(1,"Barre : somme des courants des circuits branchés sur la phase"),(2,"Ligne verte : courant moyen des trois phases"),(3,"Neutre : somme vectorielle des trois courants, pas leur somme simple"),(4,"Déséquilibre : écart maximal à la moyenne, divisé par la moyenne (S13)")]
    s.legend(690,90,items,wrap=28,lh=36)
    s.text(690,380,"Méthode : classer les circuits du plus fort",12,700,fill=N)
    s.text(690,398,"au plus faible, puis brancher chacun sur la",12,700,fill=N)
    s.text(690,416,"phase la moins chargée à cet instant.",12,700,fill=N)
    s.text(690,448,"Phases équilibrées ne veut pas dire neutre",12,400,fill=KO)
    s.text(690,466,"sans courant : les harmoniques de rang 3",12,400,fill=KO)
    s.text(690,484,"des charges non linéaires s'y ajoutent",12,400,fill=KO); s.text(690,502,"(S11).",12,400,fill=KO)
    foot(s,"Calcul : script preuves/calcul-equilibrage (phaseurs, 6561 répartitions testées). Formule : S13. Neutre : S12. Exemple fictif.")
    s.save('F6-equilibrage-avant-apres.svg')

def flow(name,title,sub,desc,steps,ft):
    s=S(960,660,title,desc)
    head(s,title,sub)
    y=76; bh=56; gap=14
    for i,(a,b) in enumerate(steps,1):
        s.rect(40,y,880,bh,fill='#f4f7fb' if i%2 else '#fff',sw=1.5,rx=8)
        s.circle(70,y+bh/2,14,fill=N,c=N,sw=1)
        s.add(f'<text class="num" x="70" y="{y+bh/2+5}" font-size="14" font-weight="700" text-anchor="middle" fill="#fff">{i}</text>')
        s.text(100,y+23,a,15,700,fill=N); s.text(100,y+43,b,13,400,fill=I)
        if i<len(steps):
            s.line(70,y+bh,70,y+bh+gap,c=M,sw=2)
        y+=bh+gap
    foot(s,ft); s.save(name)

def f_flows():
    flow('F7-remplacement-appareil.svg',"Remplacer un appareil dans un tableau : les étapes","Déroulé type, à adapter à l'installation et aux consignes du chargé de travaux",
     "Huit étapes : identifier, vérifier l'habilitation, consigner, vérifier l'absence de tension, déposer, poser l'identique, raccorder et repérer, déconsigner et essayer.",
     [("Identifier le défaut et l'appareil","Relever calibre, courbe, pouvoir de coupure, type de différentiel : l'appareil posé doit être équivalent (S7, S8)"),
      ("Vérifier le périmètre de l'habilitation","L'opération et la situation correspondent-elles au titre détenu ? Sinon, s'arrêter et demander (S1)"),
      ("Consigner","Séparer, condamner, identifier : l'ordre de la consignation enseignée par Consul Team (S22)"),
      ("Vérifier l'absence de tension","Avec un VAT, neutre compris, contrôlé avant et après sur une source connue (S16)"),
      ("Déposer l'appareil","Repérer les fils avant de les retirer, puis levier sur la griffe pour sortir l'appareil du rail (S8)"),
      ("Poser l'appareil équivalent","Même calibre, même courbe, pouvoir de coupure au moins égal : clipser sur le rail, vérifier le peigne (S8)"),
      ("Raccorder et repérer","Serrage soigné, conducteurs aux bonnes bornes, étiquette à jour (S15)"),
      ("Déconsigner et essayer","Remettre sous tension dans l'ordre prévu, essai de l'appareil, bouton T pour un différentiel (S3, S16)")],
     "Sources : S1, S3, S7, S8, S15, S16, S22. Déroulé pédagogique : le formateur le valide pour le contexte ADI.")
    flow('F8-installation-appareil.svg',"Installer un nouvel appareil dans un tableau : les étapes","Déroulé type, à adapter à l'installation et aux consignes du chargé de travaux",
     "Huit étapes : cadrer, vérifier la place et la réserve, choisir l'appareil, consigner, clipser et raccorder au peigne, raccorder l'aval, repérer et mettre à jour le schéma, essayer.",
     [("Cadrer l'opération","C'est une modification de l'installation : vérifier le titre et le périmètre avant d'agir (S1)"),
      ("Vérifier la place et la réserve","Emplacement libre sur la rangée ; une réserve minimale de 20 % est prescrite en logement (S14)"),
      ("Choisir l'appareil","Calibre, courbe, pouvoir de coupure supérieur au courant de court-circuit, type de différentiel (S7, S9)"),
      ("Consigner et vérifier l'absence de tension","Séparer, condamner, identifier, puis VAT neutre compris (S22, S16)"),
      ("Clipser l'appareil et alimenter par le peigne","Accrocher sur le rail, insérer le peigne, serrer la borne amont (S9)"),
      ("Raccorder le circuit aval","Section adaptée au calibre, conducteur de terre au bornier, bornes serrées (S9)"),
      ("Repérer et mettre à jour le schéma","Étiquette du circuit, schéma du tableau complété (S15)"),
      ("Fermer, déconsigner, essayer","Remettre le plastron, lever la consigne, essai de fonctionnement (S16)")],
     "Sources : S1, S7, S9, S14, S15, S16, S22. Déroulé pédagogique : le formateur le valide pour le contexte ADI.")
