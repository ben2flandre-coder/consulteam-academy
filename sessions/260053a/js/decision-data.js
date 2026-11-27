/* Situations fictives ; données fabricant non inventées. */
window.DecisionCases=[
  {
    "id": "reperes",
    "tag": "Mesurer",
    "title": "La marge apparente suffit-elle ?",
    "scene": "Dans cet énoncé fictif, la notice demande 4,20 m depuis les pieds. Une mesure sur site annonce 4,60 m depuis l’ancrage. Aucun relevé depuis les pieds ni plan de conversion n’est disponible.",
    "image": "mesure-reperes",
    "options": [
      "Accepter : 4,60 m est supérieur à 4,20 m.",
      "Différer : les origines de mesure sont différentes ; refaire la mesure dans le repère de la notice.",
      "Ajouter systématiquement la taille de la personne, puis accepter."
    ],
    "answer": 1,
    "reason": "Les deux distances ne se comparent pas directement. Relever la distance disponible depuis le repère prévu, jusqu’au premier obstacle pertinent. Une formule universelle ne répare pas une donnée manquante.",
    "checks": [
      "Nommer les deux origines de mesure.",
      "Demander un relevé exploitable.",
      "Vérifier ensuite configuration, obstacles et secours."
    ],
    "source": "tirant",
    "variant": "La mesure est refaite : 3,90 m depuis les pieds. Il manque 0,30 m dans l’énoncé ; la configuration est écartée. Ces valeurs d’exercice ne décrivent aucun matériel du site.",
    "source_url": "https://www.petzl.com/fr/fr/calculateur-de-degagement/clearancecalculator.html",
    "source_label": "Petzl · Calculateur de dégagement et limites"
  },
  {
    "id": "compatibilite",
    "tag": "Composer",
    "title": "Deux marquages CE prouvent-ils la compatibilité ?",
    "scene": "Un harnais et un antichute mobile sont identifiés. La corde fournie est du bon diamètre apparent, mais sa référence et la liste des combinaisons autorisées ne sont pas disponibles.",
    "image": "notice-identification",
    "options": [
      "Accepter : le diamètre et le marquage suffisent.",
      "Essayer le blocage à la main ; si cela fonctionne, accepter.",
      "Suspendre le choix jusqu’à l’identification de la corde et de la combinaison prescrite."
    ],
    "answer": 2,
    "reason": "Un diamètre compatible ne suffit pas à identifier la corde prescrite. Retrouver la référence du dispositif, sa notice et le support d’assurage autorisé. Un essai improvisé ne remplace pas cette vérification.",
    "checks": [
      "Nommer l’information absente.",
      "Distinguer conformité d’un composant et compatibilité d’un système.",
      "Écarter l’essai manuel comme preuve suffisante."
    ],
    "source": "epi",
    "variant": "Même avec la bonne corde, vérifier le sens de montage, les connexions prévues, les limites d’emploi et le contrôle fonctionnel prescrit.",
    "source_url": "https://www.inrs.fr/risques/chutes-hauteur/equipements-protection-individuelle-chutes-hauteur.html",
    "source_label": "INRS · Systèmes individuels contre les chutes"
  },
  {
    "id": "secours",
    "tag": "Anticiper",
    "title": "Un téléphone et le 112 : préparation suffisante ?",
    "scene": "La zone ne dispose d’aucune procédure de récupération renseignée. L’équipe sait téléphoner aux secours. Le travail prévu nécessite un système d’arrêt de chute.",
    "image": "secours-organisation",
    "options": [
      "Commencer si le réseau téléphonique fonctionne.",
      "Reporter l’exposition jusqu’à la définition et la disponibilité des moyens, accès, rôles et compétences nécessaires au secours.",
      "Commencer à condition qu’un collègue soit présent au sol."
    ],
    "answer": 1,
    "reason": "La présence d’un collègue et l’alerte sont nécessaires dans l’organisation retenue, mais ne démontrent pas la capacité à récupérer la personne à temps. Prévoir et vérifier l’ensemble avant l’intervention.",
    "checks": [
      "Distinguer alerte et récupération technique.",
      "Décrire les rôles, accès et moyens à préparer.",
      "Refuser une improvisation de sauvetage."
    ],
    "source": "secours",
    "variant": "L’équipe possède un kit mais n’est pas formée à son utilisation. La disponibilité du kit ne suffit pas : la préparation reste incomplète.",
    "source_url": "https://ssa.msa.fr/wp-content/uploads/2025/04/SyndromeDuHarnais_avril2025-1.pdf",
    "source_label": "Carsat / DREETS / MSA / OPPBTP · Syndrome du harnais, avril 2025"
  },
  {
    "id": "echelle",
    "tag": "Arbitrer",
    "title": "Deux minutes, vingt fois dans la journée",
    "scene": "Une tâche est proposée depuis une échelle : deux minutes par intervention, vingt interventions similaires dans la journée. L’évaluation annonce un risque faible ; aucune impossibilité technique de protection collective n’est établie.",
    "image": "echelle-exception",
    "options": [
      "L’exception de courte durée suffit.",
      "La faible hauteur suffit, quelle que soit la répétition.",
      "L’exception « faible risque et courte durée sans répétition » ne peut pas justifier ce poste tel qu’il est décrit. Rechercher une solution de travail adaptée."
    ],
    "answer": 2,
    "reason": "Le caractère non répétitif manque. Les conditions de cette branche de R.4323-63 sont cumulatives. L’autre branche est l’impossibilité technique de recourir à un équipement assurant la protection collective, qui doit être établie.",
    "checks": [
      "Repérer la répétition.",
      "Restituer les deux branches distinctes de l’exception.",
      "Proposer de réexaminer le poste et l’accès."
    ],
    "source": "echelles",
    "variant": "Changer le nombre de répétitions ne dispense pas de l’évaluation du risque ; une seule intervention n’est pas automatiquement autorisée.",
    "source_url": "https://code.travail.gouv.fr/code-du-travail/r4323-63",
    "source_label": "Code du travail · R.4323-63"
  },
  {
    "id": "toiture",
    "tag": "Protéger",
    "title": "Une rubalise autour d’un lanterneau",
    "scene": "Le cheminement prévu passe à proximité d’une surface fragile. Une rubalise la signale, mais aucune mesure n’empêche de la franchir et aucune protection contre la traversée n’est établie.",
    "image": "toiture-enquete",
    "options": [
      "La signalisation suffit à protéger contre la traversée.",
      "La signalisation aide au repérage, mais il faut définir une protection adaptée ou une exclusion effective et un cheminement sûr.",
      "Le harnais disponible suffit à autoriser l’accès."
    ],
    "answer": 1,
    "reason": "La rubalise signale sans arrêter une chute ni démontrer une exclusion effective. Le choix doit traiter l’accès, la circulation, les surfaces fragiles, la périphérie et la pose des protections.",
    "checks": [
      "Identifier ce que la rubalise fait et ne fait pas.",
      "Traiter l’accès et le cheminement.",
      "Prévoir la phase d’installation des protections."
    ],
    "source": "toiture",
    "variant": "Une grille est annoncée sous un lanterneau. Vérifier son identification, son installation et son état ; ne pas déduire sa résistance d’une photographie.",
    "source_url": "https://www.preventionbtp.fr/ressources/solutions/travaux-de-couverture-en-materiaux-fragiles-securiser-le-travail-en-hauteur_HNsxXVCnonwUrUx22JnFan",
    "source_label": "OPPBTP · Couvertures en matériaux fragiles"
  },
  {
    "id": "cordage",
    "tag": "Identifier",
    "title": "La corde ressemble à celle d’hier",
    "scene": "Un cordage est présenté sans identification ni notice. Son diamètre, sa couleur et sa construction ressemblent à ceux d’un cordage déjà utilisé.",
    "image": "observer-defauts",
    "options": [
      "L’utiliser si l’examen visuel ne révèle rien.",
      "Déduire sa fonction de sa construction : toronnée ou âme-gaine.",
      "L’écarter de l’usage envisagé pour les personnes jusqu’à l’identification et la vérification de sa fonction et de ses compatibilités."
    ],
    "answer": 2,
    "reason": "L’apparence ne permet pas de qualifier le produit. Une construction toronnée peut exister dans un EPI identifié, sans rendre utilisable un cordage inconnu ou de manutention.",
    "checks": [
      "Refuser la déduction par couleur ou construction.",
      "Rechercher référence, fonction et notice.",
      "Distinguer état visible et aptitude à l’usage."
    ],
    "source": "toron",
    "variant": "Une identification est retrouvée : elle autorise la manutention de charges uniquement. Ce produit ne devient pas un EPI pour les personnes.",
    "source_url": "https://kratossafety.com/products/hope-longe-toronnee-1-50-m-en-fourche-avec-absorbeur-d-energie-et-mousquetons-fa5010117-et-fa5020755",
    "source_label": "Kratos · HOPE FA3020015, longe en corde toronnée avec absorbeur"
  }
];
