# Recette de clôture 2.1 - session 260053A

Reprise du 28 novembre 2026 depuis `7197b3b374e0c658b5ccafe1bcd889b4bb93acf4`. Le travail des versions 1.8 à 2.1 est conservé. Les autres sessions ne sont pas modifiées. Le commit contenant ce fichier constitue la référence de cette clôture.

## Résultat numérique

- 67 vues parcourues sur le site publié, à 1280 × 720 : 57 vues statiques et 10 questions. Aucune image cassée ni aucun débordement horizontal observé. Cinq planches présentaient un dépassement vertical d'arrondi d'un pixel ; leur hauteur maximale a été réduite de trois pixels.
- Livret PDF A4 portrait de 32 pages : toutes les pages rendues et examinées ; couverture, intérieur, tableaux, médias, pagination et quatrième de couverture contrôlés. Deux anciennes mentions 2.0 (couverture HTML et colophon commun) remplacées par 2.1. PDF régénéré aux deux destinations depuis la même source éditoriale.
- Livret HTML : 32 feuilles, sans dépassement de hauteur à la largeur A4 ; à 390 px, aucun débordement horizontal ni image cassée. Accueil participant et six cas vérifiés à 390 px.
- Six cas : blocage sans choix ou justification, puis correction des six réponses attendues. Les données de recette, initialement absentes, ont été effacées après le contrôle. La justification libre n'est pas notée automatiquement.
- Grille individuelle : suppression de la mémorisation des résultats entre visites. Une nouvelle ouverture commence à NO ; les saisies restent dans l'onglet ouvert. Observations complètes et sélections préparées à l'impression, puis DOM de lecture restauré.
- Aperçu d'impression : ouverture confirmée par Benoît le 28/11/2026, puis fermeture par lui. Cela ne vaut pas validation visuelle de chaque feuille. Le cycle avant/après impression et la conservation d'une note longue sont contrôlés par un test dédié. Aucune impression physique effectuée par l'agent.

## Vérifications reproductibles

Depuis le dossier de session :

```text
python qa/check_static.py
python qa/check_coherence.py
node qa/safety-tools.test.cjs
node qa/roles.test.cjs
node qa/knots.test.cjs
node qa/print-fields.test.cjs
```

Résultats : 35 contrôles de cohérence, 24 cas de saisie et de limites, 19 cas de parcours/stockage, quatre tracés géométriques et cycle d'impression réussis. Contrôle statique : 21 pages ; références et résultat exact dans `static-report.json`. Pour cette reprise, l'existence des médias non téléchargés a été vérifiée dans l'arbre Git du commit de base ; pages, scripts et SVG examinés localement. Tous les services externes ne sont pas testés.

PDF examiné à nouveau après régénération. Contenu des aperçus des pages 8 et 13 inchangé. Les PDF Academy et Supports ont la même empreinte ; registre Supports actualisé avec les 32 pages, la date et le SHA-256 courant.

## Matrice du benchmark

Le traitement documentaire et l'exécution réelle restent distincts. Aucun statut ci-dessous ne constitue une attestation de conformité globale des équipements ou de la prestation.

| Point | Traitement vérifié | Limite pour la session |
| --- | --- | --- |
| B01 | Exceptions des échelles complètes ; cas répété vingt fois ; QCM aligné | Décision sur le poste réel |
| B02 | Accès distinct de la protection collective | Accès réellement installé à vérifier |
| B03 | Signalisation, exclusion et protection distinguées ; cas toiture | Réception de la zone réelle |
| B04 | Construction du cordage distincte de sa fonction ; contre-exemple HOPE | Identifier le produit utilisé |
| B05 | Brin libre, génération et notice ; critère observable | Démonstration sur le modèle exact |
| B06 | Aucune longueur de bout libre universelle | Notice, matériau, montage et réalisation réels |
| B07 | Périmètre, prérequis et restriction mineurs du programme conservés ; limites d'attestation et adaptations tracées | Admission, encadrement et objectifs réellement atteints ; signaler à Consulteam tout objectif pratique manquant |
| B08 | Six cas numériques avec justification ; quatre repris pages 23-24, autres situations dans le livret | Raisonnement à apprécier par le formateur |
| B09 | Repère commun, inconnues, fiche de lecture de notice et variantes ; aucune autorisation automatique | Renseigner notice, référence et plan du matériel de la salle |
| B10 | Hauteur et déport dissociés ; plan et coupe | Trajectoire et limites du dispositif réel |
| B11 | Dossiers d'observation, défaut sans diagnostic inventé, usage distinct du périodique ; procédure fabricante illustrée liée | Examen tactile, historique et décision compétente ; aucune nouvelle galerie prétendument validée |
| B12 | Tracés, photos de référence et contrôle final ; limites des animations conservées | Geste, habillage et serrage à montrer/contrôler réellement ; aucune qualification de cordiste ou de sauveteur déduite |
| B13 | Statut de revue et journal de visionnage visibles | Visionnage humain avant projection ; aucune validation globale des 27 ressources |
| B14 | Faits, arrêt, correction, nouvelle tentative, NO ; saisie éphémère, impression des valeurs | Plan d'observation et résultats individuels à renseigner |
| B15 | Édition, sources, HTML/PDF, registre Supports et liens rapprochés | Visas Consulteam et terrain à leur état réel |

## Programme et références

Comparaison au PDF source SECU37 : six objectifs, cinq parties, prérequis, restriction des exercices pour les mineurs, effectif de 4 à 10 et évaluation. Une adaptation de sécurité ne prouve pas la réalisation d'un objectif pratique non observé.

Sources sensibles dans `sources/registre-2.0.json` et `tracabilite.html#registre`. Revérification le 28/11/2026 : R.4323-61, R.4323-63, R.4323-106, arrêté du 19 mars 1993 et repères INRS. Prérequis médicaux et restriction mineurs attribués au programme Consulteam, sans règle générale nouvelle déduite.

## Diffusion et clôture humaine

Participant : `apprenants.html?e=p`. Entrée de Benoît pour tous les espaces : `index.html?e=f`, puis **Pilotage**. Un parcours participant ouvert seul ne montre pas automatiquement ce menu. L'hébergement est public : le masquage ne constitue pas une authentification.

Contrôle numérique clos dans ce périmètre. Restent sur site : visas de l'organisme, équipements et ancrages, secours, admissibilité aux exercices, validation des gestes et observation des participants. La projection des vidéos reste conditionnée à leur revue humaine.
