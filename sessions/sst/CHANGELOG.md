# Journal des changements
## v0.7.11 — 15/11/2026
- Page Grilles de certification : le lien file:// vers le dossier des grilles ne s'ouvrant pas (bloqué par le navigateur, confirmé en usage réel), remplacé par un bouton « Copier le chemin du dossier » qui copie le chemin dans le presse-papier (testé fonctionnel).
## v0.7.10 — 15/11/2026
- Page Grilles de certification : bouton « Ouvrir le dossier des grilles » (lien local vers le dossier de la session sur le poste du formateur) avec le chemin affiché en clair en repli si le navigateur bloque les liens file://.
## v0.7.9 — 15/11/2026
- Correction : le bandeau de pied de page de toutes les pages (41) affichait encore « v0.3 du 14/11/2026 » alors que le site avait déjà reçu plusieurs mises à jour. Mis à jour en « v0.7.8 du 15/11/2026 ».
## v0.7.8 — 15/11/2026
- Correction : les pages apprenant (accueil, parcours, suivre, fiches secourir, valider mes acquis, galerie, glossaire, plans, ressources, modules 1 à 8, crédits) ne proposaient aucun lien vers l'espace formateur ni vers l'animation. Un lien « Espace formateur » (accès protégé par code) est ajouté dans la navigation de ces 20 pages.
## v0.7.7 — 15/11/2026
- Audit red team (41 pages × 3 formats : mobile 375, tablette 768, bureau 1366) : aucune erreur console, aucun lien ou image cassé, aucun défilement horizontal. Correction : la porte d'accès des pages formateur ajoutait un second titre de niveau 1 (21 pages) ; elle utilise désormais un titre de niveau 2.
## v0.7.6 — 15/11/2026
- Page Grilles de certification : encart « Mes grilles de la session » (marche à suivre, aucune donnée de stagiaire publiée) et lien vers les grilles INRS vierges.
## v0.7.5 — 15/11/2026
- Les deux formats de livrets sont proposés : longs (apprenant 93 p., formateur 137 p.) et compacts (apprenant 39 p., formateur 56 p.), documents.html les relie tous ; les deux livrets formateur sont protégés par le même mot de passe.
- Visuel des neuf principes : pastilles 1, 2, 3, 5 et 7 rétablies (numérotation 1 à 9 complète, article L4121-2 du Code du travail) sur le site et dans les livrets.
## v0.7.4 — 15/11/2026
- Décision : conservation des livrets longs (apprenant 93 pages, formateur 137 pages) conformément à la demande ; les versions compactes (39 et 56 pages) de la v0.7.3 restent consultables dans l'historique (commit f1ae58c). Correctif de contraste du mode nuit conservé. Livret formateur protégé par un nouveau mot de passe.
## v0.7.3 — 15/11/2026
- Mode nuit corrigé : variables de couleur, titres, liens, encarts et livret formateur redéfinis ; contrôle automatique du contraste WCAG AA sur toutes les pages (nuit et jour, mobile) : 187 défauts avant, 0 après, y compris animation et espace formateur déverrouillés.
- Livrets PDF refaits en mise en page éditoriale A4 : couverture, sommaire paginé, bandeaux de module, schémas plafonnés, encarts non coupés, questions en deux colonnes, cadres « Mes notes » ajustés au vide restant, corrigés regroupés. Livret apprenant 39 pages (3,7 Mo), livret formateur 56 pages (3 Mo), contre 93 et 137 pages (43 et 37 Mo) : plus de pages quasi vides ni de texte coupé. Le livret formateur reste protégé (copie et modification interdites).
## v0.7.1 — 15/11/2026
- Mode jour / nuit : bouton flottant sur toutes les pages, choix mémorisé, suit le réglage du système par défaut ; fonds des encarts, tableaux et schémas adaptés au mode nuit ; l'impression reste en mode jour.
- Livrets complets : livret de formation apprenant (93 pages, avec sommaire paginé : démarche, parcours, 8 compétences, fiches secourir, scénarios, validation, plans, glossaire, ressources, sources, aide-mémoire) et livret formateur (137 pages : synthèse, espace formateur, 4 demi-journées, séquences, animation complète, scénarios, pédagogie, matériel, matrice, certification, FAQ, suivi, validation, fiches, plans, glossaire, sources).
## v0.7.0 — 14/11/2026
- Diaporama dans la partie animation : choix des diapositives par demi-journée, bloc ou diapositive, lancement plein écran, clavier, plan, mémorisation locale du choix.
- Mise en page optimisée (site, animation, livrets) : espaces mieux occupés, grilles texte/visuels, impression ajustée.
- Livret formateur (page + PDF) ; livret apprenant refondu.
- Accès formateur : code ou l'une des deux adresses e-mail autorisées.
- Déroulé strictement respecté : J1 matin C1-C6-C7-C8 ; J1 après-midi C2, C3 + introduction C4 ; J2 matin réactivation puis reprise C4 et début C5 (saignements, étouffement) ; J2 après-midi suite C5 (PLS, malaise, brûlure, plaies × traumatismes, RCP/DAE).
## v0.6.0 — 14/11/2026
- Animation complète : déroulé animé des 4 demi-journées, dans l'ordre des blocs du parcours (15 blocs, 25 étapes de projection avec les fiches secourir découpées par situation).
- Pour chaque bloc : objectifs, réflexe, schémas commentés, essentiel, pièges, mise en situation, question flash, note formateur ; fiches secourir intégrées au bon moment (matin 2 : saignement, étouffement ; après-midi 2 : PLS, malaise, brûlure, plaie, douleur, RCP et DAE).
- Repères et renvois par bloc : module apprenant (avec bandeau d'étape), fiche de séquence, déroulé formateur, fiches outils INRS, plans PI et PAP, glossaire, auto-évaluation, QR code de suivi.
- Mode présentation (une étape à la fois, adresse partageable #j2a-b4) ou « Tout afficher » ; sans JavaScript, tout est affiché. Scènes animées A (protéger à secourir) et B (alerter, masser, défibriller) conservées dans les blocs concernés.
- Ancres ajoutées : fiches de séquence (sq-C1 à sq-C8), « Suivre la formation » par demi-journée.
## v0.3.1 — 14/11/2026
- Images IA V2 (gilet vert pour le sauveteur) : 31 visuels remplacés ; 24 affichés, 7 en attente de validation d'un formateur SST (PLS, claques, compressions abdominales, nourrisson, RCP, DAE, insufflations).
- Scénarios F1–F4 et K1–K4 réécrits pour correspondre aux 8 scènes illustrées ; chaque scène est affichée dans sa fiche.
## v0.3 — 14/11/2026
- Refonte : parcours, 8 modules apprenants, glossaire, galerie, ressources, crédits, livret imprimable et PDF, registre des sources, relecture des visuels, mode hors ligne.
- 9 schémas originaux Consulteam ; 31 images générées par IA intégrées (13 affichées, 18 en attente de validation).
- 5 questions ajoutées pour couvrir les sous-compétences 2.1, 3.2, 5.1, 5.3 et 8.3 (32 questions, toutes sous-compétences couvertes).
- Menu apprenant sans lien « Espace formateur ».
## v0.2 — module initial
- Déroulé, fiches secourir, validation, scénarios, MAC, suivi, matrice (voir historique git).

## v0.3.2 — 14/11/2026
- Correction MAC selon la grille officielle INRS de juillet 2023 : épreuve 2 = C6, C7, C8 ; 7 compétences ; C1 absente de la grille MAC.
- Nouvelle page formateur certification.html (indicateurs reformulés, incontournables, conditions d’acquisition, initiale juin 2020 et MAC juillet 2023).
- Registre R05 et sources mis à jour avec les grilles.

## v0.3.3 — 14/11/2026
- Exploitation des ressources INRS : nouvelle page apprenant outils.html (PAP, ITAMaMi, Carsat, DAE, garrot, trousse, origine des gestes, responsabilité, malaises mortels, organisation des secours, repères historiques) et page formateur pedagogie.html.
- Bloc « Pour aller plus loin » dans chaque module ; registre R24 à R27.
- Garrot, DAE et trousse recoupés avec le Guide V5.01 : pas d’écart.

## v0.4.0 — 14/11/2026
- Plans INRS PAP et PI dématérialisés intégrés sans modification (outils-inrs/, page formateur plans.html), avec l’autorisation du responsable. Dépôt public.
- Les 7 visuels en attente sont validés par Benoît Deflandre (data/visuels-statut.csv).
- Aucun tarif Carsat repris de la fiche 2015 ; la revue HST (do36) est laissée de côté.

## v0.5.0 — 14/11/2026
- Accès à l’espace formateur et à l’animation par code ou adresse e-mail (contrôle côté navigateur, empreintes SHA-256 ; limite l’affichage, ne protège pas les fichiers).
- Animations (protéger–examiner–alerter–secourir ; alerter–masser–défibriller) avec QR code « Sur le site » et repères à chaque étape.
- Page « Suivre la formation » avec QR codes par séquence et par demi-journée (23 QR, décodage vérifié).
- Parcours : vignettes de demi-journée actives, étapes numérotées dans l’ordre, bandeau « étape n sur N » dans les modules.
- Modules enrichis : réflexe, pièges fréquents, question flash, icônes, explications « Comment lire » sous les schémas.
- Espace formateur : fiches de séquence, matériel et salle, modèles de documents, questions du formateur.
- Plans PI et PAP intégrés dans la page Plans (iframes) et liés depuis les modules.
