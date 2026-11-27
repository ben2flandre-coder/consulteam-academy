"""Contenu éditorial commun aux versions HTML et PDF du livret apprenant."""
from pathlib import Path
import json,subprocess
ROOT=Path(__file__).resolve().parents[1]
PAGES=[]
def p(text):return {'type':'p','text':text}
def h(text):return {'type':'h','text':text}
def bullets(*items):return {'type':'list','items':items}
def table(headers,*rows):return {'type':'table','headers':headers,'rows':rows}
def alert(text):return {'type':'alert','text':text}
def notes(label='Mes repères terrain',lines=3):return {'type':'notes','label':label,'lines':lines}
def image(file,caption,height=160):return {'type':'image','file':file,'caption':caption,'height':height}
def link(label,url):return {'type':'link','text':label,'url':url}
def page(title,lead,*blocks,kicker='Fiche de formation'):
    PAGES.append({'title':title,'lead':lead,'kicker':kicker,'blocks':list(blocks)})

page('Mon livret de formation','Observer la situation, choisir la prévention, contrôler avant de s’engager.',
 p('Session 260053A · SECU37 · lundi 30 novembre 2026 · 7 heures · Consulteam Security, La Seyne-sur-Mer.'),
 alert('Ce livret accompagne les exercices et les démonstrations. Il ne constitue ni une autorisation de travail, ni une qualification de cordiste, ni une validation d’un montage antichute.'),
 h('Objectifs de la journée'),bullets('Repérer les risques de chute et les conditions d’accès au poste.','Donner la priorité à la suppression du risque puis aux protections collectives.','Choisir, contrôler et ajuster les EPI selon les notices.','Comprendre ancrage, tirant d’air, pendule et organisation des secours.','Réaliser les exercices d’ancrage et de nœuds prévus, sous contrôle du formateur.'),
 h('Comment travailler avec ce livret'),p('Lire la fiche, observer la démonstration, réaliser au sol, faire contrôler, puis noter ce qui s’applique à son poste. Les animations, vidéos et détails des sources restent accessibles sur la plateforme.'),notes('Nom / entreprise / poste / attentes',5),kicker='Avant de commencer')
page('Le parcours en un regard','Un repère pour retrouver les fiches et préparer la mise en pratique.',
 table(['Séquence','Contenu'],['Avant de monter','Méthode · réglementation · choix du système'],['Préparer le matériel','Harnais · contrôles · connecteurs · ancrage'],['Préparer le déplacement','Tirant d’air · pendule · continuité de protection'],['Atelier au sol','Huit · cabestan · demi-cabestan et mule · approfondissement'],['Anticiper et vérifier','Cordes · secours · cas pratiques · auto-évaluation'],['Après la formation','Plan d’action · notes · sources et crédits']),
 h('Trois questions avant chaque intervention'),bullets('Puis-je réaliser la tâche depuis une zone sûre ?','Quelles protections empêchent réellement la chute ?','Si une chute se produit malgré tout, le système et le secours sont-ils adaptés ?'),
 alert('Un doute sur un équipement, un ancrage ou une procédure impose d’arrêter et de demander. Une note de criticité basse ne compense jamais une protection manquante.'),notes('Les situations de mon activité à examiner',6),kicker='Sommaire')
page('Prévenir avant de s’équiper','L’équipement individuel s’intègre dans une organisation de travail.',
 table(['Étape','Ce que je recherche'],['1 · Définir','Tâche, durée, outils, manutentions et déplacements nécessaires.'],['2 · Repérer','Bords, trémies, surfaces fragiles, obstacles, tiers et coactivité.'],['3 · Évaluer','Sol, météo, visibilité, accès et contraintes de l’environnement.'],['4 · Choisir','Poste sûr, accès adapté et protection collective.'],['5 · Organiser','Système individuel si nécessaire, mode opératoire et secours.']),
 h('La hiérarchie à conserver'),bullets('Supprimer le travail en hauteur ou déplacer l’opération au sol quand c’est possible.','Prévoir un poste et un accès sûrs ; privilégier la protection collective.','Employer un système individuel approprié lorsque la protection collective ne peut pas être mise en œuvre.','Informer, former, vérifier et prévoir une intervention de secours.'),
 h('Situation à discuter'),p('Une intervention courte est prévue près d’une trémie non protégée. La durée limitée ne supprime pas le risque : quelles mesures permettent de réaliser le travail sans exposition ?'),notes('Mes mesures de prévention',5))
page('Les exigences à connaître','Relier les règles au choix concret du poste et du matériel.',
 table(['Référence','Conséquence pratique'],['L. 4121-1 et L. 4121-2','L’employeur organise la prévention ; la protection collective est prioritaire.'],['R. 4323-58 à R. 4323-61','Poste sûr et ergonomique. Si la protection collective est impossible : système d’arrêt de chute approprié, travailleur jamais seul et notice de l’employeur.'],['R. 4323-61','Chute libre ne dépassant pas 1 m, ou effets d’une chute de plus grande hauteur limités de façon équivalente.'],['R. 4323-68','Pas de travaux temporaires en hauteur si les conditions météo ou l’environnement compromettent la sécurité.'],['Arrêté du 19 mars 1993','Vérification périodique des systèmes antichute datant de moins de douze mois ; raccourcir l’intervalle si nécessaire.']),
 alert('Il n’existe pas de hauteur minimale générale qui dispenserait d’évaluer le risque de chute d’un niveau à un autre.'),
 h('Ce que je dois connaître sur mon site'),bullets('La consigne et les limites d’intervention.','Les personnes compétentes, les ancrages autorisés et le mode opératoire.','L’organisation d’alerte, de sauvetage et d’évacuation.'),notes('Consignes et interlocuteurs de mon entreprise',4))
page('Trois systèmes, trois objectifs','Identifier ce que le système doit accomplir avant de le choisir.',
 table(['Système','Objectif','Point de vigilance'],['Retenue','Empêcher d’atteindre la zone de chute.','Longueur et cheminement empêchent réellement l’accès au bord.'],['Maintien au poste','Travailler en appui ou en position définie.','Selon le risque, prévoir en plus un système distinct d’arrêt de chute.'],['Arrêt de chute','Arrêter une chute et retenir la personne.','Harnais, liaison, ancrage, espace libre et secours adaptés ensemble.']),
 h('Le système complet'),p('La compatibilité se vérifie pour l’ensemble : harnais, liaison, connecteurs, antichute, support et ancrage. Le marquage d’un élément ne valide pas leur combinaison.'),
 table(['Repères usuels','Fonction'],['EN 361','Harnais antichute'],['EN 358','Maintien au travail et retenue'],['EN 355','Absorbeur d’énergie'],['EN 362','Connecteurs']),
 alert('Une ceinture ou un point de maintien n’est pas automatiquement un point d’arrêt de chute. Les points de connexion et les combinaisons autorisées se lisent dans la notice.'),notes('Quel système pour mon exercice ? Pourquoi ?',5))
page('Ajuster le harnais','L’ajustement se vérifie avec la notice du modèle réellement utilisé.',
 bullets('Identifier le harnais, son marquage, sa taille et sa notice.','Examiner sangles, coutures, boucles et points d’attache avant de l’enfiler.','Enfiler sans vrille ; fermer chaque boucle selon son mécanisme.','Régler les sangles pour obtenir le maintien prévu, sans gêner les mouvements.','Identifier les points d’arrêt de chute et les distinguer des points de maintien.','Connecter uniquement aux points et selon les configurations autorisées.','Faire contrôler l’ajustement et les connexions par le binôme.'),
 h('Le contrôle croisé est observable'),table(['Je montre','Mon binôme vérifie'],['Chaque fermeture','Fermeture complète et verrouillage prévu.'],['Chaque sangle','Absence de vrille et réglage conforme.'],['Le point connecté','Fonction prévue par la notice et bon cheminement.']),
 alert('Le port d’un harnais ne suffit pas à protéger : il faut un système approprié et une procédure d’utilisation.'),notes('Modèle utilisé / réglages / points de vigilance',6))
page('Contrôler et décider du retrait','La vérification périodique complète le contrôle avant chaque emploi.',
 table(['Zone','À rechercher'],['Textiles','Coupures, abrasion, brûlures, contamination, coutures dégradées.'],['Pièces métalliques','Déformation, corrosion, fissure, fonctionnement anormal.'],['Connecteurs','Fermeture et verrouillage complets, axe de travail et absence d’appui parasite.'],['Liaison / absorbeur','État, longueur adaptée, témoin ou déclenchement, selon la notice.'],['Antichute et corde','Compatibilité, diamètre, sens de montage et essai prévu.'],['Identification','Étiquettes lisibles, fiche de vie, notice et vérification à jour.']),
 h('Une anomalie : quatre actions'),bullets('Arrêter l’utilisation.','Isoler et identifier le matériel pour empêcher sa réutilisation.','Signaler à la personne compétente.','Tracer l’événement et appliquer la décision conforme à la notice.'),
 alert('Un équipement ayant arrêté une chute est retiré de l’utilisation et traité selon la notice. Ne pas le remettre en service de sa propre initiative.'),notes('Anomalie repérée pendant l’atelier / décision',5))
page('Choisir l’ancrage','Distinguer le dispositif d’ancrage, son support et l’installation.',
 bullets('Identifier l’ancrage prévu par le mode opératoire.','Vérifier le support, l’installation et les limites d’utilisation.','Tenir compte du nombre d’utilisateurs et du sens des efforts.','Vérifier la compatibilité des connecteurs et éviter les arêtes et appuis parasites.','Placer l’ancrage pour limiter la chute et l’effet pendulaire, selon la configuration autorisée.'),
 h('Un contrôle ne remplace pas l’autre'),table(['Ce que je vois','Ce que je dois aussi savoir'],['Un anneau ou une structure','Le support et l’installation sont-ils évalués pour cet usage ?'],['Un équipement marqué','Est-il adapté à ce support et à cette configuration ?'],['Un nœud bien réalisé','Le montage complet est-il autorisé et contrôlé ?']),
 alert('Ne pas transformer une structure, une sangle de fortune ou un nœud d’exercice en ancrage antichute sans validation du système.'),notes('Ancrage retenu / support / vérification / limites',6))
page('Vérifier le tirant d’air','Comparer des distances mesurées depuis le même repère.',
 p('Le tirant d’air requis dépend du système et de sa configuration. Il se lit ou se détermine selon la notice : longueur de liaison, allongements, déformation d’ancrage, position de la personne et marge éventuelle suivent les règles du fabricant.'),
 table(['Vérification','À renseigner'],['Système et configuration de notice','______________________________________'],['Repère commun de mesure','______________________________________'],['Espace libre requis par la notice','________ m'],['Espace réellement disponible','________ m'],['Obstacles / pendule / arêtes','______________________________________']),
 h('Exemple de comparaison'),p('Valeurs fictives d’exercice, pour un même repère : 6,20 m requis et 5,60 m disponibles. Il manque 0,60 m. Cette configuration ne permet pas d’utiliser ce système à cet endroit.'),
 alert('Un espace disponible supérieur au besoin ne valide pas à lui seul le système. Examiner aussi ancrage, obstacles, pendule, compatibilité et secours. Il n’existe pas de formule universelle à appliquer à tous les matériels.'),notes('Mon calcul et les limites de la comparaison',5))
page('Préparer le déplacement','Conserver la protection pendant toute la manœuvre prévue.',
 h('Facteur de chute : un repère géométrique'),p('Dans le modèle simple, le facteur est le rapport entre hauteur de chute et longueur de liaison. Ce rapport ne fournit ni la force de choc, ni le tirant d’air, ni une autorisation d’utilisation.'),
 h('Pendule, obstacles et arêtes'),bullets('Un ancrage décalé peut conduire à un mouvement latéral et à un choc contre la structure.','Une corde ou une longe au contact d’une arête peut être endommagée. Vérifier les usages autorisés et les protections prévues.','Anticiper les transitions, l’accès, le cheminement et le retour ; appliquer la notice et la consigne du site.'),
 table(['Avant la transition','Question à résoudre'],['Continuité de protection','À quel moment et sur quel point la connexion est-elle transférée ?'],['Compatibilité du système','Quels points, connecteurs et chemins sont autorisés ?'],['Évolution de la situation','L’espace libre et le pendule restent-ils maîtrisés ?']),
 alert('Aucune démonstration au sol ne doit être transposée en hauteur sans vérifier le mode opératoire et les conditions réelles.'),notes('Une transition à expliquer au binôme',6))
page('Atelier : le huit tressé','Suivre le premier trajet, puis contrôler chaque paire de brins.',
 p('L’exercice se déroule au sol, sans personne ni charge suspendue. Le formateur montre la réalisation sur la corde et le point de connexion de l’atelier.'),
 image('assets/img/noeuds/huit-tresse-final.jpg','Tracé ouvert du huit tressé sur anneau : aide à la lecture du chemin, sans simulation du serrage.',170),
 bullets('Former un huit simple lâche en prévoyant assez de corde.','Passer le bout dans le point de connexion prévu.','Suivre le huit, brin contre brin, sans vrille ni croisement parasite.','Reprendre les brins pour serrer et aligner ; conserver le bout libre prescrit.','Faire contrôler : trajet complet, paires parallèles, serrage et connexion.'),
 alert('L’animation montre la progression le long d’un tracé ouvert. Le geste et le serrage s’apprennent sur corde réelle.'),notes('Ce que mon binôme m’a fait corriger',3))
page('Atelier : le cabestan','Reconnaître les deux tours et le croisement central.',
 image('assets/img/noeuds-libres/cabestan-reference.jpg','USCG PTC Developer · CC0 1.0 · Wikimedia Commons. Forme sur barre ; la sécurité complémentaire n’est pas représentée.',215),
 bullets('Effectuer un tour autour du support prévu.','Croiser le brin, puis effectuer le second tour dans le même sens.','Passer le bout sous le croisement selon la démonstration.','Ajuster, serrer et mettre la sécurité prévue pour l’exercice.','Faire contrôler les tours, le croisement, le support et le bout libre.'),
 alert('Le cabestan peut se desserrer sous charge variable. Le montage doit rester conforme au mode opératoire. La séquence de six photos du site montre une préparation à plat, avant installation sur support.'),notes('Mon contrôle croisé : acquis / à reprendre',4))
page('Atelier : demi-cabestan et mule','Freinage, blocage et sécurité complémentaire se distinguent.',
 image('assets/img/noeuds-libres/mule-reference.jpg','Markus Bärlocher · domaine public · Wikimedia Commons. Demi-cabestan, mule et nœud d’arrêt : photographie de repérage.',205),
 p('La démonstration du formateur et la référence vidéo Petzl donnent le cheminement à reproduire au sol. Une photo finale ne décrit pas toutes les opérations.'),
 bullets('Identifier le connecteur adapté et contrôler son orientation et son verrouillage.','Reconnaître le demi-cabestan et le brin de freinage.','Distinguer le nœud de mule et le nœud d’arrêt qui le sécurise.','Vérifier chaque étape avec le formateur avant l’essai prévu.'),
 alert('Ne pas relâcher le brin de freinage sur la seule foi d’une apparence de blocage. Appliquer la procédure enseignée et validée pour le système.'),notes('Les trois éléments que je dois savoir montrer',4))
page('Reconnaître les nœuds d’arrêt','Le type et le volume de l’arrêt doivent convenir au dispositif.',
 image('assets/img/noeuds-libres/arret-double-ouvert.jpg','Arrêt double ouvert : deux tours visibles. Markus Bärlocher · domaine public · Wikimedia Commons.',170),
 table(['Nœud','Repère visuel','Contrôle'],['Arrêt simple','Une boucle et un passage du bout.','Serrage et bout libre selon la notice.'],['Arrêt double','Un passage supplémentaire dans la boucle.','Tours réguliers et serrage.'],['Huit simple','Deux lobes formant un huit.','Trajet complet, sans vrille parasite.']),
 p('Le huit simple sert aussi de base au huit tressé. Ne pas confondre le nœud d’arrêt et la boucle finale obtenue en suivant le huit.'),
 alert('Un nœud d’arrêt n’est pas un amarrage. Un connecteur n’est pas un descendeur. L’aptitude de l’arrêt à empêcher le passage se vérifie avec la notice de l’appareil.'),notes('À quoi sert l’arrêt dans mon exercice ?',4))
page('Approfondir : le nœud de chaise','Une boucle fixe dont le trajet et la sécurité se contrôlent.',
 image('assets/img/noeuds-libres/chaise-etapes.png','Buz11 · CC BY-SA 4.0 · Wikimedia Commons. Les deux couleurs suivent une même corde. La sécurité complémentaire n’est pas dessinée.',185),
 bullets('Former la petite boucle sur le dormant.','Faire sortir le bout dans la boucle, contourner le dormant, puis revenir dans la boucle.','Serrer selon la démonstration et ajouter la sécurité prévue.','Vérifier le trajet, le bout libre et le risque de desserrage sous sollicitations intermittentes.'),
 alert('Cette planche sert à l’apprentissage au sol. Ne pas l’utiliser pour improviser l’encordement d’une personne. Le système et la procédure doivent explicitement prévoir le nœud utilisé.'),notes('Comparer ma réalisation à la planche',5))
page('Approfondir : pêcheur double et sangle','Deux jonctions différentes, pour des matériaux et des usages définis.',
 image('assets/img/noeuds-libres/pecheur-ouvert.jpg','Pêcheur double avant rapprochement. Malta · CC BY-SA 2.5 · Wikimedia Commons.',110),
 image('assets/img/noeuds-libres/pecheur-serre.jpg','Pêcheur double rapproché. Malta · CC BY-SA 2.5 · Wikimedia Commons.',100),
 h('Pêcheur double'),p('Deux nœuds se font face et se rapprochent sur les brins dormants. Vérifier le trajet, le serrage, les deux bouts libres et la compatibilité des cordes ou cordelettes avec l’usage prévu.'),
 h('Nœud de sangle'),p('Le second bout suit le nœud simple en sens inverse. La sangle reste à plat. Contrôler les quatre brins, le serrage et les longueurs de sortie prescrites.'),
 alert('Une sangle nouée d’exercice ne remplace pas une élingue cousue, identifiée et adaptée au dispositif antichute. Ne pas généraliser une longueur de bout libre à tous les matériaux.'),notes('Matériau, usage autorisé et consigne à retrouver',3))
page('Cordes : identifier et préserver','Une corde se choisit avec l’appareil et la fonction qu’elle doit remplir.',
 table(['Repère','À retenir'],['Corde dynamique · EN 892','Conçue pour absorber l’énergie dans les usages prévus.'],['Corde à faible allongement · EN 1891','Usages techniques prévus ; ne pas l’assimiler à une corde dynamique.'],['Compatibilité','Type, diamètre, état et appareil suivent les notices.'],['Contrôle','Examiner et palper suivant la notice ; rechercher coupure, écrasement, brûlure ou contamination.']),
 h('Après l’atelier'),bullets('Nettoyer et sécher selon les préconisations du fabricant.','Protéger de la chaleur, des UV, des produits chimiques et des arêtes.','Conserver l’identification et la traçabilité.','Isoler tout matériel douteux ou ayant subi un événement exceptionnel.'),
 alert('L’aspect extérieur ne suffit pas à conclure qu’une corde est utilisable. Ne pas réparer ou raccourcir un matériel sans appliquer les règles du fabricant et la procédure de gestion.'),notes('Corde / appareil / diamètre / consigne',6))
page('Préparer le secours avant de monter','Une personne suspendue doit être secourue rapidement, sans créer une seconde victime.',
 table(['Avant le travail','À définir et vérifier'],['Alerte','Qui alerte ? Quels moyens fonctionnent ? Quelle localisation transmettre ?'],['Accès','Comment les intervenants et secours accèdent-ils à la zone ?'],['Intervention','Qui est formé à la manœuvre de sauvetage ? Avec quel matériel ?'],['Organisation','Comment protéger la zone et empêcher une seconde chute ?'],['Entraînement','Comment la procédure est-elle testée sans exposition réelle ?']),
 h('Deux compétences à distinguer'),p('Le SST apporte les premiers secours. Sa formation ne remplace pas la compétence technique de décrochage et d’évacuation d’une personne suspendue. Les intervenants appliquent les procédures pour lesquelles ils sont formés et équipés.'),
 p('Pour l’emploi d’un système d’arrêt de chute, le travailleur ne doit jamais rester seul. Pour les travaux sur cordes, R. 4323-89 impose notamment une organisation permettant un secours immédiat et une formation spécifique aux procédures de sauvetage.'),
 alert('Ne pas improviser une descente, un décrochage ou une posture de prise en charge à partir d’une illustration. Alerter et appliquer les consignes et les compétences de secours adaptées.'),notes('Mon plan : qui / matériel / accès / alerte',5))
page('Trois situations à résoudre','Énoncés fictifs : expliquer la décision et les informations manquantes avant d’agir.',
 h('1 · Le matériel a subi une chute'),p('Le harnais paraît intact, mais il a arrêté une chute la veille. Un collègue propose de le reprendre pour une intervention courte.'),notes('Décision, motif et traçabilité',3),
 h('2 · L’espace libre ne suffit pas'),p('La notice exige 5,80 m dans la configuration retenue. La mesure donne 5,20 m depuis le même repère. Le chantier doit démarrer.'),notes('Décision et solution à rechercher',3),
 h('3 · Le secours reste imprécis'),p('Deux salariés sont équipés. Personne ne sait qui pourrait évacuer une victime suspendue et aucun matériel de sauvetage n’est identifié.'),notes('Conditions à réunir avant de commencer',3),
 p('Repères de correction : 1. Retirer le matériel et appliquer la notice ; tracer. 2. Refuser cette configuration et rechercher une solution adaptée. 3. Organiser un secours réalisable et vérifier les compétences et moyens avant l’exposition.'))


page('Lire la notice pour décider','Une référence précise, une configuration et des limites à retrouver.',
 table(['Information à rechercher','Ma preuve dans le document'],['Produit, référence, génération, édition','________________________________'],['Fonction et combinaisons autorisées','________________________________'],['Masse équipée et position de l’ancrage','________________________________'],['Liaison, connecteurs, espace libre et repère','________________________________'],['Obstacles, arêtes, déport et effets de la ligne','________________________________'],['Vérification, entretien et secours','________________________________']),
 alert('Une donnée indispensable absente ne se remplace pas par une valeur habituelle. Suspendre le choix jusqu’à une information exploitable.'),
 h('La construction ne détermine pas la fonction'),p('Toronnée, tressée ou âme-gaine décrit une construction. Le fabricant Kratos propose par exemple une longe HOPE FA3020015 en corde toronnée avec absorbeur. Ce contre-exemple ne rend utilisable aucun cordage inconnu : identifier produit, usage et compatibilité.'),
 link('Exemple fabricant : Kratos HOPE FA3020015','https://kratossafety.com/products/hope-longe-toronnee-1-50-m-en-fourche-avec-absorbeur-d-energie-et-mousquetons-fa5010117-et-fa5020755'),notes('Information manquante / interlocuteur / décision',4),kicker='Lecture de notice')
page('Longe double : le brin inutilisé','Vérifier toute la transition, y compris le stationnement du brin libre.',
 bullets('Identifier le modèle exact et sa génération.','Retrouver les connexions et les points de stationnement autorisés dans la notice.','Décrire la transition au sol, puis la réaliser sous observation.','Conserver la protection prévue pendant le transfert.','Éviter toute liaison parasite qui contrarie le fonctionnement du système.'),
 h('Un exemple documentaire à délimiter'),p('Petzl distingue des générations d’ABSORBICA-Y avant et depuis 2024 dans son explication du stationnement. La position autorisée et le fonctionnement ne se déduisent pas d’un dessin générique ; consulter la notice du matériel réellement utilisé.'),
 table(['Pendant l’atelier','Observation du binôme / formateur'],['Modèle et notice identifiés','________________________________'],['Point de stationnement montré','________________________________'],['Transition et limites expliquées','________________________________'],['Correction et nouvelle tentative','________________________________']),
 link('Petzl : stationnement du brin libre et générations ABSORBICA-Y','https://www.petzl.com/fr/fr/professionnel/conseils-techniques/les-basiques/longes-absorbica-y-et-porte-connecteur-de-longe-dantichute-sur-le-harnais/absorbica-pe04-lanyardparking_PRO_a77w0000000Gmx9AAC.html'),alert('Une démonstration regardée ou une vidéo consultée ne prouvent pas la maîtrise du geste. Le formateur renseigne ce qui a été réellement observé.'),notes('Mes points de vigilance',3),kicker='Atelier supervisé')
page('Décider et justifier · 1 / 2','Énoncés fictifs : aucune valeur ne décrit un matériel du site.',
 h('1 · Comparer depuis le même repère'),p('Une notice d’exercice demande 4,20 m depuis les pieds. Un relevé annonce 4,60 m depuis l’ancrage. Peut-on conclure ? Quelle information faut-il retrouver ?'),notes('Ma décision et sa justification',4),
 h('2 · Une combinaison incomplètement identifiée'),p('Harnais et antichute sont marqués. La corde ressemble à celle d’hier, mais sa référence et la combinaison prescrite ne sont pas établies. Que décider ?'),notes('Ma décision et sa justification',4),
 h('Critères de retour'),p('1. Refuser une comparaison directe de repères différents et demander une mesure exploitable. 2. Ne pas déduire la compatibilité de l’aspect ou du diamètre ; retrouver la référence prescrite. Discuter aussi ancrage, obstacles et secours.'),kicker='Raisonnement technique')
page('Décider et justifier · 2 / 2','Une condition manquante suffit à suspendre une configuration.',
 h('3 · Deux minutes, vingt fois'),p('La tâche sur échelle est courte et répétée vingt fois. Aucune impossibilité technique de protection collective n’est établie. Quelle condition manque dans la branche « risque faible et courte durée » ?'),notes('Ma décision et sa justification',4),
 h('4 · Une rubalise autour d’une surface fragile'),p('Le cheminement passe près d’un lanterneau ; rien n’empêche de le franchir. Quelle différence entre signalisation, exclusion effective et protection contre la chute ?'),notes('Ma décision et sa justification',4),
 h('Critères de retour'),p('3. La branche considérée exige aussi l’absence de caractère répétitif ; la courte durée ne suffit pas. 4. Une rubalise signale sans démontrer une protection. Revoir accès, circulation, zone d’exposition et mise en place des mesures.'),kicker='Raisonnement technique')

js="const fs=require('fs'),vm=require('vm');const c={window:{}};vm.runInNewContext(fs.readFileSync(process.argv[1],'utf8'),c);process.stdout.write(JSON.stringify(c.window.QCM));"
QCM=json.loads(subprocess.check_output(['node','-e',js,str(ROOT/'js/qcm-data.js')],text=True,encoding='utf-8'))
for start in [0,5]:
    blocks=[]
    for i,q in enumerate(QCM[start:start+5],start+1):
        blocks += [h(str(i)+' · '+q['q']),{'type':'options','items':[chr(65+j)+' · '+a for j,a in enumerate(q['o'])]}]
    page('Je vérifie mes acquis · '+('1 / 2' if start==0 else '2 / 2'),'Cocher une réponse par question. Les résultats pratiques sont appréciés séparément.',*blocks,kicker='Auto-évaluation')
page('Comprendre les réponses','Une bonne réponse doit pouvoir être expliquée avec la situation de travail.',
 *[p('<b>'+str(i+1)+' · Réponse '+chr(65+q['a'])+'.</b> '+q['e']) for i,q in enumerate(QCM)],notes('Mes points à reprendre avec le formateur',5),kicker='Correction commentée')
page('Mon plan d’action','Transformer les acquis en mesures observables sur mon poste.',
 table(['Situation / risque','Action prévue','Responsable / échéance'],['________________','________________','________________'],['________________','________________','________________'],['________________','________________','________________'],['________________','________________','________________']),
 h('Avant ma prochaine intervention'),bullets('Je retrouve la notice et le mode opératoire applicables.','Je vérifie les ancrages autorisés et les conditions de déplacement.','Je contrôle l’état du matériel et la vérification périodique.','Je connais la procédure d’alerte et les moyens de secours.'),
 notes('Ce que je dois demander à mon employeur',5),notes('Ce que je retiens et que je peux transmettre',4),kicker='Après la formation')
page('Notes et observations','Noter les corrections de l’atelier et les repères utiles pour le terrain.',notes('Mes notes',24),kicker='Mon aide-mémoire')
SOURCES=[
 ('Code du travail : principes de prévention L. 4121-1 et L. 4121-2','https://code.travail.gouv.fr/code-du-travail/l4121-2'),
 ('Travaux temporaires en hauteur : R. 4323-58 à R. 4323-61','https://code.travail.gouv.fr/code-du-travail/r4323-61'),
 ('Vérifications des systèmes antichute : arrêté du 19 mars 1993, articles 1 et 2','https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000179220/'),
 ('Organisation et sauvetage pour les travaux sur cordes : R. 4323-89','https://code.travail.gouv.fr/code-du-travail/r4323-89'),
 ('INRS : réglementation du travail en hauteur','https://www.inrs.fr/risques/chutes-hauteur/reglementation-travail-hauteur.html'),
 ('INRS : équipements de protection individuelle contre les chutes','https://www.inrs.fr/risques/chutes-hauteur/equipements-protection-individuelle-chutes-hauteur.html'),
 ('Petzl : calculateur de dégagement et limites des configurations','https://www.petzl.com/fr/fr/calculateur-de-degagement/clearancecalculator.html'),
 ('Petzl : demi-cabestan, mule et nœud d’arrêt','https://www.petzl.com/ca/fr/sport/conseils-techniques/les-basiques/video---demi-cabestan-avec-un-noeud-de-mule-et-noeud-darret/Video---Demi-cabestan-avec-un-noeud-de-mule-et-noe_SPO_a77bK000007VEnRQAW.html')]
page('Retrouver les sources','Sources du contenu révisé le 28 novembre 2026 ; notices à consulter pour le matériel utilisé.',
 *[link(label,url) for label,url in SOURCES],
 p('Les références détaillées et l’historique des corrections se trouvent dans la page « Traçabilité et sources » de la plateforme. Les textes en vigueur, notices et consignes du site prévalent sur cet aide-mémoire.'),
 notes('Mes notices et documents à retrouver',4),kicker='Références')
page('Crédits et limites des images','Des formes de référence pour observer, puis réaliser et contrôler au sol.',
 table(['Média du livret','Auteur','Licence'],['Cabestan sur barre','USCG PTC Developer','CC0 1.0'],['Mule avec arrêt / arrêt double','Markus Bärlocher','Domaine public'],['Planche du nœud de chaise','Buz11','CC BY-SA 4.0'],['Pêcheur double ouvert et serré','Malta','CC BY-SA 2.5']),
 p('Les images Wikimedia sont reproduites sans retouche de contenu ; certaines sont des prévisualisations. Les pages sources, fichiers originaux et liens de licence figurent dans les crédits en ligne. Conserver l’attribution, la licence et l’indication des modifications lors d’une réutilisation.'),
 p('Les tracés ouverts du huit et les animations de la plateforme facilitent la lecture du parcours de corde. Ils ne reproduisent ni le geste de nouage ni le serrage et ne valident aucune mise en charge.'),
 link('Crédits détaillés des nœuds','https://ben2flandre-coder.github.io/consulteam-academy/sessions/260053a/credits-noeuds.html'),
 h('Édition et conception'),p('Conception et ingénierie pédagogique : Benoît Deflandre. Consulteam Groupe · session 260053A. Version 2.0 du 28 novembre 2026. Validation Consulteam : en attente.'),
 p('Présentation reprise des livrets du dépôt Consulteam Supports : couverture bleu nuit et bandeau ambre, fiches apprenant, zones de notes, plan d’action et pagination continue.'),kicker='Médiathèque et édition')
