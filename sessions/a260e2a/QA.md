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

## Espace formateur chiffré (14/11/2026)
Contenu de formateur.html chiffré dans le navigateur (AES-GCM 256, PBKDF2 600 000 itérations). Déverrouillage : code + une adresse e-mail autorisée. Ni le code ni les adresses ne sont dans le site ; le texte en clair est absent. Test : preuves/test-formateur-verrou.json. Limite : un code court se devine par essais hors ligne ; le corrigé du QCM reste lisible dans data/content.js.

## Refonte pédagogique (14/11/2026, après benchmark)
Écran de module en 5 phases (voir, comprendre, faire, vérifier, retenir), procédures pas à pas, coups de pouce gradués, entrée par symbole, avancement local. Benchmark : BENCHMARK.md. Tests : preuves/test-studio.json (22 modules ouverts sans erreur, 5 phases, pas-à-pas, aides, score), preuves/qa-responsive.json (68 combinaisons dont cours/ à 390 px, corrigé). Limite : les questions de « Faire » et « Vérifier » sont celles de la banque de l’évaluation (une moitié chacune) ; un stagiaire peut les avoir vues avant l’évaluation finale.

## Évaluations, documents de session, modules HT (14/11/2026, 13 h)
- Vue « Tout lire » ajoutée en tête de chaque module (lecture continue de tout le contenu) et ouverte par défaut ; les 5 phases guidées restent disponibles.
- Modules 12, 13, 14 et 15 étoffés à partir de l'ED 6127 : 7 à 8 sections chacun, un pas-à-pas par module, 8 à 10 questions chacun. Banque : 144 questions (118 avant). check_modules : 326 affirmations, 0 sans référence.
- Évaluations : générale complète (144 questions), tirage général de 75, et 12 évaluations par niveau de 20 questions (30 % zones et distances, 40 % limites du niveau, 30 % socle ; répartition inspirée de l'ED 6127). Seuil de référence 70 %, résultat par module. Preuves : preuves/test-evaluations.json (scripts/eval_test.py).
- Page « Documents de session » : émargement par demi-journée, satisfaction à chaud, compte rendu jour par jour, 10 grilles d'évaluation pratique par symbole (ED 6127 §5.4.2, tableau relu sur la page), avis après formation (contenu de l'ED 6127 §7.2), attestation de fin de formation. Modèles de travail, à valider par le formateur et le commanditaire.
- Tests : 60 combinaisons d'affichage sans débordement (preuves/qa-responsive.json), studio, hors ligne en local.
- Limites : la banque de 144 questions ne respecte pas « cinq fois plus de questions que posées » par thème pour chaque niveau (ED 6127) ; les grilles pratiques et la liste des savoir-faire sont à valider ; durée 21 h (programme) ou 19,5 h (horaires du CPS) non levée ; textes de la NF C 18-510 non lus.

## Études de cas, arbre de décision, compléments (14/11/2026, 14 h)
- Module 23 « Études de cas d'accidents » : 8 cas réels résumés d'après l'INRS ED 325 (source S32, lue par synthèse de page, édition de 1993 réimprimée en 2012), méthode d'analyse en quatre temps, 10 questions. À comparer à la brochure avant publication.
- Page « Quel symbole ? » : arbre de décision fondé sur le tableau de choix de l'ED 6127 (§2.3 et §2.4) ; testé sur les chemins BS, H2V, B0 et HE Manœuvre, retour arrière et mobile sans débordement. Les limites détaillées relèvent de la NF C 18-510, non lue.
- Questions ajoutées aux modules 9, 16 et 17. Banque : 165 questions (module 23 inclus) ; check_modules : 391 affirmations, 0 sans référence.
- Tests : 64 combinaisons d'affichage sans débordement, évaluations (complète 165, tirage 75, 12 niveaux de 20), studio et 23 modules ouverts sans erreur.

## Durée : 21 h
- La formation est présentée sur 21 h (dont 7 h de pratique) dans tous les documents de session ; plus aucune mention d'écart de durée. Tests studio et évaluations relancés : 0 erreur.
- Non fait : ressources INRS SST (cloud.inrs.fr) non récupérées, aucun accès accordé à l'ordinateur ni au site ; module 8 reste fondé sur S31.

## Ressources INRS SST (zip fourni le 14/11/2026)
- Zip « 2-Ressources technico-pédagogiques » reçu et ouvert : 81 fichiers. Module 8 complété avec le guide des données techniques SST V5.01/2024, TS876 et ED 4085 (sources S33 à S35, preuves/module8-inrs-controle.md). Studio et évaluations retestés : 0 erreur.
- Reste : ED 7000 non lu ; le contrôle automatique des affirmations ne couvre pas les sections ajoutées dans build_site.py, relues à la main (chaque phrase référencée).

## Audit complet du 14/11/2026
Voir preuves/RAPPORT-AUDIT.md : programme 30/31, réglementaire 7 vérifiés / 6 réserves / 1 non vérifiable, 405 affirmations sans écart, accessibilité axe 0 violation (13 pages), 60 combinaisons d'affichage sans défaut, hors ligne OK, 211 questions. Fiche de parcours et mention handicap ajoutées.

## Recherches élargies (14/11/2026)
Sources S37 à S40 ajoutées ; audit réglementaire : 13 vérifiés sur 14 ; ED 325 récupérée (édition 1993, réimpression 2012, 24 cas).
