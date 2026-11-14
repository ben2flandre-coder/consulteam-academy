# Rapport d'audit — plateforme A260E2A (14/11/2026)

Durée retenue : 21 h dont 7 h de pratique (programme Consul Team HE-BTHT-INI-21).

## Résultats
| Contrôle | Résultat | Preuve |
|---|---|---|
| Conformité au programme commandé | 30 exigences conformes sur 31 ; seul écart : réalité virtuelle (équipement du centre, hors plateforme) | audit-conformite-programme.md |
| Conformité réglementaire | 13 vérifiés sur 14 (référentiel INRS : ED 6127, FAQ, diaporama, ED 325, TS876, guide SST ; arrêtés de 2013 et 2024 ; NF C 15-100) ; 1 réserve : détail de chaque récit du module 23 à comparer à l'ED 325 | audit-conformite-reglementaire.md |
| Traçabilité des contenus | 405 affirmations, 0 sans référence, 0 nombre non déclaré (sections ajoutées dans build_site.py du module 8 relues à la main) | matrice-affirmations-sources.csv, controle-valeurs-chiffrees.json |
| Banque de questions | 211 questions, au moins 8 par module ; 12 évaluations par niveau, générale complète, tirage de 75 | audit-conformite-programme.md, test-evaluations.json |
| Accessibilité (axe, WCAG 2.1 AA) | 0 violation sur 13 pages, clair et sombre (affichage clair forcé) | qa-accessibilite-axe.json |
| Affichage | 60 combinaisons (15 pages × 4 appareils) sans débordement ni erreur | qa-responsive.json |
| Hors ligne | service worker prêt, page et images chargées sans réseau | test-hors-ligne.json |
| Studio et évaluations | 0 erreur | test-studio.json, test-evaluations.json |

## Ajouts de cette passe
Fiche individuelle de parcours et mention accessibilité handicap (exigences du programme), module 8 complété (INRS S33 à S35), sources S36 à S40 (arrêté de 2013, FAQ et diaporama INRS, amendement A2, NF C 15-100), 46 questions, mode clair forcé, tableaux accessibles au clavier.

## Ce qui reste hors de portée de cette session
- NF C 18-510 (norme payante) : texte non lu, mais seuils BS/BR et périmètre alignés sur le référentiel INRS (ED 6127, FAQ, diaporama), qui fait foi pour la formation ; amendement A2 (juin 2023, applicable octobre 2024) précise les interventions sans nouveau seuil relevé. Relecture finale par le formateur.
- Relecture technique par un formateur habilité : modules 9, 12 à 17, 19 à 23, schémas, images IA, grilles pratiques, documents de session.
- Détail de chaque récit du module 23 à comparer à l'ED 325 (édition et thèmes confirmés) ; le ratio de cinq fois plus de questions que posées (ED 6127) n'est pas atteint par niveau.
- Arbres de décision détaillés de remplacement (lampe, fusible, prise) et vidéos non produits ; équipement de réalité virtuelle non couvert.
