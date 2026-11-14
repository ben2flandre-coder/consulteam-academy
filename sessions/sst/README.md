# SST Consulteam — plateforme de formation (v0.3, 14/11/2026)
Formation initiale de Sauveteur Secouriste du Travail (14 h) et MAC (7 h), dispositif INRS. Site statique, à servir par HTTP (mode hors ligne par service worker). **Non indexé** (noindex), aucune donnée de stagiaire.

## Pages apprenant
`index` · `parcours` · `m1` à `m8` (un module par compétence, avec questions de fin de module) · `fiches-secourir` · `valider` · `galerie` · `glossaire` · `ressources` · `livret` (+ `pdf/livret-sst-consulteam.pdf`) · `credits`.

## Espace formateur (non lié depuis les pages apprenant : `formateur.html`)
`dj1-matin`, `dj1-apres-midi`, `dj2-matin`, `dj2-apres-midi` (déroulé de l'initiale) · `mac` · `scenarios` · `suivi` · `matrice` · `sources` · `registre` · `visuels-relecture` · `initiale`.

## Données et preuves
- `data/` : matrice des compétences, questions (32), registres (sources, visuels, statut des visuels), matrices de traçabilité.
- `preuves/` : journal des écarts, liens, accessibilité (axe) et hors ligne, scripts de contrôle, captures.
- `MANIFEST.sha256` : empreinte de chaque fichier.

## Régénération
Le site est produit par un générateur Python hors dépôt. Pour valider un visuel : passer sa ligne à `valide` dans `data/visuels-statut.csv`.

## Limites connues
Voir `preuves/RAPPORT-RED-TEAM.md`.
