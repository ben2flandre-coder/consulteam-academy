# Habilitation électrique B0 · H0(V) — session 260535A

Support de la session inter-entreprises 260535A (HE-NE-INI-07, personnel non électricien, initiale), lundi 16 novembre 2026, Consul Team Six-Fours-les-Plages.

Site statique (GitHub Pages) : à partager aux stagiaires avec l’adresse de la page concernée, jamais avec le lien du dépôt.

- `index.html`, `parcours.html`, `reperes.html`, `evaluation.html` : pages stagiaires.
- `assets/config.json` : `destinataire` et `endpoint`, **vides dans le dépôt** (aucune adresse publique). Les adresses de réception sont transmises par le lien privé du formateur (`evaluation.html#r=…`, lu puis effacé de la barre d’adresse). Le bouton d’envoi ouvre le courriel du stagiaire, qui l’envoie lui-même ; le formateur voit aussi le résultat à l’écran avant le départ. Aucun résultat ni nom n’est conservé sur le site.
- `livret-participant-260535A.pdf` : livret du participant (13 pages A4), envoyé après la séance depuis l’espace formateur (lien, pas de pièce jointe).
- `formateur.html` (champ unique des adresses des participants ; courriel « évaluation » pendant la séance, courriel « site et livret » après ; déroulé, matériel, vigilance) et `animation.html` (22 diapositives, notes, chrono) : pages réservées, **chiffrées** (e-mail + code, déchiffrement dans le navigateur par `assets/gate.js`). L’e-mail et le code ne sont écrits dans aucun fichier : ils se fournissent par variables d’environnement au chiffrement.
- `evaluation.html` ne s’ouvre qu’avec le lien d’ouverture fabriqué dans l’espace formateur.

Aucune donnée personnelle (stagiaires, employeurs) n’est publiée. Le titre d’habilitation est délivré par l’employeur.
