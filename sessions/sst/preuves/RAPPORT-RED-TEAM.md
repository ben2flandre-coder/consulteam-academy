# Rapport Red Team — SST Consulteam v0.3 (14/11/2026)
Contrôles exécutés : rendu 1280 et 390 px (0 débordement, 0 erreur console), 717 liens internes (0 cassé), axe-core WCAG 2.1 AA et bonnes pratiques sur 31 pages (0 violation), hors ligne (service worker actif, module et images chargés), quiz (32 questions, bonne et mauvaise réponse détectées), matrice objectifs-questions (aucune sous-compétence sans question), recherche de termes interdits sur les pages apprenant (aucun GRETA, FIPAN, FORPRO, ac-nice, RMBD, Qualiopi, NDA).

## Écarts ouverts (à traiter ou arbitrer)
1. **Relecture indépendante non faite** : elle revient à B. Deflandre. Aucun second passage sans connaissance de la production n'a eu lieu.
2. **Visuels IA à valider (10 gestes ou schémas)** : s7-pls, s8-dae-etapes, s8-rcp-compressions, s8-insufflations, s2 (claques, abdominales, nourrisson), s3-malaise-repos (tasse), itamami-5-axes, quatre-familles-dangers. Non affichés aux apprenants. Observations dans `visuels-relecture.html`.
3. **Scènes F et K (8 images)** : elles ne correspondent pas aux scénarios F1-F4 et K1-K4 écrits sur le site (contextes et victimes différents). Rattachement à décider ; présentées à part dans `scenarios.html`.
4. **Croix blanches sur trousses vertes** dans plusieurs images : signe générique, aucun logo identifié ; à confirmer au regard de la charte.
5. **Images reprises de la session a260bga** : mention « générée par IA » à confirmer.
6. **Version du référentiel** : Document de référence V8 01/2021 (version plus récente possible) ; Guide V5.01/2024 retenu ; aide-mémoire ED 4085 de mai 2026 signalé, non lu, il annonce un alignement sur le dernier guide sans en donner le numéro.
7. **Textes de loi** (223-6, R4224-15, L411-1) cités d'après les documents INRS, non relus sur Légifrance dans cet outil ; L4121-2 vérifié par le contrôle documentaire livré avec les images.
8. **Titre « Manuel du formateur »** cité comme source dans des pages apprenant (titre de document).
9. **Pas de verrou d'accès** à l'espace formateur : séparation par pages, non lié, noindex.
10. **Cockpit** : cockpit-activite.json introuvable sur le poste ; aucune fiche mission créée ni événement d'agenda.
11. **Métadonnées** : WebP convertis sans EXIF ; PDF produit par Chromium (Producer Skia/PDF, sans auteur) ; auteur des PNG d'origine non contrôlé.
12. **Plan d'intervention, PAP et plan d'apparition du dommage** numériques : à intégrer quand fournis.
