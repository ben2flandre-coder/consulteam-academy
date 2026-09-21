# SOURCE MAP · V4

Consulté le 18 septembre 2026. Cette carte distingue les apports documentaires des éléments adaptés : elle ne prétend pas importer une source telle quelle.

| Source | Apport contrôlé dans V4 | Emplacements V4 |
|---|---|---|
| `ben2flandre-coder/pms_V4` | Structure PMS, séquences opérationnelles, dangers, BPH, nettoyage, HACCP, traçabilité, études de cas. Les températures, durées, allergènes et conservation ont été revérifiés et corrigés si nécessaire. | HACCP H01–H08, F01–F08, cas « Flux petit-déjeuner » |
| Dépôt PSE prévention hôtellerie | Chaîne danger → situation → exposition → dommage, EvRP, priorisation, plan d’actions, coactivité. Les anciennes identités et les assertions réglementaires non confirmées ne sont pas reprises. | HSE S01–S05, F09–F15, cas HSE/coactivité |
| `ben2flandre-coder/livret-pse-aepe` | Démarche de prévention transposable à l’hôtellerie et formulations pédagogiques. | HSE S01, S03, S05 |
| `Consulteam_V7_Formateur_Maquette.zip` | Charte de départ, visuels techniques, structure d’évaluation DGA et 28 liens vidéo conservés à l’inventaire. Les gestes hors H0/B0 sont exclus du parcours apprenant. | H0/B0 E01–E06, vidéothèque, formateur, évaluation finale |
| Code du travail / INRS | DUERP, plan de prévention, habilitation, missions et voisinages électriques. | S01–S05, E01–E06, F09–F22, Q S01–S10/E01–E10 |
| Règlements UE / Ministère / DGCCRF | Hygiène, allergènes, traçabilité, DLC/DDM et catégories de température. | H01–H08, F01–F08, Q H01–H10 |

## Règles de dérivation appliquées

- Les contenus repris des dépôts sont des apports pédagogiques, réécrits pour l’hôtel Adonis et reliés à une source primaire ou INRS quand une affirmation est sensible.
- Aucun logo, lien, footer, mail, métadonnée ou identité institutionnelle historique n’est retenu dans le produit.
- Les deux listes de lecture PMS sont conservées dans la version formateur comme inventaire documentaire ; les 28 liens V7 sont conservés avec un objectif d’observation et un statut à valider avant projection.
- Les créations médias V4 sont fictives ; les droits et les limites d’usage sont détaillés dans `credits-medias.html`.

## Outils HSE de suivi et d’évaluation — ajout du 19/09/2026

- `outils-hse/OUTILS_SUIVI_HSE_ADONIS.xlsx` : classeur de suivi à six onglets (mode d’emploi, plan d’actions, observation terrain, coactivité, grille évaluateur, listes adaptables).
- Périmètre : modèle opérationnel et pédagogique. Il ne constitue ni DUERP ni plan de prévention et ne délivre aucune habilitation électrique.
- Références de périmètre : Code du travail, articles R4121-1 à R4121-4 (évaluation des risques et DUERP) ; R4512-6 et suivants (prévention lors d’opérations d’entreprises extérieures) ; R4544-9 et R4544-10 (habilitation électrique par l’employeur).

## Reprise du 19/09/2026 — outils PMS et HSE transformés en espaces de travail réels

La passation précédente (`RAPPORT_ETAT_ADONIS_V4_POUR_REPRISE.md`) reconnaissait que les pages « Outils PMS » et « Outils HSE » n’étaient qu’une liste de téléchargements accompagnée de deux calculateurs à trois champs, sans registre, sans tableau de bord et sans persistance. Cette reprise remplace ces pages par des outils fonctionnels, construits dans `assets/tools-engine.js` (nouveau) et servis sans connexion.

| Mécanisme repris du dépôt `pms_V4` | Apport contrôlé dans les outils V4 Adonis | Ce qui n’est PAS repris |
|---|---|---|
| Tableau de bord relié aux enregistrements locaux (indicateurs calculés depuis les registres) | `outils-pms.html#pms-tb` et `outils-hse.html#hse-tb` : indicateurs recalculés en direct depuis les registres `localStorage` | Les libellés, le contenu HACCP détaillé et l’identité visuelle du dépôt source |
| Registre de non-conformités en tableau JSON local, ajout/suppression, sauvegarde `localStorage` | `pmsNC` : mêmes principes (ajout, édition, suppression, persistance), champs propres à Adonis (fait, détection, mesure immédiate, cause, action, pilote, échéance, statut, preuve, vérification) | Le code du dépôt n’est pas copié ; les noms de fonctions, l’HTML et le CSS sont réécrits pour Consulteam |
| Calculateur de criticité avec score, classification, justification textuelle générée et historique | `pms-haccp-calc` : méthode Fréquence × Gravité × Maîtrise, classification et analyse générée, historique conservé comme registre exportable ; transfert en un clic vers le registre de non-conformités | Les textes de justification, les seuils exacts et les dangers cités dans le dépôt (réécrits pour l’hôtellerie Adonis, présentés comme pédagogiques et non réglementaires) |
| Grille d’audit interne à sections pondérées (conforme/partiel/non conforme, score cumulé) | `pms-audit` : 10 catégories originales (hygiène, flux, réception, températures, nettoyage-désinfection, traçabilité, allergènes, maintenance/métrologie, formation, gestion des écarts), 40 items, transfert des écarts vers le registre de non-conformités | Les intitulés précis des items du dépôt (rédigés spécifiquement pour Adonis) |

Les outils HSE (cotation EvRP, plan d’actions, observation terrain, contrôles, préparation de coactivité, évaluation formative) suivent la même logique de registre local mais sont des créations originales pour ce parcours : aucun dépôt de référence ne fournissait de mécanisme HSE web équivalent (le dépôt PSE prévention est un livret de lecture, pas une application).

**Champs ajoutés :** `assets/tools-engine.js` (nouveau, ~450 lignes), section « Espaces de travail PMS/HSE » de `assets/adonis.css` (nouveau bloc CSS), `outils-pms.html` et `outils-hse.html` (réécrits en totalité).

## Correction du 19/09/2026 — identité institutionnelle résiduelle dans les supports PMS

Contrairement à ce qu’affirmait `QA_RED_TEAM.md` du 18/09/2026 (« aucune occurrence publique des anciennes identités ciblées »), les 12 fiches PDF et 7 classeurs XLSX extraits de la maquette PMS et embarqués dans `outils-pms/` portaient encore en pied de page l’identité complète « Benoit Deflandre - GRETA GIP-FIPAN - benoit.deflandre@ac-nice.fr » (PDF) ou « © Benoît Deflandre - GRETA GIP-FIPAN - Académie de Nice » (XLSX), y compris une adresse courriel institutionnelle. Ce pied de page a été retiré de chaque fichier (redaction PDF + réécriture XML du XLSX) et remplacé par « Benoît Deflandre — RMBD Risk Management — Consulteam Academy — 2026 ». Les empreintes SHA-256 de `MANIFEST_PMS_SUPPORTS.md` et `catalogue.json` ont été recalculées en conséquence. Un scan textuel et binaire (PDF, XLSX, HTML, CSS, JS, SVG, MD, JSON) confirme qu’aucune occurrence de Éducation nationale, Académie, GIP FIPAN, GRETA, IFCA, ac-nice ou FORPRO ne subsiste dans le produit livré.
