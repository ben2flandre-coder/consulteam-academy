# A260BNA — registre de production, 19 octobre 2026

## Mission
Habilitation électrique H0V B2V BR BC, recyclage, intra, vendredi 30 octobre 2026, Marseille, 1 participant. Source : CPS signé des deux parties. Horaires du CPS : 09:00–12:00 / 13:30–17:00. Aucune donnée nominative, coordonnée ou condition financière n'est publiée dans le dépôt.

## Origine
Cours de base : copie byte à byte du cours Consulteam Academy `sessions/a2604ma/cours/index.html` (socle, B0/H0/H0V, BS, BE Manœuvre), conservée dans `cours/base.html` et adaptée à la session par `cours/index.html` et `cours/panzani.js` (dates, lieu, cas métiers, déroulé, médiathèque, ordre des réponses mélangé, espace formateur verrouillé). Compléments propres à la session : `parcours.html` (H0V B2V BR BC), `evaluation.html`, `galerie.html`, `formateur.html`. Aucun autre dossier de `sessions/` n'est modifié.

## Sources externes effectivement consultées
- [INRS — FAQ habilitation électrique](https://www.inrs.fr/risques/electriques/habilitation-electrique-foire-aux-questions) (consultée le 19/10/2026) : la page publiée donne la structure des symboles (tension, type d'opération, attribut V) ; les réponses sur les limites BR, le symbole de consignation et les périodicités n'y sont pas affichées.
- [INRS — habilitation électrique](https://www.inrs.fr/risques/electriques/habilitation-electrique.html) et [arrêté du 9 juillet 2013](https://www.legifrance.gouv.fr/loda/id/JORFTEXT000027736209/) : consultés le 10/10/2026 lors d'une production précédente (voisinage, rôle de l'employeur) ; non reconsultés intégralement le 19/10.

## Limites déclarées
- Le texte consolidé de la NF C 18-510 et ses amendements n'a pas été fourni à cette production. Le contenu repose sur les connaissances générales de la norme et les pages INRS ci-dessus ; il n'atteste aucune conformité complète.
- À confirmer avec la norme ou le titre du participant : (1) [levé le 19/10, voir ci-dessous] ; (2) la périodicité de recyclage retenue par l'employeur (« trois ans » présenté comme valeur usuelle recommandée) ; (3) distances de voisinage HT ; (4) vocabulaire exact des documents de consignation du site (attestation, avis de fin de travail).
- Les scénarios sont génériques ; les prescriptions et installations du site client ne sont pas connues.
- Le seuil de 70 % est un repère pédagogique interne, pas un avis favorable.

## Écart d'horaires signalé
Les créneaux du CPS totalisent 6 h 30 pour 7 h annoncées (voir espace formateur).

## Galerie
Aucune image à ce jour. Les visuels seront produits par le formateur (outil d'images) ; chaque image sera consignée ici avec son prompt avant publication.

## Médiathèque (19/10/2026)
Lot fourni par le formateur (produit par GPT) : `mediatheque/` = 24 schémas SVG, 2 illustrations de contexte, 26 fiches de traçabilité (HTML/JSON), 12 scénarios avec corrigés, cahier apprenant, projection, guide d'animation, sources, rapport. Empreintes SHA-256 dans `manifest_sha256.json`.
Réserves du lot lui-même : conformité NF C 18-510 non établie, relecteur indépendant non réalisé, symboles simplifiés non IEC, aucun schéma d'exécution, images non Panzani.
Retiré de la galerie le même jour : les premières maquettes (15 extraits, 8 PNG « HD », 3 planches d'ensemble). Motifs, repris de l'audit GPT et de ma relecture : zones de voisinage fausses (0,10 m ; « simple jusqu'à 0,30 m »), consignation en 6 étapes différente du parcours, rôles BR/BC présentés comme des autorisations générales, VAT confondue avec le mesurage, textes générés dans l'image. Les trois affiches originales sont exclues du dépôt (conservées par le formateur).
Lecture du lot par Claude : fiches et scénarios compatibles avec le parcours (pas de cotes de zones, VAT distincte du mesurage, voyant éteint ≠ absence de tension). Non relu intégralement : chaque SVG et chaque corrigé. À faire relire par un relecteur qualifié avant usage opérationnel.

## Vérification BR / BC du 19/10/2026 (OPPBTP, INRS ED 6127)
Sources lues :
- [INRS ED 6127 — L'habilitation électrique, démarche de prévention (déc. 2020)](https://www.inrs.fr/dam/inrs/CataloguePapier/ED/TI-ED-6127.pdf) : BR = interventions générales d'entretien et de dépannage (recherche de panne, remplacement, mise en service partielle et temporaire, connexion/déconnexion) ; connexion/déconnexion en présence de tension : maxi 500 V, 63 A alternatif, hors charge ; formation BR incluant la consignation pour son propre compte ; BC = consignation ; habilitation + désignation par l'employeur ; attestation de consignation (une ou deux étapes), avis de fin de travail, autorisation de travail, instructions de sécurité ; recyclage recommandé 3 ans (§ 6.2.1), réduit si pratique occasionnelle.
- [OPPBTP — Doit-on être formé pour faire une consignation sur une armoire électrique ?](https://www.preventionbtp.fr/ressources/questions/doit-on-etre-forme-pour-faire-une-consignation-sur-une-armoire-electrique_yDpmVLoTfTemKCej8uvWk7) : dans le cadre d'un travail, consignation par un chargé de consignation BC ou HC ; dans le cadre d'une intervention, par un chargé d'intervention générale BR.
Corrections apportées : mon premier jet laissait entendre que le BR ne consigne pas seul ; c'est inexact pour son propre ouvrage. Parcours, évaluation (+3 questions) et recyclage (3 ans) corrigés.
Non résolu : la page OPPBTP « Qui doit faire la consignation » est bloquée à la lecture automatique (robots) ; le site UTE et le texte de la NF C 18-510 sont payants/non lus ; les distances de voisinage BT (0,30 m / 3 m) n'figurent pas dans l'ED 6127 (renvoi au § 8.1 de la norme) ; la liste détaillée des étapes (pré-identification, séparation, condamnation, identification, VAT, mise à la terre et en court-circuit) n'est pas détaillée dans l'ED 6127 et reste fondée sur la pratique de la norme. À confirmer sur l'exemplaire de la norme de Benoît.

## Élargissement des sources (19/10/2026)
- [INRS ED 6109 — Consignations et déconsignations](https://www.inrs.fr/dam/inrs/CataloguePapier/ED/TI-ED-6109.pdf) : consignation électrique en 5 opérations dans l'ordre (séparation, condamnation, identification, VAT, mise à la terre et en court-circuit, p. 14-16) ; chargé de consignation désigné par l'employeur, peut faire exécuter par son personnel (p. 8) ; déconsignation électrique généralement en sens inverse, ordre confirmé par analyse des risques (p. 16). Identification préalable : définie p. 9. Les termes « attestation de consignation » et « avis de fin de travail » n'y figurent pas (ils figurent dans l'ED 6127).
- [Arrêté du 9 juillet 2013, annexe (relais INERIS-SSTIE)](https://sstie.ineris.fr/reglementation/arrete-090713-relatif-dimensions-zone-voisinage-autour-dune-piece-nue-sous-tension) : ligne 1 kV, distance de garde 0,30 m, DMA 0,30 m. Confirme 0,30 m en BT. La limite de 3 m (hors voisinage) et la distinction DLVS/DLVR relèvent de la NF C 18-510, non lue : source secondaire seulement.
- [INRS ED 6187](https://www.inrs.fr/dam/inrs/CataloguePapier/ED/TI-ED-6187.pdf) : renvoie aux § 3.3.2 (p. 40) et 4.15 (p. 106) pour les zones ; texte non extrait.
- Légifrance (arrêté 2013) : lecture automatique refusée lors de cette production.

## Corrections de la médiathèque par Claude (19/10/2026)
Après relecture des 24 schémas et des 12 scénarios :
- V21 : texte qui chevauchait le tracé, déplacé.
- V03 : mention « absence de MALT/CC en BT non systématique » remplacée par « cinquième opération, selon l'analyse des risques (INRS ED 6109) ».
- V13 : « aidé d'au plus un exécutant B1 » retiré (effectif et titre de l'assistant non confirmés par les sources lues) ; à vérifier sur la NF C 18-510. Le scénario C04 a été reformulé le 19/10 (étendue, ED 6127 p. 13) et V13 (assistance) sont à relire sur la norme.
- Scénario C12 et V13 : le lot cite « la FAQ INRS » pour la distinction hors tension / connexion sous tension ; la page FAQ lue le 19/10 ne publie que les intitulés des questions. Le seuil de 500 V / 63 A figure dans l'ED 6127 (p. 13), source retenue dans le parcours.
- Les fichiers `svg/*.svg` modifiés ne correspondent plus aux empreintes de `manifest_sha256.json` pour V03, V13 et V21 (empreintes d'origine du lot GPT).

## Panneaux et images (lot V2 du 19/10/2026) et sélection
Reçu : 8 panneaux pédagogiques (3200 × 1800, textes composés séparément des images) et 8 images synthétiques (1672 × 941 ; la pompe 1536 × 1024), avec fiches et prompts. Les textes des 8 panneaux ont été relus : rôles, consignation (séparation, condamnation, identification, VAT, mise à la terre et en court-circuit selon le contexte), VAT distincte du mesurage, EPI choisis à partir de l'analyse des risques, énergies multiples, coordination, reprise. Cohérents avec l'ED 6127, l'ED 6109 et l'OPPBTP lus par Claude ; aucune cote ni distance.
Retenus : les 8 panneaux et les images I03 à I08 (publiés au format WebP pour alléger le dépôt). Écartées : I01 et I02, identiques (empreinte) aux illustrations P01 et P02 déjà publiées.
Réserves : photos synthétiques, non attribuables à Panzani ; gants et matériel illustratifs, sans classe ni marquage lisibles (PN04 : ne pas lire les couleurs comme une classe de gants) ; notices fabricant citées (Chauvin Arnoux C.A 703 et C.A 751) non lues par Claude ; sources S02 et S04 du lot : la FAQ INRS publie seulement des intitulés de questions, l'ED 6109 a été lue directement par Claude.
Scénarios : tri du 19/10 selon la consigne « rien de fantaisiste, seulement ce qui est sourcé solidement ». C12 (circuit protégé à 80 A) supprimé : cas non sourcé. C04 reformulé sur l'étendue de l'intervention (ED 6127, p. 13) et la répartition consignation / travaux (OPPBTP). Les 11 scénarios restants reposent sur des principes lus dans l'ED 6109, l'ED 6127 et l'OPPBTP ; C07 s'appuie en outre sur une notice fabricant non lue (S07).

## Confirmations du 19/10/2026 (suite)
Confirmé par source primaire ou institutionnelle lue :
- Zone de voisinage : de la pièce nue jusqu'à 3 m pour les tensions jusqu'à 50 kV (BT comprise) ; arrêté du 9 juillet 2013, art. 2, texte relayé par l'INERIS (SSTIE). En BT, la limite du voisinage renforcé se confond avec la distance minimale d'approche (INRS ED 6127, p. 40) = 0,30 m (annexe de l'arrêté, ligne 1 kV : distance de garde 0,30 m, DMA 0,30 m). Le parcours dit donc : voisinage jusqu'à 3 m, renforcé jusqu'à 0,30 m. Les planches GPT (« simple jusqu'à 0,30 m », cote 0,10 m) étaient fausses.
- BR (INRS, page « Opérations sur les installations électriques ») : interventions BT générales (recherche de panne, mesures, essais, manœuvres, remplacement de matériel défectueux, mise en service partielle temporaire) ; hors tension sauf certaines connexions/déconnexions dans les seuils de la NF C 18-510 ; peut réaliser la consignation pour son compte sans habilitation BC ; admis hors tension, en voisinage simple et en voisinage renforcé. BS : exclusivement hors tension et en l'absence de voisinage. Travaux sous tension : exceptionnels ; opérations hors tension en priorité.
- Voisinage (INRS, même page) : en voisinage renforcé, opérations d'ordre non électrique interdites, sauf H0V en HT.
- Recyclage (INRS, journée technique « Habilitation électrique des travailleurs ») : périodicité à définir par l'employeur selon les opérations ; 3 ans recommandés.
Restent non confirmés (texte de la NF C 18-510 non lu) : les noms exacts DLVS/DLVR/DLI en BT dans la norme ; qui peut assister un BR (effectif, titre de l'assistant) ; la FAQ INRS publie des intitulés sans réponses lisibles.
Lien consultable : https://ben2flandre-coder.github.io/consulteam-academy/sessions/a260bna/
