# Documents de session A260E2A : émargement, satisfaction, avis après formation, attestation, compte rendu, grilles pratiques.
# Savoir-faire : INRS ED 6127 (déc. 2020) §5.4.2 pp. 34-35 [S29] ; avis après formation : §7.2 p. 39 [S29].
import html as _h
def _e(x): return _h.escape(str(x))
DATES=[('lundi 14 décembre 2026','14/12'),('mardi 15 décembre 2026','15/12'),('mercredi 16 décembre 2026','16/12')]
ENT="Consul Team Security · La Seyne-sur-Mer"
def _head(t,sub=''):
    return f'<header class="dh"><b>CONSUL TEAM</b> · Session A260E2A · Habilitation électrique, formation initiale<h2>{_e(t)}</h2>'+(f'<p class="expl">{sub}</p>' if sub else '')+'</header>'
def emargement():
    out=['<section class="doc" tabindex="0" id="emargement">'+_head("Feuille d'émargement par demi-journée","Une feuille par jour, signée par chaque stagiaire et par le formateur à chaque demi-journée (programme de 21 h). Lieu : "+ENT+". Matin 08:30-12:00, après-midi 13:30-16:30.")]
    for d,_ in DATES:
        rows=''.join('<tr><td></td><td></td><td></td><td class="sg"></td><td class="sg"></td></tr>' for _ in range(10))
        out.append(f'<h3>{_e(d)}</h3><table tabindex="0" class="dt"><thead><tr><th>Nom</th><th>Prénom</th><th>Entreprise</th><th>Matin<br><small>08:30-12:00</small></th><th>Après-midi<br><small>13:30-16:30</small></th></tr></thead><tbody>{rows}<tr class="fm"><td colspan="3"><b>Formateur : nom et signature</b></td><td class="sg"></td><td class="sg"></td></tr></tbody></table>')
    out.append('</section>'); return ''.join(out)
def satisfaction():
    items=["Accueil et organisation","Salle et matériel","Pertinence du contenu pour mon poste","Clarté des explications du formateur","Rythme de la formation","Qualité des travaux pratiques","Supports et plateforme de formation","Durée de la formation"]
    cols=['Très satisfaisant','Satisfaisant','Peu satisfaisant','Insatisfaisant']
    rows=''.join('<tr><td>'+_e(i)+'</td>'+''.join('<td class="ck">☐</td>' for _ in cols)+'</tr>' for i in items)
    return ('<section class="doc" tabindex="0" id="satisfaction">'+_head("Questionnaire de satisfaction à chaud","À remplir en fin de formation. Stagiaire (facultatif) : ………………………")+
     '<table tabindex="0" class="dt"><thead><tr><th>Votre appréciation</th>'+''.join(f'<th>{c}</th>' for c in cols)+f'</tr></thead><tbody>{rows}</tbody></table>'
     '<p><b>Les objectifs de la formation sont-ils atteints ?</b> ☐ Oui ☐ Plutôt oui ☐ Plutôt non ☐ Non</p>'
     '<p><b>Ce qui vous a le plus aidé :</b></p><div class="ln"></div><div class="ln"></div>'
     '<p><b>Ce qui pourrait être amélioré :</b></p><div class="ln"></div><div class="ln"></div>'
     '<p><b>Souhaits de formation complémentaire :</b></p><div class="ln"></div></section>')
def avis():
    return ('<section class="doc" tabindex="0" id="avis">'+_head("Avis après formation","Modèle fondé sur le contenu minimal de l'avis (INRS ED 6127 §7.2) [S29]. Un avis par stagiaire. L'habilitation est délivrée par l'employeur : cet avis l'éclaire, il ne l'accorde pas.")+
     '<table tabindex="0" class="dt kv"><tbody>'
     '<tr><th>Nom et prénom du stagiaire</th><td></td></tr>'
     '<tr><th>Type de formation suivie</th><td>☑ Initiale ☐ Recyclage</td></tr>'
     '<tr><th>Intitulé du stage</th><td>HE-BTHT-INI-21 Habilitation électrique, personnel électricien, initiale</td></tr>'
     '<tr><th>Date et lieu</th><td>14, 15 et 16 décembre 2026 · '+ENT+'</td></tr>'
     '<tr><th>Durées de formation</th><td>Théorique : …… h · Pratique : …… h (21 h dont 7 h de pratique)</td></tr>'
     '<tr><th>Formateur et organisme</th><td>Benoît Deflandre · Consul Team</td></tr>'
     '<tr><th>Symboles envisagés par l\'employeur</th><td></td></tr>'
     '<tr><th>Domaine de tension, attributs, champs d\'application</th><td>☐ BT ☐ HTA ☐ HTB · Attributs : …………………</td></tr>'
     '<tr><th>Évaluation des savoirs (QCM)</th><td>Score : …… % (seuil de référence 70 %)</td></tr>'
     '<tr><th>Évaluation des savoir-faire</th><td>Erreurs mineures : …… (2 au maximum) · Erreur majeure : ☐ aucune ☐ oui</td></tr>'
     '<tr><th>Avis sur les symboles envisagés</th><td>Symbole : ……… ☐ favorable ☐ réservé ☐ défavorable<br>Symbole : ……… ☐ favorable ☐ réservé ☐ défavorable<br>Symbole : ……… ☐ favorable ☐ réservé ☐ défavorable</td></tr>'
     '<tr><th>Symbole(s) recommandé(s) à l\'issue de la formation</th><td></td></tr>'
     '<tr><th>Informations utiles à l\'employeur</th><td><div class="ln"></div><div class="ln"></div></td></tr>'
     '<tr><th>Nom, fonction et signature du signataire</th><td>Benoît Deflandre, formateur<br><br></td></tr></tbody></table>'
     '<p class="expl">Le titre d\'habilitation est établi et signé par l\'employeur, qui reste responsable de la décision.</p></section>')
def attestation():
    return ('<section class="doc" tabindex="0" id="attestation">'+_head("Attestation individuelle de fin de formation")+
     '<p>Je soussigné, Benoît Deflandre, formateur pour <b>CONSUL TEAM</b>, atteste que :</p>'
     '<p class="big">Madame / Monsieur ………………………………………………</p>'
     '<p>a suivi l\'action de formation <b>HE-BTHT-INI-21 Habilitation électrique, personnel électricien, initiale</b>, organisée du 14 au 16 décembre 2026 à '+ENT+', pour une durée de 21 heures dont 7 heures de pratique.</p>'
     '<p><b>Nature de l\'action :</b> action de formation (acquisition de connaissances et de savoir-faire). <b>Objectifs :</b> identifier les dangers de l\'électricité, les zones d\'environnement et les mesures de prévention ; réaliser en sécurité les opérations correspondant aux symboles étudiés ; réagir en cas d\'accident ou d\'incendie d\'origine électrique.</p>'
     '<p><b>Résultats de l\'évaluation des acquis :</b> savoirs …… % · savoir-faire : ☐ validés ☐ non validés. Symboles étudiés : ……………………</p>'
     '<p class="expl">La présente attestation ne vaut pas titre d\'habilitation. Le titre d\'habilitation est délivré par l\'employeur, au vu de l\'avis après formation.</p>'
     '<p>Fait à ……………………, le ……………………<br><br>Signature du formateur :</p></section>')
def compte_rendu():
    out=['<section class="doc" tabindex="0" id="compte-rendu">'+_head("Compte rendu de formation, jour par jour","À remplir en fin de chaque journée et à transmettre au commanditaire.")]
    for i,(d,_) in enumerate(DATES,1):
        out.append(f'<h3>Jour {i} · {_e(d)}</h3><table tabindex="0" class="dt kv"><tbody><tr><th>Horaires effectifs</th><td>Matin …… à …… · Après-midi …… à ……</td></tr><tr><th>Stagiaires présents</th><td>…… sur ……  (voir émargement)</td></tr><tr><th>Modules traités</th><td></td></tr><tr><th>Travaux pratiques réalisés</th><td></td></tr><tr><th>Évaluations réalisées</th><td></td></tr><tr><th>Écarts au programme et incidents</th><td></td></tr><tr><th>Points d\'attention pour le lendemain</th><td></td></tr></tbody></table>')
    out.append('</section>'); return ''.join(out)
# --- grilles pratiques : savoir-faire par symbole (ED 6127 §5.4.2) [S29]
COMMUN=["Identifier les risques électriques sur ou à proximité d'une installation ou d'un ouvrage ; se déplacer et évoluer dans un environnement électrique","Avoir un comportement adapté à la situation (risques)","Rendre compte de l'opération réalisée, selon le cas, au chargé de chantier, de travaux, d'exploitation électrique, de consignation ou à l'employeur"]
GRILLES=[
 ("B0 · H0 · H0V Exécutant",["Maîtriser la manipulation de matériel et outillage dans un environnement électrique"]),
 ("B0 · H0 · H0V Chargé de chantier",["Baliser et surveiller la zone des opérations"]),
 ("B1 · B1V · H1 · H1V Exécutant",["Respecter les consignes de sécurité pour exécuter les travaux","Maîtriser la manipulation de matériel et outillage dans un environnement électrique","Identifier, vérifier et mettre en œuvre les équipements de protection individuelle","B1V et H1V : identifier, vérifier et mettre en œuvre les équipements de protection collective (nappe isolante, écran, etc.)"]),
 ("B2 · B2V · B2V Essai · H2 · H2V · H2V Essai Chargé de travaux",["Baliser et surveiller la zone des opérations","Préparer et diriger les travaux","Rédiger ou compléter les documents propres aux opérations","Identifier, vérifier et mettre en œuvre les équipements de protection individuelle","B2V et H2V : identifier, vérifier et mettre en œuvre les équipements de protection collective (nappe isolante, écran, etc.)"]),
 ("BS · Intervention BT élémentaire",["Réaliser une analyse préalable de l'intervention","Réaliser une intervention BT élémentaire (mise hors tension + vérification d'absence de tension) et réarmement d'un dispositif de protection","Identifier, vérifier et mettre en œuvre les équipements de protection individuelle"]),
 ("BR · Intervention BT générale",["Réaliser une analyse préalable de l'intervention","Réaliser une intervention BT générale avec nécessité de consignation et connexion ou déconnexion","Identifier, vérifier et mettre en œuvre les équipements de protection collective (nappe isolante, écran, etc.)","Identifier, vérifier et mettre en œuvre les équipements de protection individuelle"]),
 ("BC · HC Consignation",["Réaliser une analyse préalable de l'opération (consignation)","Réaliser une consignation en une étape","Rédiger ou compléter les documents propres aux opérations","Identifier, vérifier et mettre en œuvre les équipements de protection individuelle"]),
 ("BE · HE Manœuvre",["Réaliser une manœuvre d'exploitation ou de consignation dans le respect des instructions et documents (fiche de manœuvre, etc.)","Identifier, vérifier et mettre en œuvre les équipements de protection individuelle"]),
 ("BE · HE Mesurage · Vérification",["Réaliser un mesurage ou une vérification (examen visuel, essai, mesurage)","Identifier, vérifier et mettre en œuvre les équipements de protection individuelle"]),
 ("BE · HE Essai",["Baliser et surveiller la zone des opérations","Réaliser un essai et un mesurage, seul ou à plusieurs, et une consignation pour son propre compte","Identifier, vérifier et mettre en œuvre les équipements de protection individuelle"]),
]
def grilles():
    out=['<section class="doc" tabindex="0" id="grilles">'+_head("Grilles d'évaluation pratique par symbole","Source : INRS ED 6127 §5.4.2 [S29]. L'évaluation des savoir-faire se fait après l'évaluation positive des savoirs, à partir d'une ou plusieurs situations de travail ou d'intervention. Critères : sans erreur ; erreur mineure sans conséquence pour la sécurité des personnes ; erreur majeure avec conséquence directe pour la sécurité des personnes. Acceptation : deux erreurs mineures au maximum, aucune erreur majeure. La liste peut être complétée selon les opérations réalisées et l\'environnement. Liste à valider par le formateur.")]
    for t,l in GRILLES:
        rows=''.join(f'<tr><td>{_e(x)}</td><td class="ck">☐</td><td class="ck">☐</td><td class="ck">☐</td><td></td></tr>' for x in COMMUN+l)
        out.append(f'<div class="gr"><h3>{_e(t)}</h3><p class="expl">Stagiaire : ……………………… · Date : ………… · Situation observée : …………………………</p><table tabindex="0" class="dt"><thead><tr><th>Savoir-faire observé</th><th>Sans erreur</th><th>Erreur mineure</th><th>Erreur majeure</th><th>Observations</th></tr></thead><tbody>{rows}</tbody></table><p><b>Total :</b> erreurs mineures …… · erreur majeure ☐ non ☐ oui · <b>Savoir-faire</b> ☐ validés ☐ non validés</p></div>')
    out.append('</section>'); return ''.join(out)
def fiche_parcours():
    rows=''.join('<tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>' for _ in range(10))
    return ('<section class="doc" tabindex="0" id="parcours-individuel">'+_head("Fiche individuelle de parcours","À remplir par l'employeur avant la formation, pour chaque participant : fonctions exercées, opérations confiées, domaines de tension, symboles et attributs visés (programme HE-BTHT-INI-21, modalités d'entrée en formation).")+
     '<table tabindex="0" class="dt"><thead><tr><th>Nom, prénom</th><th>Fonction exercée</th><th>Opérations confiées</th><th>Domaine de tension (BT, HTA, HTB)</th><th>Symboles et attributs visés</th><th>Situation de handicap à signaler</th></tr></thead><tbody>'+rows+'</tbody></table>'
     '<p class="expl">Un parcours qui combine plusieurs spécialités ou domaines de tension fait l\'objet d\'une validation pédagogique préalable. Pour les symboles HT, le participant doit déjà posséder les compétences techniques nécessaires aux opérations réalisées sur ou dans l\'environnement d\'installations HTA ou HTB.</p>'
     '<h3>Accessibilité et situation de handicap</h3><p class="expl">La formation est accessible sous réserve de la compatibilité de la situation de handicap avec les fonctions, les opérations et les conditions d\'accès aux zones pratiques. Les besoins sont étudiés avec le référent handicap afin de déterminer les adaptations pédagogiques, techniques ou organisationnelles possibles. Le client signale avant la formation toute contrainte d\'accès, de sécurité ou d\'adaptation.</p></section>')
def page_html():
    nav='<nav class="no-print"><a href="#parcours-individuel">Fiche de parcours</a> · <a href="#emargement">Émargement</a> · <a href="#satisfaction">Satisfaction</a> · <a href="#compte-rendu">Compte rendu</a> · <a href="#grilles">Grilles pratiques</a> · <a href="#avis">Avis après formation</a> · <a href="#attestation">Attestation</a></nav>'
    return ('<small>DOCUMENTS DE SESSION</small><h1>Documents de session</h1><p class="lead">Documents à imprimer ou à remplir à l\'écran : émargement par demi-journée, questionnaire de satisfaction à chaud, compte rendu jour par jour, grilles d\'évaluation pratique par symbole, avis après formation et attestation de fin de formation. Ce sont des modèles de travail, à valider par le formateur et le commanditaire avant usage.</p>'
      '<p class="no-print"><button type="button" onclick="window.print()">Imprimer cette page</button></p>'+nav+fiche_parcours()+emargement()+satisfaction()+compte_rendu()+grilles()+avis()+attestation())
CSS='''<style>.doc{margin:1.4rem 0;padding:1rem 1.2rem;border:1px solid var(--l);border-radius:10px;background:#fff;color:#16273d;page-break-after:always}.dh{border-bottom:3px solid #102c53;margin-bottom:.8rem}.dh h2{margin:.2rem 0}.dt{width:100%;border-collapse:collapse;margin:.5rem 0}.dt th,.dt td{border:1px solid #8a97a8;padding:.45rem .5rem;text-align:left;vertical-align:top;font-size:.92rem}.dt thead th,.dt th{color:#16273d!important;background:#e8eef6}.dt td.sg{width:20%;height:2rem}.dt td.ck{text-align:center;width:9%;font-size:1.1rem}.dt tbody tr{height:2rem}.kv th{width:34%;background:#f1f5fa!important}.ln{border-bottom:1px solid #8a97a8;height:1.7rem}.big{font-size:1.2rem}.gr{margin:1rem 0;page-break-inside:avoid}.fm td{background:#f1f5fa}@media print{.no-print,header.top,.fab,nav.nav,.skip{display:none!important}.doc{border:none;padding:0}body{background:#fff}}</style>'''
