# Contrôles A260BNA — 19 octobre 2026
| Contrôle | Résultat |
|---|---|
| 5 pages rendues (Chromium, 1280 px et 390 px) | Aucune erreur JavaScript propre au support |
| Débordement horizontal mobile | Aucun après correction (tableaux défilables) |
| Évaluation : 37 questions | Jeu de réponses attendues : 37/37 ; question d'ordre testée |
| Galerie | 17 images déposées avec bandeau « non validée »  ; 0 image cassée (contrôle Chromium, serveur local) |
| Données nominatives | Aucune |
Limite : le chargement du manifeste de la galerie échoue en ouverture directe de fichier ; servir par HTTP (GitHub Pages ou serveur local).

## Passe du 19/10/2026 (cours de base + compléments)
- Cours chargé par HTTP (Chromium) : 14 vues parcourues sans erreur JavaScript ni ressource en erreur ; aucune mention « DGA/Toulon » dans les pages de session.
- Carte « Panzani » sur l'accueil du cours, cas H0V B2V BR BC ajoutés à la page des cas, médiathèque dans la galerie du cours (26 visuels, 0 cassé).
- Ordre des réponses mélangé : le questionnaire de base avait 26 réponses justes sur 32 en position B ; après mélange, répartition variable à chaque chargement (contrôlé).
- Espace formateur du cours verrouillé par code.
- Médiathèque : 3 planches d'ensemble, 15 extraits, 8 illustrations HD schématiques, toutes avec avertissement de non-validation ; la planche des zones reste à refaire.

## Médiathèque intégrée (19/10/2026)
- `mediatheque/` : 26 médias, 26 fiches, 12 scénarios, projection, cahier apprenant : toutes les pages s'ouvrent sans erreur ni ressource manquante (Chromium, HTTP).
- Galerie du site et galerie du cours : 26 visuels chargés, aucun cassé, pas de débordement mobile.
- Anciennes maquettes retirées de la galerie (voir `REGISTRE-SOURCES.md`).
- Relecture indépendante des SVG et des corrigés : non réalisée.

## Lot panneaux/images et tri des scénarios (19/10/2026)
- Galerie du site et du cours : 40 visuels (24 schémas, 2 + 6 images, 8 panneaux), aucun cassé, aucune erreur JavaScript, pas de débordement mobile.
- Scénarios : 11 conservés (C12 supprimé, C04 reformulé) ; liens internes de la médiathèque revérifiés.

## Confirmations (19/10/2026, suite)
- Parcours et évaluation recalés sur l'arrêté du 9 juillet 2013 (zone jusqu'à 3 m ; BT : voisinage renforcé 0,30 m) et sur la page INRS « Opérations sur les installations électriques » (BR consigne pour son compte). Évaluation : jeu de réponses attendues 37/37 avec ordre mélangé.

## Contrôles du 19 octobre (accès, agrandissement, évaluation)
- Espace formateur : 34 pages chiffrées (AES-GCM, clé dérivée de l’e-mail et du code par PBKDF2). Mauvais code refusé ; bon code accepté ; navigation entre pages formateur sans ressaisie dans la session. Protection côté navigateur : elle écarte les lecteurs occasionnels, elle ne remplace pas un serveur authentifié.
- Agrandissement : galerie, médiathèque et cours (clic, flèches, Échap) testés.
- Mentions « non validé » : retirées des pages apprenants (galerie, cours, SVG, médiathèque) ; le registre des statuts est dans l’espace formateur.
- Évaluation : inscription obligatoire ; correction contrôlée (37/37 si tout juste, 36/37 avec une erreur, 0/37 sans réponse) ; position de la bonne réponse répartie (15/12/9/4 sur les rangs 1 à 4) ; résultat envoyé par e-mail prérempli ou téléchargé, point de collecte automatique possible (`assets/config.json`).

## 19 octobre, lots GPT « affiche corrigée » et « 14 parties »
- Archives lues en entier ; empreintes SHA-256 des 14 PNG vérifiées avant conversion en WebP ; planches 03, 06, 13 relues en plein format.
- Contrôle de fond : consignation dans l’ordre ED 6109 (séparer, condamner, identifier, vérifier l’absence de tension, MALT/CC), rôles B2V/BR/BC conformes à l’ED 6127, aucune cote ni classe inventée. Aucune correction nécessaire.
- Intégration : 15 visuels dans la galerie (55 au total), section « L’affiche en 14 parties » dans la médiathèque, page de corrigés réservée au formateur.
- Logos Consulteam Groupe et Groupe Valto en en-tête, pied de page, médiathèque et écran d’accès formateur.

## Contrôles du 19/10/2026 — red team, animation, consolidation
- Évaluation : 42 questions, correction vérifiée (42/42 sur réponses exactes, 0 sur vide), mailto prérempli, ordre des réponses mélangé.
- Mode animation : 56 diapositives (version de travail 17 remplacée), 0 image cassée, aucune erreur JS, accès par e-mail et code (Chromium headless).
- Pages publiques : aucune mention « non validé », aucun débordement horizontal (bureau et mobile), galerie 55 images, lightbox active.
- Limites : texte de la NF C 18-510 non consulté ; validation du contenu par Anaïs Iversi en attente ; test sur appareil réel et sur le site en ligne à refaire après publication.
- Mode animation : accès par l'accueil, la navigation et la page formateur ; boutons ‹ ›, sommaire déroulant, clavier, balayage tactile ; défilement vertical contrôlé à 1366 et 390 px, sans débordement horizontal ; 45 questions à l'évaluation.
