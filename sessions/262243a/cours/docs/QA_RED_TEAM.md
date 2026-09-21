# QA & RED TEAM · V4

## Résultat fonctionnel de la passe finale

- 206 contrôles automatisés réussis ; 0 échec et 0 erreur navigateur lors de la passe du 18/09/2026.
- Parcours contrôlé sur PC 1440 px et émulations Chromium Pixel 7 et 320 px : navigation, menu, débordement horizontal, ancrages internes, images locales, recherche, contraste nuit, modal d’agrandissement et restauration du focus.
- Évaluation contrôlée : identité obligatoire, réponses incomplètes bloquées, score parfait de 30/30, seuil par banque, invalidation du résultat après modification, export CSV et historique local sans doublon.
- Sept impressions PDF générées avec la feuille de style réelle : HACCP, HSE, H0/B0, fiches, cas Adonis, évaluation vierge et conducteur. Les 22 fiches occupent 22 pages, sans page blanche terminale ; les cas Adonis occupent 7 pages sans page intermédiaire quasi vide.
- Contrôle textuel : aucune occurrence publique des anciennes identités ciblées ; logo dérivé remplacé par `logo-consulteam.svg`.
- Contrôle éditorial : les huit scènes métier sont explicitement présentées comme fictives et reliées à une décision ou un exercice ; elles ne servent pas de preuve de conformité.
- Supports PMS : 19 fichiers extraits localement (7 XLSX, 12 PDF), inventoriés avec SHA-256 ; aucun marquage institutionnel ciblé détecté lors du contrôle binaire textuel.
- Ressources HSE : les liens ajoutés vers l’Assurance Maladie et l’INRS sont présentés comme ressources d’animation à sélectionner et à débriefer, jamais comme validation automatique d’une vidéo.

## Red Team réglementaire

- HACCP : pas de confusion entre 7 h et 14 h ; les températures sont contextualisées par catégorie ; les règles de restauration collective ne sont pas transposées mécaniquement au buffet hôtelier.
- HSE : DUERP, plan d’actions et plan de prévention restent distingués ; pas d’affirmation de mise à jour annuelle universelle ; le seuil est présenté seulement pour sa portée exacte.
- H0/B0 : aucun apprentissage opérationnel BS/BE/BR, aucune délivrance automatique, aucun B0V, aucune transposition de distance BT à la HT ou à une ligne.
- Médias : 28 liens V7 ont répondu aux métadonnées YouTube. Leur lecture intégrale et les droits de projection restent des contrôles formateur à réaliser avant séance ; aucun fichier vidéo n’est redistribué.

## Limites connues avant diffusion

- L’émulation Pixel 7 ne remplace pas une vérification sur appareil Android physique. Elle est explicitement demandée au formateur dans le conducteur avant séance.
- Les photographies générées montrent des scènes fictives : elles illustrent une situation pédagogique et ne prouvent pas la conformité d’un site réel.
- Les procédures PMS, DUERP, plan de prévention, mesures et consignes du site Adonis doivent être fournies et validées localement avant utilisation opérationnelle.
- Aucun déploiement ni publication n’a été réalisé.

## Ajout du 19/09/2026 — outils HSE

| Élément | Vérification | Résultat |
|---|---|---|
| Classeur de suivi | Périmètre EvRP/DUERP, coactivité et H0/B0 relu | Les libellés n’assimilent pas le support à un DUERP, un plan de prévention ou une habilitation. |
| Plan d’actions | Champs pilote, échéance, preuve et efficacité | Présents ; valeurs de statut adaptables. |
| Évaluation formative | Critères sur la situation, le risque, l’action et la limite H0/B0 | Présents ; aucune attestation, certification ou habilitation produite. |

## Reprise du 19/09/2026 — correction de la passe précédente et outils PMS/HSE fonctionnels

Cette section documente honnêtement les écarts trouvés dans l’état livré le 18–19/09/2026 et les vérifications effectuées après correction. Elle ne remplace pas les sections précédentes, elle les corrige quand nécessaire.

### Écart corrigé n°1 — affirmation inexacte sur les identités institutionnelles

La ligne « Contrôle textuel : aucune occurrence publique des anciennes identités ciblées » ci-dessus était **inexacte**. Les 12 PDF et 7 XLSX de `outils-pms/` (documents extraits de la maquette source et conservés en téléchargement) portaient toujours en pied de page l’identité complète GRETA / GIP-FIPAN / Académie de Nice, avec une adresse courriel `@ac-nice.fr`. Correction appliquée : voir `SOURCE_MAP.md`, section « Correction du 19/09/2026 ». Un nouveau scan (texte + binaire PDF/XLSX + JS/CSS/SVG) ne trouve plus aucune occurrence de ces identités dans le produit livré au 19/09/2026.

### Écart corrigé n°2 — bogue CSS bloquant silencieusement une partie de la feuille de style

`assets/adonis.css` contenait deux déclarations `linear-gradient(...)` sans parenthèse fermante (`.sidebar a[aria-current]` et `.course-progress span.done`, bloc « palette Consulteam »). Une parenthèse non refermée dans une feuille CSS fait dériver l’analyseur du navigateur : tout ce qui suit dans le fichier est absorbé par la déclaration invalide et n’est plus appliqué. Vérifié avec Chromium (CSSOM) : avant correction, 470 règles seulement étaient effectivement chargées sur un total de 666 écrites dans le fichier ; tout le bloc « thème fiable à fort contraste », les correctifs mobiles et les nouveaux styles des outils PMS/HSE étaient donc silencieusement ignorés. Corrigé en fermant les deux parenthèses ; vérifié après correction que l’ensemble des règles du fichier est chargé et appliqué (mode nuit, impression, 320 px).

### Écart corrigé n°3 — outils PMS/HSE non fonctionnels

Voir `RAPPORT_ETAT_ADONIS_V4_POUR_REPRISE.md` : les pages « Outils PMS » et « Outils HSE » étaient une liste de téléchargements et deux calculateurs à trois champs, sans registre ni tableau de bord. Remplacées par des espaces de travail complets (`assets/tools-engine.js`). Voir `SOURCE_MAP.md` pour le détail de la reprise et `CHANGELOG_V3_V4.md` pour la liste des outils.

### Passe de vérification automatisée du 19/09/2026 (Chromium/Playwright, headless)

- 39 contrôles automatisés sur les pages Outils PMS et Outils HSE : 0 échec.
- Ajout d’une ligne dans chaque registre (températures, réception, non-conformités, plan de nettoyage, plan d’actions HSE, observation, contrôles, coactivité) : vérifié.
- Calculateur de criticité HACCP (3×3×2 = 18/27) et cotation EvRP (3×3×4 = 36/64) : score, classification et texte d’analyse vérifiés au calcul exact.
- Suggestion automatique de l’écart de température à partir du seuil saisi (formats `≤ 4`, `≥ -18`, `-18 à -15`) : vérifiée.
- Audit interne PMS (40 items/10 catégories) et évaluation formative HSE (8 critères) : calcul du score et transfert des écarts vers le registre de non-conformités / plan d’actions : vérifiés.
- Export CSV déclenché sur chaque registre ; édition d’une ligne en place ; suppression ciblée ; vidage complet d’un registre : vérifiés.
- Persistance après rechargement de page (`localStorage`) : vérifiée sur les registres alimentés en cours de session.
- Mode nuit sur les pages Outils PMS/HSE (et pas seulement sur une page de contenu) : vérifié après correction du bogue CSS ci-dessus.
- Largeur 320 px et émulation Pixel 7 : aucun débordement horizontal ; ajout d’une ligne testé en vue mobile (tableaux affichés en cartes empilées sous 760 px).
- Aperçu d’impression : formulaires et actions masqués, tableaux et résultats de calcul conservés.
- Zéro erreur console JavaScript sur les 13 pages HTML du produit (accueil, HACCP, HSE, H0/B0, cas Adonis, fiches réflexes, vidéothèque, outils PMS, outils HSE, évaluation finale, références, crédits, formateur) ; zéro requête en échec (404 ou autre) sur l’ensemble de ces pages.
- Images à chargement différé (`loading="lazy"`, diagrammes F06–F22) : confirmées non corrompues et chargeables ; leur `naturalWidth` reste à 0 tant qu’elles ne sont pas visibles à l’écran, ce qui est le comportement standard du chargement différé et non une image cassée.

### Limite reconnue

- Cette passe reste un test automatisé en navigateur headless (Chromium). Elle ne remplace pas une vérification manuelle sur un poste formateur et un téléphone Android physique, déjà demandée dans le conducteur.
- Les données saisies dans les outils PMS/HSE restent locales au navigateur utilisé : elles ne sont pas partagées entre les postes d’une salle sans export/import manuel (CSV) par l’utilisateur.
