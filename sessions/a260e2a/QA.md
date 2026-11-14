# Contrôles A260E2A — 14/11/2026 (refonte charte Panzani, 22 modules rédigés)
Chaque ligne renvoie à une pièce du dossier `preuves/`.
| Contrôle | Résultat | Pièce |
|---|---|---|
| 7 pages × 4 largeurs (390, 768, 1024, 1280 px), Chromium | 28 combinaisons : 0 débordement horizontal, 0 erreur JavaScript, `lang="fr"`, viewport présent | qa-responsive.json |
| Pages des modules 19 à 22 à 390 et 1280 px | Pas de débordement, toutes les images chargées, captures complètes | qa-modules-nouveaux.json, captures/ |
| Exercices intermédiaires (9, dans les modules 19 à 22) | Bonne réponse jugée « Juste » et mauvaise réponse « À revoir » pour les 9 ; un défaut sur la mise en ordre, trouvé par ce test, est corrigé | test-exercices.json |
| QCM : 97 questions, réponses justes cochées | 97/97 ; toutes fausses : 0/97 ; types simple, multiple et ordre ; 0 erreur JS | test-qcm.json |
| Hors connexion (service worker, Chromium) | Page du module 20 et son schéma s'affichent hors ligne après un premier chargement | test-hors-ligne.json |
| Schémas F1 à F8 | XML valide (xmllint), aucun texte hors cadre, aucun chevauchement de textes (mesure sur rendu) ; contrôle visuel des 8 rendus | validation-svg.json |
| Équilibrage : valeurs de l'exemple | Calcul par phaseurs, 6561 répartitions énumérées, la méthode atteint l'optimum | calcul-equilibrage.json |
| Valeurs chiffrées des modules 19 à 22 | Chaque nombre du texte est déclaré avec sa source ou son calcul : 0 nombre non déclaré | controle-valeurs-chiffrees.json |
| Affirmations des modules 19 à 22 | 100 affirmations, chacune avec une référence [S#], [C] ou [R] : 0 sans référence | matrice-affirmations-sources.csv |
| Sources S1 à S22 | Accès (lu ou extrait), fiabilité, usage et limites de chaque source | sources-lues.json |
| Images reprises de Panzani | 5 fichiers, empreintes sha256 identiques à celles du dépôt d'origine | verification-reprises.json |
| Questions reprises : indices de réponse | 45 questions Panzani et 32 questions A2604MA comparées tuple à tuple (type, énoncé, options, indice, explication) : 77 identiques, 0 écart | verification-reprises.json |
| Textes repris de Panzani et A2604MA | 289 et 276 éléments retrouvés dans les dépôts d'origine : 0 introuvable | verification-reprises.json |
| Pack de prompts | 64 prompts, identifiants uniques, aucun chiffre accolé à une unité, aucune mention « INRS » | verification-prompts.json |
Limites, à lire :
- La NF C 18-510 n'a pas été lue : le périmètre d'habilitation pour remplacer ou installer un appareil reste à confirmer.
- Les niveaux de preuve : [S] source lue ou extrait, [C] calcul prouvé, [R] principe de raisonnement à valider par le formateur. Une partie des sources n'a été lue qu'en extrait (voir sources-lues.json). Aucune copie des pages web n'est conservée.
- La comparaison des sections reprises prouve la présence du texte d'origine, pas l'ordre des phrases. Les questions, elles, sont comparées une à une, indice de réponse compris.
- S13 (Fluke) et S14 (Éduscol) ont été relues le 14/11/2026 par l'outil de lecture web avec une question ciblée : formule du déséquilibre et réserve minimale de 20 % confirmées. Cette relecture a conduit à corriger une formulation (connexions desserrées, et non échauffement).
- Les schémas sont des schémas de principe non à l'échelle ; leur justesse technique est à valider par le formateur.
- Contraste, lecteur d'écran et mode nuit : non vérifiés. Espace formateur non chiffré. Visuels IA : aucun intégré.

## Mise à jour du 14/11/2026 — images IA, NF C 18-510 (état de 11 h 45)
- Images : lot de 64 (11 h 42) intégré, 64/64 SHA-256 conformes au suivi (preuves/controle-images.json) ; les 55 premières sont inchangées. Versions légères dans images/ia (précachées), originaux dans sources-images. TB01 à TB09 vues une par une en pleine taille : réserves dans preuves/controle-images-TB.md. Défaut corrigé : les images n'apparaissaient pas dans la médiathèque (chargement paresseux d'une image hors DOM) ; 64/64 affichées après correction (preuves/test-mediatheque-images.json).
- Statuts du suivi : examen préliminaire de Codex (43 relectures techniques, 20 renforcées, 1 examen standard) ; ce n'est pas une relecture de formateur habilité. Lot de 55 : visages visibles (PR01, BT02, SI03, BT01, NE02, TC09, EX03), gants de TC03 non isolants, instrument d'EX01 d'aspect multimètre ; lot TB : conducteurs bleus sur bornes de phase (TB03, TB09), sectionneur jaune et rouge (TB06), main nue (TB09), pince d'aspect de marque connue (TB08).
- NF C 18-510 : sources S23 à S30. Limites lues dans l'INRS ED 6127, 3e édition de décembre 2020 (fichier fourni par Benoît, p. 11-12) : BS circuits terminaux, 400 V et 32 A, hors tension et sans voisinage renforcé ; BR connexion sous tension jusqu'à 500 V et 63 A en courant alternatif, hors charge. L'édition de 2012 (S30) disait « BR maxi 1000 V et 63 A » : mention absente en 2020. Section de 6 mm² : sources secondaires seulement. L'édition lue date de décembre 2020, avant A2 (juin 2023) ; texte de la norme (payant) non lu.
- Contrôles rejoués : 117 affirmations sourcées, 0 sans référence ; responsive, QCM (97 questions), hors ligne, exercices : sans erreur JS.

## Refonte du 14/11/2026 (après-midi)
| Contrôle | Résultat | Pièce |
|---|---|---|
| 13 pages × 4 largeurs (390 à 1280 px) | 52 combinaisons : 0 débordement, 0 erreur JS, 0 image sans alt, lang fr | qa-responsive.json |
| QCM global (75 questions tirées de 118) | tout juste = 75/75, tout faux = 0/75 ; deux tirages partagent environ 46 questions sur 75 | test-qcm.json |
| Traçabilité des modules 9, 12 à 17, 19 à 22 | 239 affirmations, 0 sans référence, 0 nombre non déclaré | matrice-affirmations-sources.csv |
| Cours de base (12 routes) | toutes affichent leur contenu, 0 erreur JS | non archivé |
| Lot GPT du 14/11/2026 (12 h) | 64 SHA-256 conformes au suivi ; 4 images modifiées (TB01, TB03, TB06, TB07, vues et intégrées) ; 5 coupes ajoutées (A à E, vues) ; galerie : 69 images affichées | controle-images.json, test-mediatheque-images.json |
