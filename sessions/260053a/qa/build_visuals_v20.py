"""Schémas pédagogiques originaux. Aucun dessin de matériel n'est une notice."""
from pathlib import Path
from html import escape as E
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'assets/svg/v20';OUT.mkdir(parents=True,exist_ok=True)
N='#102c53';B='#0b68ae';A='#f6b63d';G='#16744d';R='#b8322a';M='#52677d';P='#eef3f8'
def text(x,y,s,size=25,color=N,weight=500):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" font-weight="{weight}">{E(s)}</text>'
def lines(x,y,ss,size=25,color=N,gap=36):return ''.join(text(x,y+i*gap,s,size,color) for i,s in enumerate(ss))
def rect(x,y,w,h,fill=P,stroke='none',radius=14):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}" stroke-width="3"/>'
def line(x,y,a,b,color=B,width=5,dash=''):return f'<path d="M{x} {y} L{a} {b}" fill="none" stroke="{color}" stroke-width="{width}"'+(f' stroke-dasharray="{dash}"' if dash else '')+'/>'
def circle(x,y,r,fill=A,stroke='none'):return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="4"/>'
def arrow(x,y,a,b,color=B):return line(x,y,a,b,color)+f'<path d="M{a-10} {b-9} L{a} {b} L{a-10} {b+9}" fill="none" stroke="{color}" stroke-width="4"/>'
def doc(x,y,title,rows):
    z=rect(x,y,440,340,'#fff','#cbd8e5',5)+rect(x,y,440,65,N,radius=0)+text(x+22,y+43,title,26,'#fff',700)
    for i,(a,b) in enumerate(rows):z+=text(x+24,y+110+i*61,a,21,M)+text(x+24,y+138+i*61,b,25,N,700)
    return z
def save(name,title,subtitle,body,foot='Schéma de principe • à confronter à la notice et au site réel'):
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 620" role="img" aria-labelledby="title desc"><title id="title">{E(title)}</title><desc id="desc">{E(subtitle)}</desc><rect width="1100" height="620" fill="#fff"/><style>text{{font-family:Segoe UI,Arial,sans-serif}}path{{stroke-linecap:round;stroke-linejoin:round}}</style>{rect(0,0,14,620,A,radius=0)}{text(40,56,title,34,N,800)}{text(40,94,subtitle,23,M)}{body}{line(40,570,1060,570,'#d6e0ea',2)}{text(40,603,foot,19,M)}</svg>'''
    (OUT/(name+'.svg')).write_text(svg,encoding='utf-8')

save('responsabilites','Une responsabilité, une action, une preuve','La consigne relie l’organisation et le geste de l’utilisateur.',
    rect(42,140,490,370,N)+text(72,194,'ORGANISER',30,'#fff',800)+lines(72,250,['Évaluer la tâche et le poste','Choisir les moyens adaptés','Former et préparer le secours'],26,'#fff',64)+
    rect(566,140,490,370,P)+text(598,194,'APPLIQUER ET SIGNALER',28,N,800)+lines(598,250,['Contrôler avant chaque emploi','Respecter la configuration','Suspendre en cas de doute'],26,N,64)+
    text(72,477,'Consigne • notices • organisation',22,A)+text(598,477,'Contrôle • alerte • trace',23,B))

def roof(answer=False):
    z=rect(110,147,830,345,'#e6edf3',N,4)
    z+=line(110,147,940,147,G,11)+line(110,147,110,492,G,11)
    z+=rect(400,220,210,103,'#fff5d9',A,3)+text(422,263,'LANTERNEAU',23,N,700)+text(428,296,'surface fragile',20,M)
    z+=rect(760,360,120,86,'#fff',R,2)+text(772,411,'TRÉMIE',24,R,800)
    z+=rect(165,355,115,92,'#dcecf7',B,3)+text(180,410,'ACCÈS',24,B,700)
    z+=text(154,185,'Continuité de protection à prévoir' if answer else 'Protection périphérique partielle',23,G,700)
    if not answer:
        for x,y,n in [(965,244,'1'),(623,245,'2'),(890,406,'3'),(280,390,'4')]:z+=circle(x,y,24,A)+text(x-7,y+9,n,27,N,800)
        z+=text(120,535,'Où est l’exposition ? Quelles informations manquent ?',25,N,700)
    else:
        z+=line(940,147,940,492,G,11)+line(110,492,940,492,G,11)
        z+=rect(390,210,230,123,'none',G,6)+rect(749,350,143,106,'none',G,6)
        z+=line(282,403,350,403,B,13)+line(350,403,350,195,B,13)
        z+=text(125,535,'Accès • circulation • ouvertures • installation des protections',23,N,700)
    return z
save('toiture-enquete','Lire le poste avant de choisir un EPI','Cas d’exercice : ce plan ne constitue pas une installation validée.',roof())
save('toiture-correction','Protéger le parcours, puis le poste','Mesures à définir et à installer selon une procédure sécurisée.',roof(True),'Principes de correction • le trait vert ne décrit pas un dispositif homologué')

save('controle-chronologie','Trois moments, trois vérifications','Une vérification périodique à jour ne remplace pas l’examen d’usage.',
    line(100,230,990,230,B,8)+''.join(circle(x,230,23,c) for x,c in [(140,B),(550,N),(960,R)])+
    text(70,180,'AVANT L’EMPLOI',25,B,800)+text(407,180,'PÉRIODIQUEMENT',25,N,800)+text(790,180,'APRÈS ÉVÉNEMENT',24,R,800)+
    lines(65,307,['Utilisateur','État et fonctionnement','Compatibilité et suivi'],24,N,46)+
    lines(410,307,['Personne compétente','Vérification tracée','Moins de douze mois*'],24,N,46)+
    lines(785,307,['Chute, choc, doute…','Mise à l’écart','Décision selon la notice'],24,N,46)+
    rect(65,470,965,61,'#fff5d9')+text(86,509,'* Systèmes concernés par l’arrêté du 19 mars 1993 ; délai réduit si nécessaire.',22,N),
    'La notice, les conditions d’usage et l’historique complètent les exigences réglementaires')

save('notice-identification','Lire une notice, pas seulement un marquage','Document d’exercice : aucune référence ni valeur fabricant n’est inventée.',
    doc(45,146,'IDENTIFIER',[('Produit et référence','________________________'),('Génération / édition','________________________'),('Fonction du système','________________________'),('Historique / suivi','________________________')])+
    doc(600,146,'VÉRIFIER L’EMPLOI',[('Combinaisons autorisées','________________________'),('Masse et position d’ancrage','________________________'),('Limites et espace libre','________________________'),('Contrôles et secours','________________________')])+
    arrow(505,300,580,300,A)+text(81,535,'Une information essentielle absente impose de différer la décision.',26,R,700))

save('mesure-reperes','Deux distances, deux origines ?','Avant de comparer les valeurs, retrouver le repère de chaque mesure.',
    line(100,493,1030,493,N,9)+text(775,533,'Sol ou obstacle',23,N)+
    circle(305,174,14,B)+text(80,152,'ANCRAGE',23,B,800)+line(305,186,305,306,B,5)+
    circle(305,337,20,N)+line(305,356,305,413,N,10)+line(305,413,278,461,N,8)+line(305,413,332,461,N,8)+
    line(165,174,165,490,B,5)+text(66,332,'Depuis',23,B)+text(49,364,'l’ancrage',23,B)+
    line(456,462,456,492,R,7)+text(501,463,'Depuis les pieds',25,R,700)+
    rect(628,179,405,176,'#fff5d9')+lines(653,226,['Même repère de notice','Même obstacle considéré','Puis comparaison'],25,N,46),
    'Géométrie illustrative, sans échelle • aucune valeur de dégagement universelle')

save('pendule-double-vue','Un ancrage haut peut rester décalé','La hauteur et le déport latéral se vérifient séparément.',
    rect(43,146,486,365,P)+text(67,190,'VUE DE FACE',25,B,800)+line(110,447,480,447,N,9)+line(180,245,180,445,M,3,'9 10')+
    circle(180,245,13,B)+line(180,245,385,365,R,6)+circle(385,365,20,N)+
    '<path d="M385 365 Q335 430 220 448" fill="none" stroke="#b8322a" stroke-width="5" stroke-dasharray="10 9"/>'+
    rect(221,415,68,33,'#b7c8d8')+text(88,483,'Trajectoire et obstacle à examiner',23,R)+
    rect(570,146,486,365,'#f4f7fa')+text(596,190,'VUE EN PLAN',25,B,800)+circle(693,293,13,B)+
    line(693,293,693,450,M,3,'9 10')+line(693,293,937,390,R,6)+circle(937,390,20,N)+
    line(693,467,937,467,A,8)+text(750,440,'Déport latéral',24,N,700),
    'Trajectoire indicative • limites d’angle et d’emploi : notice du dispositif exact')

save('secours-organisation','Préparer la récupération avant de commencer','Le téléphone donne l’alerte ; il ne récupère pas la victime.',
    circle(548,331,109,N)+text(479,321,'SECOURS',30,'#fff',800)+text(484,361,'PRÉPARÉ',28,A,800)+
    rect(44,155,325,133,P)+lines(65,200,['Qui alerte ?','Lieu précis, accès, guidage'],23,N,40)+
    rect(731,155,325,133,P)+lines(752,200,['Qui intervient ?','Compétences et rôles définis'],23,N,40)+
    rect(44,374,325,136,P)+lines(65,418,['Avec quels moyens ?','Matériel prévu, disponible'],23,N,40)+
    rect(731,374,325,136,P)+lines(752,418,['Par quel chemin ?','Accès et procédure prévus'],23,N,40)+
    line(369,225,442,290,A)+line(656,290,731,225,A)+line(369,437,442,375,A)+line(656,375,731,437,A),
    'L’initiation et le SST ne constituent pas, seuls, une compétence de sauvetage technique')

save('longe-brin-libre','Le brin libre fait aussi partie du contrôle','Schéma fonctionnel : aucune position universelle sur le harnais.',
    rect(45,145,350,362,N)+text(72,195,'LIRE LA NOTICE',27,'#fff',800)+lines(72,253,['Référence et génération','Connexion au harnais','Stationnement autorisé','Limites de transition'],24,'#fff',55)+
    rect(470,173,186,70,P,B)+text(488,218,'ABSORBEUR',24,N,700)+
    '<path d="M656 207 C750 207 750 164 850 164 M656 207 C750 207 750 379 850 379" fill="none" stroke="#0b68ae" stroke-width="12"/>'+
    circle(862,164,22,'#fff',B)+circle(862,379,22,'#fff',B)+
    text(710,125,'Brin connecté au point autorisé',20,B,700)+
    text(735,432,'Brin inutilisé :',25,N,700)+text(695,470,'où le stationner ?',25,R,800)+
    text(470,534,'Ne pas créer de liaison parasite.',27,R,700),
    'Exemple documentaire : Petzl ABSORBICA-Y • se reporter au produit réellement utilisé')

save('echelle-exception','L’échelle : accès et exception de poste','R.4323-63 : les deux branches de l’exception ne se confondent pas.',
    rect(65,147,972,77,N)+text(99,195,'Le poste doit permettre un travail protégé et adapté.',30,'#fff',700)+
    rect(65,280,442,222,P)+text(90,329,'IMPOSSIBILITÉ TECHNIQUE',25,N,800)+lines(90,380,['de recourir à un équipement','assurant la protection collective','à établir dans la situation'],24,N,40)+
    text(535,393,'OU',27,B,800)+rect(602,280,435,222,'#fff5d9')+text(625,329,'ÉVALUATION DU RISQUE',25,N,800)+lines(625,380,['Risque faible','ET travaux de courte durée','ET sans caractère répétitif'],24,N,40),
    'Accès : stabilité, prévention du glissement, prise sûre et transfert protégés selon la situation')

save('apres-chute','Après l’arrêt d’une chute','L’alerte, la protection et la récupération préparée se coordonnent.',
    ''.join(rect(60+i*254,180,222,246,[N,'#e7eff7','#e8f4ed','#fff5d9'][i])+text(80+i*254,230,str(i+1),43,'#fff' if i==0 else B,800)+lines(80+i*254,298,ss,23,'#fff' if i==0 else N,37) for i,ss in enumerate([['ALERTER','Lieu exact','Durée, état'],['PROTÉGER','Éviter un','second accident'],['RÉCUPÉRER','Procédure prévue','Intervenants formés'],['ÉCARTER','Équipements','Traçabilité']]))+
    text(80,504,'Après récupération : examen et gestes selon la formation du secouriste.',24,N,700),
    'Aucun délai de suspension « sûr » • suivre les consignes du plan de secours et la régulation médicale')

save('observer-defauts','Observer, décrire, mettre à l’écart','Illustrations de signes : aucun seuil de rebut ne se déduit du dessin.',
    rect(48,154,310,260,P)+rect(395,154,310,260,P)+rect(742,154,310,260,P)+
    line(85,244,320,244,B,35)+line(194,220,175,263,'#fff',15)+line(195,223,211,265,R,4)+text(79,350,'Atteinte de la gaine',24,N,700)+
    line(435,250,663,250,B,36)+'<ellipse cx="548" cy="250" rx="48" ry="38" fill="#0b68ae"/>'+
    text(429,350,'Déformation localisée',24,N,700)+
    line(782,248,1015,248,B,35)+rect(845,214,70,68,'#7f8c99')+text(775,350,'Trace ou contamination',23,N,700)+
    lines(81,469,['Ce que je vois ≠ une cause certaine. Rechercher aussi l’historique.','Doute : suspendre l’usage, isoler, signaler et faire décider selon la notice.'],24,N,42),
    'Photographies réelles et procédure détaillée : document original de vérification Petzl, pages 3–4')

save('briefing-zone','Avant l’ouverture de la zone','Une inconnue critique non résolue maintient la zone fermée.',
    rect(52,151,410,350,N)+text(82,210,'POINT D’ARRÊT',34,'#fff',800)+lines(82,282,['Poste et accès protégés ?','Système documenté ?','Secours opérationnel ?'],25,'#fff',65)+
    rect(515,151,525,350,P)+text(544,209,'LE BRIEFING DOIT NOMMER',25,N,800)+lines(544,269,['La tâche et les limites','La configuration autorisée','Le signal d’arrêt','Les rôles et la conduite d’alerte'],25,N,59))

save('meteo-environnement','Surveiller ce qui change pendant le travail','Les critères de suspension se définissent pour la tâche et le matériel.',
    circle(169,235,47,A)+line(232,263,319,263,B,6)+line(241,289,307,289,B,6)+text(89,362,'Vent et météo',27,N,800)+
    '<path d="M441 266 Q505 160 559 266 Z" fill="#cad8e7"/>'+line(470,284,450,320,B,4)+line(520,284,500,320,B,4)+text(407,362,'Sol et adhérence',27,N,800)+
    rect(785,203,140,94,N)+line(810,225,899,225,A,5)+line(810,250,875,250,A,5)+text(735,362,'Tâche et visibilité',27,N,800)+
    rect(79,432,949,83,'#fff5d9')+text(105,481,'Notice + consignes du site + observation réelle = décision à réexaminer',24,N,700),
    'R.4323-68 • pas de seuil universel de vent inventé pour tous les équipements')

save('preuve-competence','Ce qui est observé peut être attesté','Le support consulté et le geste réalisé sont des preuves différentes.',
    rect(70,153,960,70,N)+text(94,198,'ACTIVITÉ',25,'#fff',800)+text(590,198,'TRACE DE L’OBSERVATION',25,'#fff',800)+
    ''.join(rect(70,237+i*76,960,65,P)+text(94,278+i*76,a,25,N,700)+text(590,278+i*76,b,24,B) for i,(a,b) in enumerate([('Démonstration regardée','Vu, sans maîtrise présumée'),('Geste essayé au sol','Essai et corrections notés'),('Critère démontré en situation','Acquis / EC / NA, contexte indiqué'),('Exercice non réalisé','Non observé, motif et suite')])) )

print('15 schémas originaux générés dans assets/svg/v20')
