# Modules 19 à 22 : appareillage d'un tableau électrique. Texte, questions et déclaration des valeurs chiffrées.
# Niveaux de preuve : S = source lue ou extrait cité ; C = calcul prouvé par script ; R = principe de raisonnement à valider par le formateur ;
# D = distracteur de QCM, volontairement faux.

def Q(i,t,q,o,c,why): return dict(id=i,type=t,q=q,options=o,correct=c,why=why)

M19=dict(id=19,title="Reconnaître l'appareillage d'un tableau et son fonctionnement",scope="Tous niveaux",niveaux=["Tous"],statut="nouveau",
 goal="Nommer les appareils usuels d'un tableau de répartition, dire à quoi ils servent, comment ils fonctionnent et ce qu'ils ne garantissent pas.",
 scenario="Vous ouvrez le capot d'un tableau de répartition : plusieurs rangées d'appareils, un peigne, des borniers. Avant de toucher à quoi que ce soit, vous devez dire ce que vous voyez et à quoi cela sert.",
 figures=[["images/schemas/F1-facade-tableau.svg","Vue de face d'un tableau de répartition à deux rangées, légendée (schéma de principe)."],
          ["images/schemas/F2-coupe-disjoncteur.svg","Coupe d'un disjoncteur modulaire : bilame, bobine, contacts, chambre de coupure, clip de fixation."],
          ["images/schemas/F3-principe-differentiel.svg","Principe d'un interrupteur différentiel : tore, relais, bouton test."],
          ["images/schemas/F4-coupe-contacteur.svg","Coupe d'un contacteur au repos : bobine, circuit magnétique, armature, contacts."]],
 sections=[
 ["Lire un tableau de l'amont vers l'aval","Un tableau de répartition se lit de l'amont vers l'aval : l'arrivée, les protections de tête, puis les départs vers les circuits [S6]. Les rangées sont alimentées par un peigne, la terre et le neutre vont sur des borniers [S6, R]. La disposition varie d'un tableau à l'autre : appuyez-vous sur les repères et sur le schéma du tableau, pas seulement sur la place des appareils [R]."],
 ["Le disjoncteur divisionnaire","Il protège un circuit [S2]. Il contient trois organes [S2] : une bobine électromagnétique qui réagit au court-circuit en moins de 0,02 s, un bilame qui réagit à la surcharge en deux minutes à plusieurs minutes, et une chambre de coupure qui disloque l'arc électrique. Entre les deux bornes, on trouve dans l'ordre le bilame, la bobine avec son noyau, le contact mobile, puis les chambres de coupure [S10]."],
 ["Courbe et pouvoir de coupure","La courbe indique à partir de quel multiple du calibre le déclencheur magnétique agit : les courbes B, C, D, K et Z existent [S20], et pour la courbe B, le magnétique agit entre 3 et 5 fois le calibre [S19]. Le pouvoir de coupure du disjoncteur doit être supérieur au courant de court-circuit présumé à son emplacement [S7]."],
 ["L'interrupteur différentiel","Il compare le courant qui part et le courant qui revient ; un écart signale une fuite vers la terre et provoque le déclenchement [S3]. En logement, la sensibilité est de 30 mA [S3]. Le bouton test (T) alimente un circuit d'essai qui dérive un courant en dehors du tore [S4]. Il ne protège pas contre la surcharge ni le court-circuit : c'est le rôle du disjoncteur en aval [S4]. Les types AC et A se distinguent par les courants de fuite qu'ils détectent [S3]."],
 ["Contacteur, télérupteur, minuterie, parafoudre","Le contacteur ferme ses contacts quand sa bobine est alimentée et les rouvre par un ressort quand elle est coupée [S5]. Il a des contacts de puissance et des contacts auxiliaires [S17]. Le télérupteur commande un circuit par impulsions, la minuterie coupe après un délai, le parafoudre limite les surtensions d'origine atmosphérique [S6, R]. Repérez la fonction de chaque appareil avant toute intervention [R]."],
 ["Ce que la position d'un appareil ne prouve pas","Un appareil en position ouvert ne prouve pas que l'aval est hors tension [R]. Seule la vérification d'absence de tension, sur tous les conducteurs actifs, neutre compris, permet de conclure [S16, S22]."]],
 decision="Un collègue vous dit : « le disjoncteur est sur OFF, tu peux y aller ». Que répondez-vous ?",
 answer="Que la position OFF ne suffit pas : on sépare, on condamne, on identifie, puis on vérifie l'absence de tension, neutre compris, avant d'intervenir [S16, S22].",
 check=["Ai-je identifié chaque appareil et son rôle ?","Le repérage et le schéma du tableau sont-ils lisibles ?","Ai-je vérifié l'absence de tension, sans me fier à la position des appareils ?"],
 source="Sources S2, S3, S4, S5, S6, S7, S10, S16, S17, S19, S20, S22 (voir le registre). Schémas F1 à F4 : dessins Consul Team, non à l'échelle.",
 note="Module nouveau, à valider par le formateur. Les appareils réels diffèrent selon les marques et les tableaux.",
 questions=[
  Q("T19-01","s","Dans un disjoncteur, quel organe réagit aux surcharges lentes ?",["Le bilame","La bobine électromagnétique","La chambre de coupure"],0,"Le bilame se dilate à la chaleur et déclenche [S2]. La bobine répond au court-circuit, la chambre disloque l'arc [S2]."),
  Q("T19-02","s","Quel organe provoque le déclenchement en moins de 0,02 s en cas de court-circuit ?",["La bobine électromagnétique","Le bilame","Le bouton test"],0,"La bobine électromagnétique abaisse la manette, déclenchement inférieur à 0,02 s [S2]."),
  Q("T19-03","m","Quelles affirmations sur l'interrupteur différentiel sont exactes ?",["Il compare le courant aller et le courant retour","En logement, sa sensibilité est de 30 mA","Il protège contre la surcharge et le court-circuit","Le bouton test permet de vérifier son fonctionnement"],[0,1,3],"Comparaison des courants et 30 mA [S3], bouton test [S3, S4]. Il ne protège pas contre la surcharge ni le court-circuit [S4]."),
  Q("T19-04","s","Le pouvoir de coupure d'un disjoncteur doit être :",["Supérieur au courant de court-circuit présumé à son emplacement","Inférieur au calibre","Égal à la section du câble"],0,"Pouvoir de coupure supérieur au courant de court-circuit [S7]."),
  Q("T19-05","s","Un disjoncteur est sur OFF. Pouvez-vous en conclure que l'aval est hors tension ?",["Non : il faut vérifier l'absence de tension","Oui, c'est suffisant","Oui, si le différentiel est aussi ouvert"],0,"Seule la VAT, neutre compris, permet de conclure [S16, S22]."),
  Q("T19-06","s","Quand la bobine d'un contacteur est alimentée :",["L'armature est attirée et les contacts se ferment","Le ressort ouvre les contacts","Le bilame se dilate"],0,"Bobine alimentée : l'armature est attirée, les contacts se ferment [S5]. Bobine coupée : le ressort les rouvre [S5]."),
 ])

M20=dict(id=20,title="Équilibrer un tableau triphasé et comprendre pourquoi",scope="Tous niveaux",niveaux=["Tous"],statut="nouveau",
 goal="Expliquer l'intérêt d'équilibrer les phases, répartir des circuits monophasés sur trois phases et contrôler le résultat.",
 scenario="Un tableau triphasé alimente huit circuits monophasés. Trois d'entre eux sont sur la même phase, deux sur une autre, trois sur la dernière. On vous demande de les répartir pour équilibrer le tableau.",
 figures=[["images/schemas/F6-equilibrage-avant-apres.svg","Exemple chiffré fictif : courants par phase avant et après répartition, neutre et déséquilibre (calcul prouvé par script)."]],
 sections=[
 ["Pourquoi équilibrer","Avec des charges monophasées, le courant dans le neutre correspond au déséquilibre entre phases [S12]. Plus le déséquilibre est fort, plus le neutre est sollicité [S12, R]. Un déséquilibre pénalise aussi les moteurs (couple, surintensité, surchauffe) et peut signaler des connexions desserrées ou des contacts usés [S13]. Équilibrer répartit la charge pour limiter ces effets [R]."],
 ["La tension et le neutre","Dans un réseau triphasé avec neutre, on mesure 230 V entre une phase et le neutre, 400 V entre deux phases [S21]. Les trois courants de phase sont décalés ; leur somme vectorielle passe dans le neutre [C]. Trois courants égaux de 10 A, avec des charges résistives, donnent 0 A dans le neutre ; tous les circuits sur une seule phase, 76 A au total, donnent 76 A dans le neutre [C]."],
 ["Mesurer le déséquilibre","Le pourcentage de déséquilibre se calcule ainsi : écart maximal à la moyenne, divisé par la moyenne, multiplié par cent [S13]. La moyenne des trois courants de l'exemple est de 25,33 A [C]."],
 ["Exemple chiffré fictif","Huit circuits de 16, 16, 10, 10, 8, 6, 6 et 4 A, charges résistives [C]. Avant : 42, 18 et 16 A par phase, neutre à 25,06 A, déséquilibre de 65,8 % [C]. Après répartition : 24, 26 et 26 A, neutre à 2,0 A, déséquilibre de 5,3 % [C]. Ce résultat est le meilleur possible parmi les 6561 répartitions testées par le script [C]."],
 ["Méthode","Lister les courants d'emploi des circuits ; les classer du plus fort au plus faible ; brancher chacun sur la phase la moins chargée à cet instant ; contrôler à la pince ampèremétrique, en charge normale ; repérer chaque circuit avec sa phase [R]. Respecter l'habilitation et les règles de sécurité de l'intervention : déplacer un circuit est une opération sur l'installation [S1]."],
 ["Une limite à connaître","Des phases équilibrées ne suppriment pas les courants harmoniques de rang 3 et multiples, qui s'additionnent dans le neutre avec des charges non linéaires (informatique, éclairage électronique) [S11]. Le calcul ci-dessus suppose des charges résistives [C]."]],
 decision="Les trois phases d'un tableau portent 42, 18 et 16 A. Que proposez-vous et que contrôlez-vous ensuite ?",
 answer="Répartir les circuits du plus fort au plus faible sur la phase la moins chargée, puis mesurer les courants de phase et du neutre en charge normale ; sur l'exemple, on passe à 24, 26 et 26 A [C].",
 check=["Ai-je les courants d'emploi réels des circuits ?","Mon intervention entre-t-elle dans mon habilitation ?","Ai-je mesuré avant et après, en charge normale ?","Les phases sont-elles repérées sur chaque départ ?"],
 source="Sources S1, S11, S12, S13, S21 ; calcul : preuves/calcul-equilibrage.json (script src/calc_equilibrage.py). Exemple fictif.",
 note="Module nouveau, à valider par le formateur. Les valeurs de l'exemple sont fictives ; la méthode est un principe de raisonnement.",
 questions=[
  Q("T20-01","s","Trois phases chargées chacune à 10 A (charges résistives). Quel courant circule dans le neutre ?",["0 A","10 A","30 A"],0,"Trois courants égaux et décalés de manière régulière s'annulent dans le neutre [C]."),
  Q("T20-02","s","Tous les circuits (76 A au total) sont branchés sur la même phase. Quel courant dans le neutre ?",["76 A","25 A","0 A"],0,"Un seul courant de phase revient entièrement par le neutre [C]."),
  Q("T20-03","s","Dans l'exemple, quels sont les courants par phase après répartition ?",["24, 26 et 26 A","42, 18 et 16 A","25, 25 et 26 A"],0,"Après répartition : 24, 26 et 26 A, neutre à 2,0 A [C]."),
  Q("T20-04","s","Moyenne 25,33 A, phase la plus chargée à 42 A. Quel est le déséquilibre ?",["65,8 %","16,7 %","60,3 %"],0,"(42 − 25,33) ÷ 25,33 × 100 ≈ 65,8 % [S13, C]. 16,7 est l'écart en ampères, 60,3 le rapport moyenne sur maximum [C]."),
  Q("T20-05","s","Des phases bien équilibrées garantissent-elles un neutre sans courant ?",["Non : les harmoniques de rang 3 s'additionnent dans le neutre","Oui, toujours","Non, seulement avec des moteurs"],0,"Les harmoniques de rang 3 et multiples s'additionnent dans le neutre [S11]."),
 ])

M21=dict(id=21,title="Remplacer un appareillage dans un tableau",scope="BS · BR · BE (périmètre à vérifier)",niveaux=["BS","BR","BE"],statut="nouveau",
 goal="Remplacer un appareil par un appareil équivalent, en sécurité, dans le cadre de l'habilitation détenue.",
 scenario="Un disjoncteur ne se réarme plus. Le tableau est en service. On vous demande de le remplacer.",
 figures=[["images/schemas/F5-coupe-rail-peigne.svg","Coupe d'une rangée : appareil sur rail, peigne, bornes et levier sur la griffe."],
          ["images/schemas/F7-remplacement-appareil.svg","Les huit étapes du remplacement d'un appareil."]],
 sections=[
 ["Cadrer : ai-je le droit ?","La page de l'INRS lue décrit pour le BS le remplacement à l'identique d'un fusible ou le réarmement d'un dispositif de protection, et pour le BR le dépannage et le remplacement d'un matériel défectueux [S1]. Elle ne cite pas le remplacement d'un élément d'armoire : le périmètre exact se vérifie dans le titre d'habilitation, la NF C 18-510 (non lue ici) et les consignes de l'employeur [S1]."],
 ["Diagnostiquer avant de remplacer","Un disjoncteur qui ne se réarme pas est peut-être défectueux, ou le défaut de l'installation persiste : vérifier d'abord la cause [S8]. Relever les caractéristiques de l'appareil : calibre, courbe, pouvoir de coupure, type de différentiel [S7, S8]."],
 ["Consigner et vérifier l'absence de tension","Séparer, condamner, identifier, vérifier l'absence de tension [S22]. La VAT porte sur tous les conducteurs actifs, neutre compris, et le VAT se contrôle avant et après sur une source connue [S16]."],
 ["Déposer","Disjoncteur à vis : dévisser les quatre vis, puis extraire l'appareil en faisant levier sur la griffe de fixation ; si un peigne l'alimente, desserrer les vis du haut de tous les disjoncteurs de la rangée [S8]. Disjoncteur à bornes automatiques : retirer le peigne avec un tournevis en levier, appuyer sur les poussoirs pour libérer les fils, puis extraire l'appareil en faisant levier sur la griffe [S8]. Repérer les fils avant de les retirer [R]."],
 ["Poser et raccorder","Clipser le nouvel appareil sur le rail à l'emplacement libéré, relier par fils ou peigne en haut et par fils en bas [S8]. Pour un calibre supérieur, vérifier d'abord que les conducteurs supportent l'intensité visée [S8]. Appareil équivalent : même calibre, même courbe, pouvoir de coupure au moins égal [R]."],
 ["Repérer, déconsigner, essayer","Mettre à jour le repérage du circuit [S15]. Lever la consigne dans l'ordre prévu, puis essayer l'appareil ; pour un différentiel, utiliser le bouton test [S3, S4]."],
   ["Limites du BS et du BR","La brochure INRS ED 6127, 3e édition de décembre 2020, décrit le BS comme une intervention élémentaire sur des circuits terminaux, au maximum 400 V et 32 A en courant alternatif, hors tension et en l'absence de voisinage renforcé [S29]. Elle décrit le BR avec, pour connecter ou déconnecter en présence de tension, au maximum 500 V et 63 A en courant alternatif, et hors charge [S29]. L'édition de 2012 indiquait pour le BR « maxi 1000 V et 63 A » et ne disait pas hors charge : cette mention n'apparaît plus dans le tableau de 2020 [S30]. Une section de 6 mm² en cuivre figure pour le BS et le BR dans deux sources secondaires issues de l'INRS, pas dans la brochure [S23, S24]. L'INRS renvoie la portée exacte des symboles à la NF C 18-510 [S29, S28], dont le texte payant, y compris ses amendements A1 et A2 en vigueur [S27], n'a pas été lu : confirmer ces valeurs à la norme avant de les enseigner comme limites réglementaires [R]."]],
 decision="Le disjoncteur à remplacer est sur un peigne, avec des bornes automatiques. Par où commencez-vous la dépose, une fois le tableau consigné ?",
 answer="Par le retrait du peigne d'alimentation en partie haute, puis les poussoirs des bornes, puis le levier sur la griffe [S8].",
 check=["Mon titre couvre-t-il cette opération ?","Ai-je relevé calibre, courbe, pouvoir de coupure ?","VAT faite, neutre compris, VAT contrôlé avant et après ?","Fils repérés avant dépose ?"],
 source="Sources S1, S3, S4, S7, S8, S15, S16, S22. Schémas F5 et F7 : dessins Consul Team, non à l'échelle.",
 note="Module nouveau, à valider par le formateur. Le périmètre d'habilitation reste à confirmer à la NF C 18-510.",
 questions=[
  Q("T21-01","s","Un disjoncteur ne se réarme pas. Que faire en premier ?",["Vérifier la cause : l'appareil est peut-être défectueux, ou le défaut persiste","Le remplacer aussitôt","Le forcer en position marche"],0,"Diagnostic d'abord [S8]."),
  Q("T21-02","s","Vous remplacez un disjoncteur par un calibre supérieur. Que vérifiez-vous d'abord ?",["Que les conducteurs du circuit supportent l'intensité visée","La couleur du boîtier","Rien de particulier"],0,"Vérifier les conducteurs avant de passer à un calibre supérieur [S8]."),
  Q("T21-03","o","Remettez dans l'ordre les étapes du remplacement :",["Consigner (séparer, condamner, identifier)","Vérifier l'absence de tension","Déposer l'ancien appareil","Poser l'appareil équivalent","Raccorder et repérer","Déconsigner et essayer"],[0,1,2,3,4,5],"Consignation et VAT d'abord [S22, S16], dépose et pose [S8], repérage [S15], déconsignation et essais [S3]."),
  Q("T21-04","m","Quelles affirmations sur la VAT sont exactes ?",["Elle porte sur tous les conducteurs actifs, neutre compris","Le VAT se contrôle avant et après la mesure","La position OFF du disjoncteur la remplace","Elle se fait avant de déposer l'appareil"],[0,1,3],"VAT neutre compris, contrôle du VAT avant et après [S16], avant d'intervenir [S22]. La position OFF ne la remplace pas [S16]."),
  Q("T21-05","s","Disjoncteur à bornes automatiques, alimenté par un peigne. Première action de dépose ?",["Retirer le peigne d'alimentation en partie haute","Tirer sur les fils","Dévisser les quatre vis du bas"],0,"Retirer le peigne, puis les poussoirs, puis le levier sur la griffe [S8]."),
 ])

M22=dict(id=22,title="Installer un nouvel appareillage dans un tableau",scope="Périmètre à vérifier (modification de l'installation)",niveaux=["BR","BE"],statut="nouveau",
 goal="Ajouter un appareil dans un tableau : cadrer l'opération, choisir l'appareil, le poser, le raccorder, le repérer, l'essayer.",
 scenario="Un nouveau circuit doit être protégé dans un tableau existant. Il reste des emplacements libres sur la rangée.",
 figures=[["images/schemas/F8-installation-appareil.svg","Les huit étapes de l'installation d'un nouvel appareil."],
          ["images/schemas/F5-coupe-rail-peigne.svg","Coupe d'une rangée : appareil sur rail, peigne, bornes et levier sur la griffe."]],
 sections=[
 ["Cadrer l'opération","Ajouter un appareil modifie l'installation [R]. Le BS décrit par l'INRS se limite notamment à la connexion sur un circuit de réserve protégé [S1] : vérifier le titre et le périmètre avant d'agir, la NF C 18-510 n'ayant pas été lue [S1]."],
 ["Vérifier la place et la réserve","Une réserve minimale de 20 % de modules libres est prescrite pour les tableaux de répartition de logement, avec une possibilité de la limiter à six modules par logement en immeuble collectif d'habitation [S14]. Vérifier qu'un emplacement est libre sur la rangée [S9]."],
 ["Choisir l'appareil","Le choix porte sur le calibre, la courbe, le pouvoir de coupure et, pour un différentiel, le type [S9, S7]. Le calibre dépend des conducteurs du circuit à protéger, selon la NF C 15-100 [S8]. Le pouvoir de coupure doit être supérieur au courant de court-circuit présumé [S7]."],
 ["Poser et raccorder","Consigner et vérifier l'absence de tension [S22, S16]. Clipser l'appareil sur le rail, insérer le peigne, serrer la borne amont, raccorder le circuit aval et la terre au bornier [S9]."],
 ["Repérer et essayer","Repérer le circuit et mettre à jour le schéma du tableau [S15]. Remettre en place le plastron, lever la consigne, essayer le circuit [S9, S16]."]],
 decision="Il reste peu d'emplacements libres sur la rangée. Que faites-vous ?",
 answer="On n'improvise pas : on vérifie la réserve préconisée, on alerte le responsable et on décide avec lui d'une extension ou d'un autre tableau [S14, R].",
 check=["Mon titre couvre-t-il cette modification ?","Calibre, courbe, pouvoir de coupure et type vérifiés ?","Consignation et VAT faites, neutre compris ?","Repérage et schéma mis à jour ?"],
 source="Sources S1, S7, S8, S9, S14, S15, S16, S22. Schéma F8 : dessin Consul Team, non à l'échelle.",
 note="Module nouveau, à valider par le formateur. Le périmètre d'habilitation reste à confirmer à la NF C 18-510.",
 questions=[
  Q("T22-01","s","Quelle réserve minimale de modules libres est prescrite pour un tableau de logement ?",["20 %","5 %","50 %"],0,"Réserve minimale de 20 % [S14]."),
  Q("T22-02","s","Sur quoi repose le choix du calibre du disjoncteur d'un circuit ?",["Sur les conducteurs du circuit à protéger","Sur la couleur du boîtier","Sur la taille du tableau seulement"],0,"Le calibre dépend des conducteurs [S8]."),
  Q("T22-03","o","Remettez dans l'ordre les étapes d'installation :",["Cadrer l'opération et vérifier le périmètre","Vérifier la place et la réserve","Choisir l'appareil","Consigner et vérifier l'absence de tension","Clipser et alimenter par le peigne","Raccorder le circuit aval","Repérer et mettre à jour le schéma","Fermer, déconsigner, essayer"],[0,1,2,3,4,5,6,7],"Ordre du schéma F8 : cadrage [S1], place [S14], choix [S7, S9], consignation [S22, S16], pose et raccordement [S9], repérage [S15], essais [S16]."),
  Q("T22-04","s","Après l'ajout, que faut-il mettre à jour ?",["Le repérage du circuit et le schéma du tableau","Seulement le plastron","Rien, l'appareil suffit"],0,"Repérage des circuits [S15]."),
 ])


def X(after,t,q,o,c,why): return dict(after=after,type=t,q=q,options=o,correct=c,why=why)
M19['exercices']=[
 X(0,"s","Dans une rangée, qu'est-ce qui alimente les appareils par le haut ?",["Le peigne d'alimentation","Le bornier de terre","Le rail de fixation seul"],0,"Le peigne alimente les appareils de la rangée [S9]. Le bornier de terre reçoit les conducteurs de terre [S6, R]."),
 X(1,"o","Entre les deux bornes d'un disjoncteur, remettez les éléments dans l'ordre :",["Bilame","Bobine avec noyau","Contact mobile","Chambres de coupure"],[0,1,2,3],"Ordre bilame, bobine avec noyau, contact mobile, chambres de coupure [S10]."),
 X(3,"s","Vous appuyez sur le bouton T d'un différentiel en service. Qu'attendez-vous ?",["Il déclenche","Rien ne se passe","Le disjoncteur divisionnaire en aval déclenche"],0,"Le bouton test dérive un courant en dehors du tore : le différentiel doit déclencher [S3, S4]."),
]
M20['exercices']=[
 X(2,"s","Phases à 24, 26 et 26 A, moyenne 25,33 A. Quel est le déséquilibre ?",["5,3 %","1,3 %","8 %"],0,"Écart maximal : 25,33 − 24 = 1,33 A, soit 5,3 % de la moyenne [S13, C]. 1,3 est l'écart en ampères arrondi, pas un pourcentage [C]."),
 X(4,"o","Remettez dans l'ordre la méthode d'équilibrage :",["Lister les courants d'emploi des circuits","Les classer du plus fort au plus faible","Brancher chacun sur la phase la moins chargée","Contrôler à la pince en charge normale","Repérer la phase de chaque circuit"],[0,1,2,3,4],"Méthode de l'exemple [R], formule de contrôle [S13]."),
]
M21['exercices']=[
 X(2,"s","Quand le VAT se contrôle-t-il ?",["Avant et après la vérification, sur une source connue","Seulement après","Jamais, s'il est neuf"],0,"Contrôle du VAT avant et après usage [S16]."),
 X(3,"m","Pour déposer un disjoncteur à vis, quelles actions sont prévues ?",["Dévisser les quatre vis","Faire levier sur la griffe de fixation","Si un peigne l'alimente, desserrer les vis du haut de tous les disjoncteurs de la rangée","Tirer sur les fils pour l'extraire"],[0,1,2],"Quatre vis, levier sur la griffe, peigne libéré en desserrant le haut de la rangée [S8]. On n'extrait pas l'appareil en tirant sur les fils [R]."),
]
M22['exercices']=[
 X(1,"s","Pourquoi conserver des emplacements libres dans un tableau de logement ?",["Pour les ajouts futurs : une réserve minimale de 20 % est prescrite en logement","Pour ventiler l'appareillage","Parce que le différentiel l'impose"],0,"Réserve minimale de 20 % préconisée [S14] ; l'usage est de prévoir les extensions [R]."),
 X(3,"o","Remettez dans l'ordre la pose d'un appareil :",["Consigner et vérifier l'absence de tension","Clipser l'appareil sur le rail","Insérer le peigne et serrer la borne amont","Raccorder le circuit aval et la terre"],[0,1,2,3],"Consignation [S22, S16], pose sur rail, peigne, raccordement [S9]."),
]
MODULES=[M19,M20,M21,M22]

# ---- déclaration des valeurs chiffrées : jeton -> (niveau, référence) ----
VALEURS={
 '2020':('S','S29 : ED 6127 de décembre 2020'),
 '6127':('S','S29 : numéro de la brochure ED 6127'),'2012':('S','S29 : édition de décembre 2012'),'1':('S','S27 : amendement A1'),'2':('S','S27 : amendement A2 ; S23 : 6 mm²'),
 '1000':('S','S29 : maxi 1000 V du BR, borne du domaine BT'),
 '32':('S','S23 et S24 : protection 32 A du BS'),'63':('S','S23 et S24 : protection amont 63 A du BR'),'500':('S','S23 et S24 : 500 V en connexion sous tension'),
 '0,02':('S','S2 : déclenchement < 0,02 s'),
 '3':('S','S19 : courbe B entre 3 et 5 fois In'),'5':('S','S19 ; C : 5,3 %'),
 '30':('S','S3 : sensibilité 30 mA en logement'),'20':('S','S14 : réserve minimale de 20 %'),
 '230':('S','S21'),'400':('S','S21'),
 '10':('C','calcul-equilibrage : 3 x 10 A = neutre 0 A ; courant d\'un circuit'),'0':('C','calcul-equilibrage : 3 x 10 A = 0 A'),
 '76':('C','calcul-equilibrage : somme 16+16+10+10+8+6+6+4 = 76 A'),
 '16':('C','circuits de l\'exemple'),'8':('C','circuits de l\'exemple'),'6':('C','circuits de l\'exemple'),'4':('C','circuits de l\'exemple'),
 '42':('C','calcul-equilibrage : L1 avant'),'18':('C','L2 avant'),'24':('C','L1 après'),'26':('C','L2 et L3 après'),
 '25,06':('C','neutre avant'),'25,33':('C','moyenne'),'65,8':('C','déséquilibre avant'),'5,3':('C','déséquilibre après'),'2,0':('C','neutre après'),
 '6561':('C','3^8 répartitions énumérées'),'25':('D','distracteur'),'100':('R','formule du pourcentage (× 100) [S13]'),
 '16,7':('D','distracteur : écart en A'),'60,3':('D','distracteur : moyenne ÷ maximum'),'5':('S','S19 ; C : 5,3 %'),'50':('D','distracteur'),
}

VALEURS['1,3']=('D','distracteur : écart arrondi'); VALEURS['1,33']=('C','25,33 − 24')
