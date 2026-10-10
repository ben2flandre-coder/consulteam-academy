# Livraison Bonifay A2604QA — contrôles du 10 octobre 2026

## Résultats fonctionnels

Contrôle navigateur Chromium, à partir de l'accueil du cours et du chargeur HTTP :

| Contrôle | Résultat |
|---|---|
| 13 vues générales + 8 séquences | 21 vues rendues, aucun écran vide |
| Console JavaScript | Aucune erreur pendant le parcours vérifié |
| Ressources HTTP du parcours vérifié | Aucune réponse >= 400 |
| Galerie et 5 nouveaux visuels | Toutes les images chargées |
| Navigation mobile 390 × 844 | Aucun débordement horizontal ; bouton de thème repositionné |
| Notes de séquence | Enregistrement puis rechargement : valeur conservée |
| Questionnaire final | 38 questions, total 40 points |
| Jeu de réponses attendues | 40/40, sans délivrance d'habilitation |
| Corrections Q13, Q37, Q38 | Terminologie BT, 400 V CA et 6 mm² cuivre vérifiés |
| Séparation du suivi | Clés locales dédiées A2604QA |

La passe fonctionnelle est réalisée avant la dernière retouche des styles d'impression de l'annexe ; cette retouche ne touche pas les règles métier. La dernière relance complète a rencontré un arrêt du navigateur de test au démarrage, sans accès à la page. Les PDF finaux ont ensuite été produits et contrôlés séparément.

## PDF et contrôle visuel

- Livret : 86 pages A4, cours et annexes conservés, cinq nouvelles planches en annexe. Les 81 premières pages proviennent du rendu du parcours adapté. Les cinq dernières ont une maquette PDF dédiée pour supprimer une page presque vide et des intitulés isolés.
- Évaluation imprimable : 6 pages A4, les mêmes 38 questions corrigées que le HTML ; aucune réponse du corrigé imprimée.
- Rendu de l'ensemble du livret en vignettes, inspection de la couverture, du sommaire et des dernières planches ; inspection de la première page d'évaluation. Les images sont lisibles et les textes ajoutés ne sont pas rognés.
- Sources et prompt des illustrations consignés dans `REGISTRE-SOURCES.md`.

## Préservation

Publication limitée à `sessions/a2604qa/`. Le fichier source DGA est réutilisé sans modification comme `cours/base.html`. Les autres sessions sont conservées. La création d'objets Git emploie l'arbre existant et une mise à jour de branche avec SHA attendu ; elle n'écrase pas les fichiers des autres sessions.

## Limites de recette

- La norme NF C 18-510 consolidée intégrale n'a pas été fournie : contrôle ciblé des prescriptions à partir des sources institutionnelles, sans certification exhaustive de tout le contenu hérité.
- Validation intégrale des vidéos non revendiquée ; liens et métadonnées hérités restent identifiés comme ressources à examiner.
- Titres individuels, prescriptions locales, équipements et réalisations pratiques à vérifier pendant la préparation de session.
- Écart de durée annoncé 10,5 h / créneaux 10 h signalé dans l'espace formateur ; pas de modification arbitraire des horaires.
- L'envoi de résultats via mailto dépend du logiciel de messagerie ; aucune transmission automatique ni pièce jointe automatique.
