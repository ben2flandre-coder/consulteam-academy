# Habilitation électrique B0 · H0(V) — session 260535A

Support de la session inter-entreprises 260535A (HE-NE-INI-07, personnel non électricien, initiale), lundi 16 novembre 2026, Consul Team Six-Fours-les-Plages.

Site statique (GitHub Pages) : à partager aux stagiaires avec l’adresse de la page concernée, jamais avec le lien du dépôt.

- `index.html`, `parcours.html`, `reperes.html`, `evaluation.html` : pages stagiaires.
- `assets/config.json` : `destinataire` et `endpoint`, **vides dans le dépôt** (aucune adresse publique). Les adresses de réception sont transmises par le lien privé du formateur (`evaluation.html#r=…`, lu puis effacé de la barre d’adresse). Le bouton d’envoi ouvre le courriel du stagiaire, qui l’envoie lui-même ; le formateur voit aussi le résultat à l’écran avant le départ. Aucun résultat ni nom n’est conservé sur le site.
- `livret-participant-260535A.pdf` : livret du participant (13 pages A4), envoyé après la séance depuis l’espace formateur (lien, pas de pièce jointe).
- `formateur.html` (champ unique des adresses des participants ; courriel « évaluation » pendant la séance, courriel « site et livret » après ; déroulé, matériel, vigilance) et `animation.html` (22 diapositives, notes, chrono) : pages réservées, **chiffrées** (e-mail + code, déchiffrement dans le navigateur par `assets/gate.js`). L’e-mail et le code ne sont écrits dans aucun fichier : ils se fournissent par variables d’environnement au chiffrement.
- `evaluation.html` ne s’ouvre qu’avec le lien d’ouverture fabriqué dans l’espace formateur.

Aucune donnée personnelle (stagiaires, employeurs) n’est publiée. Le titre d’habilitation est délivré par l’employeur.

## Ajouts du 15 novembre 2026 (visuels, missions, secours, cours complet)
- `missions.html` : à quoi servent B0, H0, H0V (rôles, « V », ce qu’on ne fait jamais, jeu de 9 situations).
- `secours.html` : accident électrique (protéger, examiner, alerter, secourir), deux scénarios à choix, renvoi vers la plateforme SST du dépôt (`../sst/`).
- `cours/` : cours complet de la plateforme (socle électrique, séquences, repères, vidéothèque, livret), dérivé du cours de base des plateformes Consul Team ; modules BS et BE Manœuvre retirés (hors programme). Chargé par `cours/index.html` qui adapte dates, lieu et périmètre.
- `assets/img/{v,p,s,m}` : visuels (schémas Consul Team, photographies libres, illustrations SST, planches pédagogiques). Crédits dans `REGISTRE-SOURCES.md` et en bas de la page Repères.
- `animation.html` : 32 diapositives illustrées, deux diapositives « À vous » à réponse masquée (touche R).
