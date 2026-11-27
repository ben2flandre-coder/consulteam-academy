# Recette 260053A — version 1.8 — 27 novembre 2026

## Périmètre

Reprise de la session INTER SECU37 du 30/11/2026, à partir du commit `35d55c964ef168430b3579579a53efa4bfae8e18`. Les autres sessions sont conservées. La navigation formateur/participant reste une séparation d’usage sur un hébergement public ; elle ne constitue pas une authentification.

## Corrections de fond

- R.4323-61 : rétablissement de l’alternative entre chute libre limitée à 1 m et limitation équivalente des effets d’une chute plus haute ; maintien du non-isolement et de la notice employeur.
- Vérifications : l’arrêté du 19/03/1993 impose une vérification de moins de douze mois à l’utilisation des systèmes antichute, en service ou en stock. Correction de la mention erronée « simple pratique INRS ».
- R.4224-15 : distinction entre ateliers dangereux et chantiers dangereux d’au moins 20 travailleurs pendant plus de 15 jours. Organisation des secours à prévoir aussi dans les autres cas.
- Tirant d’air : retrait de la formule universelle à quatre termes et de la confusion pieds/ancrage ; comparaison de la valeur de notice et de l’espace disponible depuis un même repère. Le résultat ne délivre aucune autorisation de travail.
- Facteur de chute : refus des valeurs négatives et des saisies partielles ; absence de déduction automatique de l’effort ou de la position d’ancrage à partir du seul rapport. Schéma corrigé : deux longueurs de déplacement avant freinage ne sont pas un allongement de longe.
- Secours : prise en compte de la conscience, de la respiration et des consignes médicales ; le retrait du harnais ne retarde pas les gestes urgents.
- Cordes : retrait du tableau d’essais confondant les facteurs 0,3 et 1 ; remplacement par la lecture d’une fiche fabricant identifiée. Entretien selon la notice du modèle.
- Nœuds : distinction explicite entre tracé ouvert, geste et serrage réel ; aucun nouveau cheminement inventé. Contrôles géométriques conservés sans les présenter comme une validation en charge.

## Corrections de fonctionnement

Accueil participant conservé depuis les boutons de retour ; comportement prévu si le stockage du navigateur est indisponible ; suivi séparé par session ; réinitialisation des radios réellement persistante ; clavier des onglets et liens directs ; menu refermable ; boutons flottants placés sous la fenêtre de zoom ; miniatures vidéo conservées comme liens vidéo ; impression du seul formulaire demandé ; rétablissement de toutes les étapes en impression ; correction des sept QR codes aux dimensions contradictoires ; fichiers CSS/JS versionnés dans les URL ; livret PDF révisé associé à la session.

## Contrôles exécutables

Depuis ce dossier :

```text
python check_static.py
node safety-tools.test.cjs
node roles.test.cjs
node knots.test.cjs
python build_livret.py
```

Le rapport statique contrôle 17 pages et 809 références, sans cible locale absente, attribut répété, erreur d’ancre statique ou erreur de syntaxe JavaScript/XML. Les tests portent sur 23 cas de nombres et limites, 17 cas de parcours/stockage et quatre tracés de nœuds. Le livret contient 36 pages A4 paysage, dont quatre planches illustrées ; contrôle des positions de texte consigné dans `livret-layout.json`.

La validation visuelle dans le navigateur complète ces contrôles. Ils ne mesurent pas la disponibilité future des services externes et ne constituent pas une réception des équipements du site.

## Sources consultées le 27/11/2026

- [R.4323-61 — Légifrance](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000018531391/)
- [Arrêté du 19 mars 1993 — Légifrance](https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000179220/)
- [R.4224-15 — Légifrance](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000018532203/)
- [L.4131-4 — Légifrance](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000035653293/)
- [INRS — équipements de protection contre les chutes](https://www.inrs.fr/risques/chutes-hauteur/equipements-protection-individuelle-chutes-hauteur)
- [Petzl — paramètres du tirant d’air](https://www.petzl.com/fr/fr/calculateur-de-degagement/clearancecalculator.html)
- [Petzl — fiche AXIS 11 mm](https://www.petzl.com/FR/fr/Professionnel/Cordes/AXIS-11-mm-CUSTOM)
- [MSA — syndrome du harnais, avril 2025](https://ssa.msa.fr/wp-content/uploads/2025/04/SyndromeDuHarnais_avril2025-1.pdf)
- [Sécurité civile — références techniques nationales](https://www.securite-civile.interieur.gouv.fr/documentation/secourisme-et-associations/secourisme-references-techniques-nationales.html)

## Validation de la séance

Les validations Consulteam déjà signalées restent à leur état réel. Avant la pratique : réception de la zone et des ancrages, notices des modèles disponibles, compétences et moyens de secours, contrôle du matériel et observation du geste sur corde réelle. Ces éléments physiques ne peuvent pas être attestés par une correction de site web.
