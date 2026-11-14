# Rapport d'audit — plateforme A260E2A (14/11/2026)

Durée retenue : 21 h dont 7 h de pratique (programme Consul Team HE-BTHT-INI-21). Référentiel : INRS (ED 6127, FAQ, diaporama, guide SST, ED 325), qui fait foi pour la formation.

## Résultats
| Contrôle | Résultat | Preuve |
|---|---|---|
| Conformité au programme commandé | 32 exigences sur 32 conformes (la réalité virtuelle est hors périmètre de cette session) | audit-conformite-programme.md |
| Conformité réglementaire | 14 points sur 14 vérifiés : seuils BS/BR (ED 6127, FAQ et diaporama INRS), voisinage (arrêté du 9 juillet 2013, ED 6127), zones 1 à 4 (tableau ED 6127), arrêtés de 2013 et 2024, NF C 15-100, ED 325 | audit-conformite-reglementaire.md |
| Études de cas d'accidents (module 23) | Les 8 récits comparés au texte de l'ED 325 (26 cas : 13 contacts directs, 6 indirects, 7 brûlures ou explosions) ; 4 résumés corrigés (boîte de jonction, échelle contre la cellule voisine, brûlures, décompte « quatre cas sur huit ») | S32 du registre |
| Traçabilité des contenus | 589 affirmations, 0 sans référence, 0 nombre non déclaré | matrice-affirmations-sources.csv, controle-valeurs-chiffrees.json |
| Banque de questions | 333 questions, 8 au moins par module. QCM par niveau de 16 questions (ED 6127 : 15 au minimum), 4 par thème, tirées d'une base d'au moins 20 questions par thème (cinq fois plus) : dangers 22, zones 24, protections 34, limites de chaque niveau de 22 à 28 | controle-ratio-questions.json, test-evaluations.json |
| Arbres de décision de remplacement | Page « Puis-je remplacer ? » : lampe, fusible, socle de prise ; 21 chemins testés, chaque chemin mène à une issue (arrêt, à faire avant, remplacement possible) | test-arbres-remplacement.json |
| Accessibilité (axe, WCAG 2.1 AA) | 0 violation sur 14 pages, clair et sombre | qa-accessibilite-axe.json |
| Affichage | 68 combinaisons (17 pages × 4 appareils), 0 débordement, 0 erreur | qa-responsive.json |
| Hors ligne | service worker prêt, pages et images chargées sans réseau | test-hors-ligne.json |
| Studio et évaluations | 0 erreur | test-studio.json, test-evaluations.json |

## Adaptation au métier d'ADI sécurité (installation, vérification et maintenance de SSI)
Le support de départ (A260BNA, Panzani) était générique. Il est adapté à l'activité d'ADI :
- **Module 17 réécrit** « Chez ADI : installer, vérifier et maintenir des systèmes de sécurité incendie » : chaîne SDI/SMSI (détecteurs, déclencheurs, ECS, CMSI, DAS), catégories A à E et types d'alarme, alimentations (AES, batteries), cadre de maintenance (NF S 61-933, dossier technique, mesures compensatoires), visite de vérification geste par geste, désenfumage, éclairage de sécurité, portes coupe-feu, extincteurs et RIA, opérations et symboles à étudier, 22 questions.
- **Section « Chez ADI » dans 20 modules** (1 à 16, 18, 19, 21), chacune avec 2 questions : batterie qui reste une source après coupure du secteur, essai d'asservissement à annoncer à l'exploitant, dépannage au-delà du BS, HT hors métier, pratique sur centrale avec batterie.
- **Habilitations du métier** : la fiche RNCP 29900 prévoit B2(V), B2(V) Essais, BR, BC et H0, limitées aux installations de sécurité incendie y compris leurs alimentations basse tension (S41). La liste des symboles retenus par ADI reste à fixer par son employeur ; tout rattachement opération-symbole est marqué [R].
- **Sources ajoutées** S41 à S51 (France Compétences, Legrand, EPS Formation SSI et AES, AFNOR NF S 61-933 en fiche, CNPP, tableaux de vérifications, cahier des charges de maintenance). Les normes SSI n'ont pas été lues en texte intégral : périodicités et autonomies à confirmer par le formateur.
- **Mode animation enrichi** : chaque section est découpée en diapositives courtes, mention « Chez ADI », décision avec « Voir la réponse », 4 questions flash par module (de 19 à 31 diapositives par module au lieu de 9).

## Ajouts de la passe précédente
Mode animation : QR code par module (renvoi vers le module sur téléphone), trois QR sur la page Suivre, diapositives des modules 10, 11 et 18 (reprises du support Panzani) qui n'apparaissaient pas, QR décodés et vérifiés.

Arbres de décision lampe, fusible, prise ; 68 questions pour atteindre le ratio de l'ED 6127 ; corrections du module 23 d'après l'ED 325 ; section de vidéos officielles de l'INRS (Napo, webinaire, interview) sur la page Ressources ; mentions périmées retirées des pages publiques (durée « en hypothèse », modules « en rédaction »).

## Ce qui reste à faire par Benoît
- Relecture technique des modules, schémas, images IA, grilles pratiques et documents de session avant la session de décembre.
- Décision sur `main` (fusion directe, pull request ou attente) ; les liens apprenants sont actifs après fusion.

## Précisions de méthode
- La norme NF C 18-510 est payante et n'est pas reproduite ; les seuils et périmètres suivent le référentiel INRS. L'amendement A2 (juin 2023, applicable octobre 2024) ne change aucun seuil relevé.
- Les sections ajoutées directement dans build_site.py (module 8) et les pages de décision ne sont pas couvertes par le contrôle automatique : relues à la main.
