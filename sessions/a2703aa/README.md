# Habilitation électrique initiale A2703AA — support de session

Support de formation pour la session intra A2703AA (HE-BSBE-INI-14, B0 · H0(V) · BS · BE Manœuvre), SOTEM, Le Revest-les-Eaux, 4 et 5 janvier 2027.

Site statique (GitHub Pages) : à partager aux participants avec l’adresse de la page concernée, jamais avec le lien du dépôt.

- `index.html`, `parcours.html`, `metiers.html`, `evaluation.html`, `galerie.html`, `securite-site.html` : pages participants.
- `electricien.html` : ressource complémentaire, hors programme de la session, pour les électriciens de métier.
- `assets/config.json` : adresse de réception des résultats (`destinataire`) et point de collecte facultatif (`endpoint`) ; vides par défaut.

Aucune donnée personnelle (stagiaires, adresses) n’est publiée. Le titre d’habilitation est délivré par l’employeur.
- `animation.html`, `formateur.html` : pages réservées, chiffrées (e-mail + code) ; le code n'est jamais dans le dépôt. Mode animation de 43 diapositives (notes du formateur, révélation pas à pas, QR « Sur le site », chrono, impression) ; espace formateur (cadre de session, déroulé indicatif, vigilances, corrigés des 16 cas par métier).
- `assets/gate.js`, `assets/check.json` : contrôle d'accès côté navigateur (PBKDF2 + AES-GCM).
- `assets/svg/S01` à `S06` : scènes dessinées pour le site (vue d'ensemble, engin sous une ligne, contact engin / ligne, accueil et pesée, atelier, extérieur sous la pluie), génériques, sans personne ni marque.
