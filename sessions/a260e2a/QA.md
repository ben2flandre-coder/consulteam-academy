# Contrôles A260E2A — 14/11/2026 (version avec modules 19 à 22)
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

## Mise à jour du 14/11/2026 — images IA et NF C 18-510
- Images : 55/55 SHA-256 conformes au suivi (preuves/controle-images.json) ; versions légères dans images/ia (précachées hors ligne), originaux dans sources-images (non précachés). Statuts repris du suivi : examen visuel préliminaire de Codex, relecture technique ou renforcée à faire ; ce n'est pas une relecture de formateur habilité. TB01–TB09 sans image.
- À signaler : visages visibles (PR01, BT02, SI03, BT01, NE02, TC09, EX03), gants de TC03 d'aspect non isolant, instrument d'EX01 d'aspect multimètre, texte et logos à revérifier en pleine taille.
- NF C 18-510 : sources S23 à S29 ajoutées. Limites lues dans l'INRS ED 6127 (édition de décembre 2012, p. 11) : BS 400 V et 32 A ; BR 1000 V et 63 A, connexion sous tension jusqu'à 500 V. Écart levé : le 1000 V est la borne du domaine BT (lecture [R]). Section 6 mm² : sources secondaires seulement. L'édition lue date de 2012, avant A1 et A2 ; texte de la norme (payant) non lu ; la page INRS opérations ne mentionne aucun effet des amendements sur le BS et le BR.
- Contrôles rejoués : 115 affirmations sourcées, 0 sans référence ; responsive, QCM (97 questions), hors ligne, exercices : sans erreur JS.
