# Questions complémentaires (modules 3, 4, 5, 7, 8) : banque portée à 8 questions minimum par module. Contenu repris des sections des modules.
def Q(i,t,q,o,c,why): return dict(id=i,type=t,q=q,options=o,correct=c,why=why)
QC={
3:[
 Q("C03-01","s","Le métier d'un agent suffit-il à déterminer son symbole d'habilitation ?",["Oui, le métier décide","Non, ce sont les opérations confiées qui comptent","Oui, pour un agent de maintenance"],1,"Un même métier recouvre des missions de natures différentes ; le symbole se décide d'après l'opération [R]."),
 Q("C03-02","s","Une mission devient-elle élémentaire parce qu'elle est courte ou habituelle ?",["Oui","Non","Oui si elle est répétée chaque jour"],1,"La durée ou l'habitude ne changent pas la nature de l'opération [R]."),
 Q("C03-03","s","Que fait un agent dont la tâche dépasse son périmètre ?",["Il continue prudemment","Il décrit les faits, dit ce qui dépasse son périmètre et demande le relais prévu","Il demande à un collègue non habilité"],1,"Un refus utile décrit les faits et demande le relais prévu [R]."),
 Q("C03-04","m","Quels symboles concernent des opérations non électriques ?",["B0","H0","H0V","BR"],[0,1,2],"B0, H0 et H0V concernent des opérations d'ordre non électrique ; BR est une intervention générale en BT [R]."),
],
4:[
 Q("C04-01","s","Le symbole B0V existe-t-il ?",["Oui","Non","Oui pour les chantiers"],1,"Le symbole B0V n'existe pas ; le V de H0V concerne le voisinage renforcé HT [R]."),
 Q("C04-02","s","Une porte d'armoire est ouverte pendant le travail. Que faire ?",["Poursuivre sans y toucher","Suspendre l'activité, garder une position sûre et alerter le responsable","Refermer la porte soi-même"],1,"Une situation qui change impose une nouvelle décision [R]."),
 Q("C04-03","s","Peut-on déplacer un écran de protection électrique pour gagner de la place ?",["Oui si on est prudent","Non","Oui pendant une courte durée"],1,"Il ne faut pas déplacer soi-même une protection électrique [R]."),
 Q("C04-04","s","Qui organise la prévention d'un chantier non électrique dans son périmètre ?",["Le chargé de chantier","Tout exécutant","Le chargé de consignation"],0,"Le chargé de chantier organise la prévention dans son périmètre ; l'exécutant suit la conduite prévue [R]."),
],
5:[
 Q("C05-01","s","La recherche de panne est-elle une mission BS ?",["Oui","Non","Oui si le circuit est simple"],1,"La recherche de panne n'est pas une mission BS [R]."),
 Q("C05-02","s","Qui effectue la mise hors tension d'une intervention BS ?",["Le BS pour sa propre intervention","Un chargé de consignation uniquement","Un exécutant sous ses ordres"],0,"Le BS met hors tension pour sa propre intervention et n'a pas d'exécutant [R]."),
 Q("C05-03","s","Une étiquette douteuse suffit-elle à identifier un circuit ?",["Oui","Non, il faut interrompre et demander le relais si le doute persiste","Oui si elle est récente"],1,"Une étiquette douteuse n'est pas une identification [R]."),
 Q("C05-04","s","Un défaut est constaté à la remise en service. Que faire ?",["Commencer un dépannage","S'arrêter et rendre compte","Remettre en service quand même"],1,"Un défaut constaté impose l'arrêt, pas un dépannage [R]."),
],
7:[
 Q("C07-01","s","Un sectionneur peut-il couper une charge ?",["Oui toujours","Non, ne jamais le supposer","Oui en BT"],1,"Un interrupteur, un sectionneur et un disjoncteur n'ont pas des fonctions interchangeables [R]."),
 Q("C07-02","s","Le BE Manœuvre peut-il réparer l'installation ?",["Oui","Non, il exécute les manœuvres de sa mission","Oui si c'est rapide"],1,"Il ne répare pas et ne recherche pas la panne sur la seule base de ce symbole [R]."),
 Q("C07-03","s","Un organe se redéclenche après un réarmement autorisé. Que faire ?",["Réarmer jusqu'à ce que cela tienne","Suspendre, décrire le phénomène et faire prendre en charge","Neutraliser la protection"],1,"Un nouveau déclenchement est une information, il faut suspendre [R]."),
 Q("C07-04","s","La pression pour remettre vite un service en marche modifie-t-elle le périmètre de l'habilitation ?",["Oui","Non","Oui en cas d'urgence"],1,"Le périmètre de l'habilitation ne change pas avec la pression [R]."),
],
8:[
 Q("C08-01","s","Quelles sont les trois actions de l'INRS face à une personne électrisée ?",["Couper le courant, alerter, secourir","Toucher la victime, appeler un collègue, partir","Attendre, filmer, partir"],0,"Couper le courant sans toucher la victime, alerter, secourir en restant auprès d'elle [S31]."),
 Q("C08-02","s","Quels numéros d'alerte l'INRS cite-t-il ?",["15, 18 ou 112","17 uniquement","10 ou 20"],0,"Les secours s'alertent par le 15, le 18 ou le 112 [S31]."),
 Q("C08-03","s","Dans la phase protéger, quel est l'ordre à suivre face à un danger persistant ?",["Supprimer, puis isoler, puis soustraire la victime","Soustraire d'abord la victime","Alerter puis attendre"],0,"Supprimer le danger si possible, sinon l'isoler, sinon soustraire la victime [S33]."),
 Q("C08-04","s","Quand le dégagement d'urgence est-il justifié ?",["Pour tout danger","Danger réel, immédiat et non contrôlable qui menace la vie","Pour gagner du temps"],1,"C'est une manœuvre exceptionnelle réservée à ce cas [S33]."),
 Q("C08-05","s","La formation à l'habilitation électrique remplace-t-elle la formation SST ?",["Oui","Non, les gestes enseignés ne sont pas les mêmes","Oui pour les électriciens"],1,"Les gestes de l'habilitation ne remplacent pas ceux du SST [S34]."),
 Q("C08-06","s","La réglementation oblige-t-elle à former les habilités au SST ?",["Oui toujours","Non, c'est une décision de l'employeur après avis du médecin du travail","Oui au-delà de dix salariés"],1,"Il n'existe pas d'obligation ; la double compétence est recommandée [S34]."),
 Q("C08-07","s","Que fait-on d'abord face à une brûlure électrique, après protection et examen ?",["Appliquer une crème","Arroser à l'eau courante tempérée, puis alerter et surveiller","Percer les cloques"],1,"Arroser la zone, alerter les secours et surveiller la victime [S33]."),
 Q("C08-08","s","Peut-on appliquer un produit sur une brûlure sans avis médical ?",["Oui","Non","Oui si c'est un produit pharmaceutique"],1,"Aucun produit ne s'applique sans avis médical [S33]."),
 Q("C08-09","m","Quels dangers persistants analyse-t-on avant d'approcher la victime ?",["Mécanique","Électrique","Thermique ou incendie","Aucun, on approche directement"],[0,1,2],"Les dangers : mécanique, électrique, thermique, atmosphère irrespirable [S33]."),
],
}

QC[3].append(Q("C03-05","s","Un agent informatique peut-il utiliser un appareil et intervenir sur son alimentation avec la même habilitation ?",["Oui, c'est la même opération","Non, ce ne sont pas les mêmes opérations","Oui, si l'appareil est petit"],1,"Utiliser un appareil et intervenir sur une alimentation sont des opérations différentes [R]."))
QC[6]=[
 Q("C06-01","s","L'arrêt fonctionnel d'un appareil établit-il l'absence de tension ?",["Oui","Non","Oui après une minute"],1,"L'arrêt fonctionnel n'établit pas l'absence de tension [R]."),
 Q("C06-02","m","Quels outils ne remplacent pas la VAT ?",["Tournevis testeur","Détecteur sans contact","Voyant","Dispositif de VAT adapté"],[0,1,2],"Seul un dispositif prévu pour la VAT permet de conclure [R]."),
]
QC[10]=[
 Q("C10-01","s","Un BR seul permet-il de travailler sous tension ?",["Oui","Non, cela relève d'un symbole spécifique et de procédures dédiées","Oui en BT"],1,"Les travaux sous tension relèvent d'une habilitation spécifique (symbole T) [S29]."),
 Q("C10-02","s","Quelle est la limite de la connexion en présence de tension pour un BR ?",["500 V et 63 A en alternatif, hors charge","1000 V sans limite d'intensité","230 V et 10 A"],0,"Au maximum 500 V et 63 A en courant alternatif, hors charge [S29]."),
]
QC[17]=[
 Q("C17-01","s","Une pose de détecteur en hauteur ajoute :",["Un risque de chute à combiner avec la proximité de conducteurs","Aucun risque nouveau","Uniquement un risque thermique"],0,"La hauteur ajoute un risque de chute à organiser avec la proximité électrique [R]."),
 Q("C17-02","s","Qui fournit la liste des opérations d'ADI sécurité pour la session ?",["Elle est à fournir à partir de cas réels, l'employeur définissant le cahier des charges","Elle est connue d'avance","Le stagiaire seul"],0,"L'employeur définit les opérations, l'organisation et le matériel [S29]."),
]
QC[18]=[
 Q("C18-01","s","Jusqu'à quelle distance de la pièce nue sous tension s'étend la zone de voisinage (tension jusqu'à 50 kV) ?",["3 m","30 m","0,30 m"],0,"La zone de voisinage s'étend jusqu'à 3 m pour les tensions jusqu'à 50 kV, BT comprise [S26]."),
 Q("C18-02","s","Un B0 peut-il entrer en voisinage renforcé BT ?",["Oui avec surveillance","Non","Oui en zone 1"],1,"B0 n'est pas admis en voisinage renforcé BT [S26, R]."),
]
QC[19]=[
 Q("C19-01","s","Quelle est la sensibilité d'un différentiel en logement ?",["30 mA","300 mA","3 A"],0,"En logement, la sensibilité est de 30 mA [S3]."),
 Q("C19-02","s","À quoi sert la chambre de coupure d'un disjoncteur ?",["À disloquer l'arc électrique","À mesurer le courant","À commander le contacteur"],0,"La chambre de coupure disloque l'arc [S2]."),
]
QC[20]=[
 Q("C20-01","s","Comment calcule-t-on le pourcentage de déséquilibre ?",["Écart maximal à la moyenne divisé par la moyenne, fois cent","Somme des courants divisée par trois","Courant du neutre divisé par 400"],0,"Formule du déséquilibre [S13]."),
 Q("C20-02","s","Quelle tension mesure-t-on entre phase et neutre en triphasé 400 V ?",["230 V","400 V","110 V"],0,"230 V entre phase et neutre, 400 V entre deux phases [S21]."),
 Q("C20-03","s","Quelle limite du calcul d'équilibrage faut-il retenir ?",["Il suppose des charges résistives ; les harmoniques de rang 3 restent dans le neutre","Il est valable pour toutes les charges","Il remplace la mesure à la pince"],0,"Les harmoniques de rang 3 s'additionnent dans le neutre avec des charges non linéaires [S11, C]."),
]
QC[21]=[
 Q("C21-01","s","Quel contrôle effectue-t-on sur le VAT avant et après la vérification ?",["Un essai sur une source connue","Aucun","Un simple regard"],0,"Le VAT se contrôle avant et après sur une source connue [S16]."),
 Q("C21-02","s","Après remplacement d'un différentiel, comment l'essaie-t-on ?",["Avec le bouton test","En court-circuitant le circuit","On ne l'essaie pas"],0,"Pour un différentiel, utiliser le bouton test [S3, S4]."),
 Q("C21-03","s","Que faut-il vérifier avant de poser un calibre supérieur ?",["Que les conducteurs supportent l'intensité visée","Que l'appareil est de la même marque","Rien"],0,"Il faut vérifier que les conducteurs supportent l'intensité visée [S8]."),
]
QC[22]=[
 Q("C22-01","s","Ajouter un appareil dans un tableau est-il une simple opération de remplacement ?",["Non, cela modifie l'installation","Oui","Oui si le tableau est récent"],0,"Ajouter un appareil modifie l'installation [R]."),
 Q("C22-02","s","Sur quoi repose le choix du calibre ?",["Les conducteurs du circuit à protéger (NF C 15-100)","La couleur du disjoncteur","Le prix"],0,"Le calibre dépend des conducteurs du circuit à protéger [S8]."),
 Q("C22-03","s","Que doit dépasser le pouvoir de coupure ?",["Le courant de court-circuit présumé","Le calibre uniquement","La tension"],0,"Le pouvoir de coupure doit être supérieur au courant de court-circuit [S19, S20]."),
 Q("C22-04","s","Que fait-on avant de lever la consigne après la pose ?",["Remettre le plastron et repérer le circuit","Rien","Retirer le repérage"],0,"Repérer, remettre en place le plastron, lever la consigne, essayer [S15, S9, S16]."),
]

def declare(V):
    V.update({'300':('D','distracteur : sensibilité fausse (30 mA en logement)'),'110':('D','distracteur : tension fausse (230 V phase-neutre)')})

from q_niveaux import QN
for _k,_v in QN.items(): QC.setdefault(_k,[]).extend(_v)
