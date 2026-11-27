# Recette 1.9 — session 260053A

## Périmètre

Nœuds et livret apprenant uniquement, en conservant les corrections réglementaires et fonctionnelles de la version 1.8. Les autres sessions ne sont pas modifiées.

## Livret

- Référence visuelle examinée : première page, page intérieure et quatrième de couverture du livret 261537B présent dans `consulteam-supports`, ainsi que les sources HTML/CSS du livret A260H4A.
- 28 pages A4 portrait, bleu nuit et ambre, logo, quatrième de couverture avec QR vers `apprenants.html?e=p`, pagination n / N, fiches, cas, notes, QCM, corrigés et plan d’action.
- Contenu commun : `qa/livret_content.py`. Générateur HTML/PDF : `qa/build_livret.py`. Le PDF remplace l’export textuel paysage 1.8.
- PDF de 1 639 768 octets ; 26 signets ; polices incorporées. Contrôle des positions et de la pagination sans erreur, extraction du texte sans caractère de remplacement.
- Les 28 pages ont été rendues ; planche contact inspectée et contrôle agrandi de couverture, cabestan, QCM et quatrième de couverture.
- HTML en ligne : 28 feuilles, images chargées, lecture à 390 px sans débordement horizontal ; feuilles A4 à largeur normale sans dépassement de hauteur. L’impression physique n’a pas été effectuée ; le PDF est le fichier de diffusion de référence.

## Médias et lecture

- 13 fichiers libres intégrés, avec auteurs, sources et licences : six vues de préparation à plat du cabestan, cabestan sur barre, mule sécurisée, arrêt double, planche et photo du nœud de chaise, pêcheur double ouvert/serré.
- La photo de demi-cabestan sur connecteur sans verrouillage a été écartée de l’intégration. Aucune photo sur appareil de freinage assisté n’est présentée comme un demi-cabestan.
- Originaux non retouchés ; certaines images sont des prévisualisations Wikimedia. Les six vues de cabestan sont de petite définition, clairement annoncée.
- Pause des tracés : test en lecture lente ; valeur de parcours 308 conservée après pause et lors du contrôle suivant. Vue complète : 1000 ; touches Début/Fin : 0 et 1000.
- Vitesse, trajet en pointillés et suppression des textures vérifiés dans les commandes visibles.
- Séquence cabestan : passage direct à la vue 4, lecture puis pause vérifiées. Les deux images alors visibles ont chargé (403 et 960 px de largeur native).
- Page demi-cabestan/mule à 390 px : photo chargée, attribution visible, lien de référence Petzl présent, aucun débordement horizontal.
- Aucun message d’erreur JavaScript relevé dans le journal de l’onglet de contrôle.

## Non-régression

- `check_static.py` : 19 pages et 964 références, aucune erreur de cible locale, d’ancre statique, de syntaxe JS ou XML.
- `safety-tools.test.cjs` : 23 cas réussis.
- `roles.test.cjs` : 17 cas réussis.
- `knots.test.cjs` : quatre tracés, coordonnées finies et croisements attendus (3, 4, 16, 12).

## Limites conservées

Les tracés ouverts ne simulent ni le geste réel ni le serrage. Les photos montrent des formes de référence, sans valider une configuration antichute. Le contrôle du formateur et la validation Consulteam restent distincts de la recette informatique.

L’ancien PDF « livret du site » de 85 pages n’a pas été régénéré : il est identifié comme archive du 20/11 dans le catalogue Supports. Pour diffuser le contenu actuel, utiliser le site ou le livret apprenant 1.9 de 28 pages.
