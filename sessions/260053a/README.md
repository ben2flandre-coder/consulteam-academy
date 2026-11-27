# Session 260053a — Travail en hauteur / port du harnais (SECU37)

Session **260053A** · lundi 30 novembre 2026 · 09 h–12 h / 13 h–17 h (7 h) · Consulteam Security, 119 avenue Robert Brun, 83500 La Seyne-sur-Mer.

| Page | Usage | Diffusion |
|---|---|---|
| `index.html` | Hub | formateur |
| `animation.html` | Diaporama plein écran (notes, chrono, QCM, calculateurs) | formateur / projection |
| `apprenant.html` | Support participant | apprenants |
| `programme.html` | Programme SECU37 (texte + PDF) | tous |
| `noeuds.html` | Fiches nœuds et grille d'observation | apprenants |
| `formulaires.html` | Émargement, ouverture de zone, grille, bilan, évaluation, attestation | formateur (imprimable) |
| `formateur.html` | Déroulé, corrigés, vigilance | **formateur uniquement** |

Diffuser uniquement les liens des pages concernées, jamais celui du dépôt.
Les visuels d’équipements sont générés (non contractuels) : à remplacer par des photos réelles. Les nœuds sont dessinés d’après un trajet de corde calculé et contrôlé (test automatique) ; cabestan, demi-cabestan et mule : démonstration sur corde réelle.


## Version et traçabilité
Version **1.9 du 27/11/2026** : photos et planche libres créditées, séquence photographique cabestan, commandes de lecture et pause immédiate, livret apprenant A4 portrait standardisé de 28 pages. Sources communes HTML/PDF : `qa/livret_content.py` et `qa/build_livret.py` ; dépendances ReportLab, Pillow, pypdf et pypdfium2.

Version **1.8 du 27/11/2026** : correction des résumés R.4323-61 et R.4224-15, du délai des vérifications de l’arrêté du 19 mars 1993, des repères du tirant d’air et des consignes après suspension. Comparateur de distances selon la notice, saisies contrôlées, parcours participant conservé, stockage séparé par session, onglets accessibles au clavier, impression individuelle des formulaires, QR codes dimensionnés avec un viewBox. Livret révisé dans `pdf/` (ancienne génération depuis les HTML, remplacée en 1.9 par le contenu éditorial commun).

Recette et limites : [qa/RECETTE-1.8.md](qa/RECETTE-1.8.md). Cette reprise concerne **260053A** ; les autres sessions ne sont pas modifiées.

Version 1.7 du 27/11/2026 (revue critique : nœuds redessinés sous la forme des manuels, images générées de nœuds retirées, fiches, vidéos et références corrigées). Version 1.6 du 23/11/2026 (planches pas à pas dessinées, étapes alignées sur les fiches). Version 1.5 du 21/11/2026 (animations de nœuds, retrait de la photo du huit sur anneau). Version 1.4 du 21/11/2026 (page Nœuds : choix par usage, recherche, mode étape par étape). Version 1.3 du 20/11/2026 (reprise de la session A260B0A pour 260053A : INTER, 10 participants, salle MILLENNIUM STADIUM, commande 260053A-15752). Voir `tracabilite.html` (historique, sources, rapprochement des illustrations, validation Consulteam en attente). Horaires : 9 h–12 h / 13 h–17 h (convocation Consulteam) ; déroulé formateur et mode animation recalés.


## Livret et médias 1.9

- `livret.html` : lecture mobile et version imprimable ; `pdf/livret-formation-260053a.pdf` : fichier de diffusion de référence.
- Présentation alignée sur `consulteam-supports/pdf/261537b/livret-formation-261537b.pdf` et la trame éditoriale de `sessions/a260h4a/livret.html`. Couverture bleu nuit/ambre, quatrième de couverture et QR participant, pagination n / N.
- `assets/img/noeuds-libres/credits.json` et `credits-noeuds.html` : origine, auteur et licence des 13 médias intégrés. Les six vues du cabestan sont une préparation à plat ; elles ne simulent pas le nouage sur une barre.
- Les tracés géométriques montrent un parcours ouvert ; les photos de référence ne valident aucun système antichute.

Recette de la version 1.9 : [qa/RECETTE-1.9.md](qa/RECETTE-1.9.md).
