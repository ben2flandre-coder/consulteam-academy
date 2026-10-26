# AIPR 260018A — contrôles du 26 octobre 2026

| Contrôle | Résultat |
|---|---|
| 18 pages, Chromium, 390 × 844 et 1280 × 800 | Aucun débordement horizontal (espace formateur verrouillé et ouvert compris) |
| Console JavaScript, réponses HTTP | Aucune erreur, aucune réponse >= 400 |
| Entraînement type examen | 30 questions dont 3 prioritaires ; toutes justes = 60/60 ; toutes fausses = −42/60 (3×−5 + 27×−1) ; seuil 36 |
| Espace formateur chiffré (AES-GCM, PBKDF2 250 000) | Mauvais code refusé ; bon code ouvre le contenu |
| Code formateur / données personnelles | Absents du dossier (recherche textuelle) |
| Chiffres réglementaires | Chacun rattaché à une source du registre |

Limite connue : le code formateur est court ; un chiffrement côté navigateur sur un dépôt public ne résiste pas à une attaque hors ligne déterminée. L'espace formateur ne contient donc que du contenu pédagogique, sans donnée personnelle ni confidentielle.

Non vérifié : vrais téléphones, lecteur d'écran, impression. Contenu non relu par Consul Team.
