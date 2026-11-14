# Rapport d'audit — plateforme A260E2A (14/11/2026)

Durée retenue : 21 h dont 7 h de pratique (programme Consul Team HE-BTHT-INI-21). Référentiel : INRS (ED 6127, FAQ, diaporama, guide SST, ED 325), qui fait foi pour la formation.

## Résultats
| Contrôle | Résultat | Preuve |
|---|---|---|
| Conformité au programme commandé | 32 exigences sur 32 conformes (la réalité virtuelle est hors périmètre de cette session) | audit-conformite-programme.md |
| Conformité réglementaire | 14 points sur 14 vérifiés : seuils BS/BR (ED 6127, FAQ et diaporama INRS), voisinage (arrêté du 9 juillet 2013, ED 6127), zones 1 à 4 (tableau ED 6127), arrêtés de 2013 et 2024, NF C 15-100, ED 325 | audit-conformite-reglementaire.md |
| Études de cas d'accidents (module 23) | Les 8 récits comparés au texte de l'ED 325 (26 cas : 13 contacts directs, 6 indirects, 7 brûlures ou explosions) ; 4 résumés corrigés (boîte de jonction, échelle contre la cellule voisine, brûlures, décompte « quatre cas sur huit ») | S32 du registre |
| Traçabilité des contenus | 450 affirmations, 0 sans référence, 0 nombre non déclaré | matrice-affirmations-sources.csv, controle-valeurs-chiffrees.json |
| Banque de questions | 279 questions, 8 au moins par module. QCM par niveau de 16 questions (ED 6127 : 15 au minimum), 4 par thème, tirées d'une base d'au moins 20 questions par thème (cinq fois plus) : dangers 20, zones 20, protections 30, limites de chaque niveau de 20 à 24 | controle-ratio-questions.json, test-evaluations.json |
| Arbres de décision de remplacement | Page « Puis-je remplacer ? » : lampe, fusible, socle de prise ; 21 chemins testés, chaque chemin mène à une issue (arrêt, à faire avant, remplacement possible) | test-arbres-remplacement.json |
| Accessibilité (axe, WCAG 2.1 AA) | 0 violation sur 14 pages, clair et sombre | qa-accessibilite-axe.json |
| Affichage | 64 combinaisons (16 pages × 4 appareils), 0 débordement, 0 erreur | qa-responsive.json |
| Hors ligne | service worker prêt, pages et images chargées sans réseau | test-hors-ligne.json |
| Studio et évaluations | 0 erreur | test-studio.json, test-evaluations.json |

## Ajouts de cette passe
Arbres de décision lampe, fusible, prise ; 68 questions pour atteindre le ratio de l'ED 6127 ; corrections du module 23 d'après l'ED 325 ; section de vidéos officielles de l'INRS (Napo, webinaire, interview) sur la page Ressources ; mentions périmées retirées des pages publiques (durée « en hypothèse », modules « en rédaction »).

## Ce qui reste à faire par Benoît
- Relecture technique des modules, schémas, images IA, grilles pratiques et documents de session avant la session de décembre.
- Décision sur `main` (fusion directe, pull request ou attente) ; les liens apprenants sont actifs après fusion.

## Précisions de méthode
- La norme NF C 18-510 est payante et n'est pas reproduite ; les seuils et périmètres suivent le référentiel INRS. L'amendement A2 (juin 2023, applicable octobre 2024) ne change aucun seuil relevé.
- Les sections ajoutées directement dans build_site.py (module 8) et les pages de décision ne sont pas couvertes par le contrôle automatique : relues à la main.
