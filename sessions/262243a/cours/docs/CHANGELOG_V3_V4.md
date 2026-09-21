# CHANGELOG V3 → V4

## Parcours et contenus

- Refonte complète en 19 chapitres : 8 HACCP/BPH/PMS, 5 HSE et 6 H0/B0 ; 22 fiches réflexes et 5 cas Adonis.
- Passage à une structure éditoriale dynamique inspirée de PMS : héro métier, sommaire visuel, progression, cartes de boussole, décision terrain, approfondissement et question flash.
- Séparation visible entre le niveau Adonis indispensable en séance et les méthodes, exceptions et limites à approfondir.
- Ajout de 30 questions finales indépendantes, 10 par domaine, et remplacement des réponses systématiquement positionnées au premier choix.

## Médias et identité

- Ajout de 8 scènes métier originales : service petit-déjeuner, allergènes, réception, briefing HSE, ergonomie de housekeeping, observation HSE, accès/balisage H0/B0 et briefing technique.
- Ajout, au début de chaque module, d’un regard terrain illustré avec une lecture de situation et trois décisions concrètes reliées au chapitre concerné.
- Ajout de 22 schémas vectoriels dédiés aux fiches réflexes ; conservation et contextualisation de l’inventaire complet des 28 liens V7.
- Extraction fidèle des 19 supports téléchargeables embarqués dans la maquette PMS : 7 tableurs et 12 fiches PDF, avec manifeste SHA-256 et espace local « Outils PMS ».
- Enrichissement de la vidéothèque : les sept portails réellement présents dans PMS sont distingués des vidéos ; une sélection HSE institutionnelle en français sert l’animation TMS, lombalgies et prévention.
- Refonte des cas Adonis en kit d’animation : cinq scénarios avec durée, rôles, situation, consigne, production attendue, questions de débrief et chronologie de travail.
- Remplacement du logo hérité par une signature Consulteam Academy autonome ; suppression de toute identité institutionnelle historique de la dérivation.

## Conformité et limites

- Correction ou neutralisation des généralisations non vérifiées des sources : 7 h / 14 h, températures et durées, lactose/allergène, conservation des preuves, DUERP, coactivité et voisinage électrique.
- H0/B0 maintenu strict : pas de BS, BE ou BR ; la formation et l’évaluation ne délivrent pas l’habilitation.
- V3 n’a pas été modifiée. Son SHA-256 de référence est `B55CFE65C9EA360A13F3E0ACD765ACD16BC38685FC85D4FE6CB6CC5087B81DBF`.

## Reprise du 19/09/2026 — outils PMS et HSE, correction d’un bogue CSS et d’une fuite d’identité

Cette reprise fait suite à `RAPPORT_ETAT_ADONIS_V4_POUR_REPRISE.md`, qui reconnaissait que les outils PMS/HSE n’étaient pas repris fidèlement des dépôts de référence. Voir `docs/SOURCE_MAP.md` et `docs/QA_RED_TEAM.md` pour le détail complet.

### Outils PMS — nouvel espace de travail (`outils-pms.html`)

- Tableau de bord relié en direct aux registres locaux (relevés, réceptions, non-conformités, audits, plan de nettoyage).
- Calculateur de criticité HACCP (Fréquence × Gravité × Maîtrise) avec analyse générée, historique exportable et transfert en un clic vers le registre de non-conformités.
- Suivi des températures : relevé daté, zone/équipement, seuil validé localement, mesure, écart suggéré automatiquement, décision, preuve, visa ; export CSV.
- Réception / traçabilité : fournisseur, produit, lot, DLC/DDM, état, température, décision, action ; export CSV.
- Registre de non-conformités complet : fait, détection, mesure immédiate, cause, action, pilote, échéance, statut, preuve, vérification d’efficacité ; ajout, édition, suppression, export CSV.
- Audit interne PMS : grille de 40 items sur 10 catégories (hygiène, flux, réception, températures, nettoyage-désinfection, traçabilité, allergènes, maintenance/métrologie, formation, gestion des écarts), score calculé, transfert des écarts vers le registre de non-conformités.
- Plan de nettoyage-désinfection et maintenance : tableau éditable, lignes ajoutables.
- Les 19 supports téléchargeables d’origine sont conservés comme complément, plus haut dans la page et non plus en tête de liste unique.

### Outils HSE — nouvel espace de travail (`outils-hse.html`)

- Tableau de bord HSE relié en direct aux registres locaux.
- Cotation EvRP complète (unité de travail, danger, personnes exposées, gravité, probabilité, exposition/maîtrise, justification obligatoire, mesures existantes, action, pilote, échéance) avec transfert vers le plan d’actions.
- Plan d’actions prévention, observation terrain/situation dangereuse/presque-accident, contrôles HSE, préparation de coactivité : registres complets avec export CSV.
- Évaluation formative : 8 critères observables, résultat calculé, axes de reprise, export CSV de l’historique.
- Le classeur HSE téléchargeable d’origine est conservé comme complément.

### Corrections transverses

- **Bogue CSS bloquant :** deux `linear-gradient(...)` sans parenthèse fermante dans `assets/adonis.css` faisaient échouer silencieusement l’analyse de tout le reste de la feuille de style (196 règles sur 666 non appliquées avant correction), affectant le mode nuit, l’impression et le responsive sur l’ensemble du site, pas seulement les outils. Corrigé.
- **Identité institutionnelle résiduelle :** les 12 PDF et 7 XLSX de `outils-pms/` portaient encore en pied de page l’identité GRETA / GIP-FIPAN / Académie de Nice et une adresse `@ac-nice.fr`, malgré l’exigence explicite de suppression. Corrigé (remplacement du pied de page, recalcul des empreintes SHA-256 dans `MANIFEST_PMS_SUPPORTS.md` et `catalogue.json`).
- Suppression des fichiers de contrôle internes non destinés à la diffusion (`*.xlsx.inspect.ndjson`, `CONTROLE_OUTILS_*.txt`) restés par erreur dans `outils-pms/` et `outils-hse/`.
- Ajout de `assets/tools-engine.js` (moteur des registres, calculateurs, audits et tableaux de bord des outils PMS/HSE).
