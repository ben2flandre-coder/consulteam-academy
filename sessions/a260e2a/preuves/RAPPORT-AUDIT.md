# Rapport d'audit — plateforme A260E2A (14/11/2026)

Durée retenue : 21 h dont 7 h de pratique (programme Consul Team HE-BTHT-INI-21).

## Résultats
| Contrôle | Résultat | Preuve |
|---|---|---|
| Conformité au programme commandé | 30 exigences conformes sur 31 ; seul écart : réalité virtuelle (équipement du centre, hors plateforme) | audit-conformite-programme.md |
| Conformité réglementaire | 7 vérifiés, 6 avec réserve, 1 non vérifiable (NF C 18-510 payante non lue) | audit-conformite-reglementaire.md |
| Traçabilité des contenus | 405 affirmations, 0 sans référence, 0 nombre non déclaré (sections ajoutées dans build_site.py du module 8 relues à la main) | matrice-affirmations-sources.csv, controle-valeurs-chiffrees.json |
| Banque de questions | 211 questions, au moins 8 par module ; 12 évaluations par niveau, générale complète, tirage de 75 | audit-conformite-programme.md, test-evaluations.json |
| Accessibilité (axe, WCAG 2.1 AA) | 0 violation sur 13 pages, clair et sombre (affichage clair forcé) | qa-accessibilite-axe.json |
| Affichage | 60 combinaisons (15 pages × 4 appareils) sans débordement ni erreur | qa-responsive.json |
| Hors ligne | service worker prêt, page et images chargées sans réseau | test-hors-ligne.json |
| Studio et évaluations | 0 erreur | test-studio.json, test-evaluations.json |

## Ajouts de cette passe
Fiche individuelle de parcours et mention accessibilité handicap (exigences du programme), module 8 complété (INRS S33 à S35), source S36 (arrêté du 9 juillet 2013), 46 questions, mode clair forcé, tableaux accessibles au clavier.

## Ce qui reste hors de portée de cette session
- NF C 18-510 (norme payante) non lue : périmètre exact BS/BR/BE, remplacement et installation d'appareil (modules 21, 22) à confirmer par le formateur.
- Relecture technique par un formateur habilité : modules 9, 12 à 17, 19 à 23, schémas, images IA, grilles pratiques, documents de session.
- Études de cas d'accidents (module 23) à comparer à l'ED 325 ; le ratio de cinq fois plus de questions que posées (ED 6127) n'est pas atteint par niveau.
- Arbres de décision détaillés de remplacement (lampe, fusible, prise) et vidéos non produits ; équipement de réalité virtuelle non couvert.
