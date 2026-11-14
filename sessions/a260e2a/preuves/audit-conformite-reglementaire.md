# Audit de conformité réglementaire — A260E2A (14/11/2026)

Affirmations réglementaires structurantes de la plateforme, avec la source lue et le niveau de vérification. Un contrôle exhaustif de la norme NF C 18-510 est impossible ici : norme payante non lue.

| Affirmation | Texte de référence | Source du registre | Statut | Module |
|---|---|---|---|---|
| Voisinage : 3 m jusqu'à 50 kV (BT comprise) | Arrêté du 9 juillet 2013, art. 2 | S36 (OPPBTP) + ED 6127 fig. 8.1.1 | VÉRIFIÉ | Module 18 |
| Zone 4 (voisinage renforcé BT) limitée à 0,30 m ; DLVR confondue avec DMA en BT | ED 6127 annexe 8.1.1 | S29, figure vue visuellement | VÉRIFIÉ | Module 18 |
| Symboles autorisés par zone (zones 0 à 4) ; B0 non admis en zone 4 | ED 6127 annexe 8.1.1 (tableau) | S29, tableau vu visuellement | VÉRIFIÉ | Modules 4, 18 |
| BS : 400 V et 32 A en alternatif, hors tension, sans voisinage renforcé | ED 6127 (2020) | S29, S38 | VÉRIFIÉ : ED 6127 (référentiel INRS) et diaporama INRS concordants ; seuils CC (600 V, 16 A) et sans exécutant confirmés par S38 | Module 5, 21 |
| BR : 500 V et 63 A en alternatif, connexion/déconnexion hors charge ; consignation pour son propre compte | ED 6127 (2020) | S29, S38 | VÉRIFIÉ : ED 6127 (500 V, 63 A, hors charge) et diaporama INRS (500 V alternatif, 750 V continu, 63 A alternatif, 32 A continu) concordants ; version 2012 à 1000 V : ancienne | Module 10 |
| Section BS (6 mm² Cu / 10 mm² Al), 600 V CC, 16 A CC | FAQ INRS | S37, S38 | VÉRIFIÉ : FAQ INRS (6 mm² cuivre, 10 mm² aluminium) et diaporama INRS (600 V continu, 16 A continu) | Module 5 |
| Programme de formation par symbole, durées pratiques minimales | ED 6127 §5 | S29 | VÉRIFIÉ à l'ED 6127 | Modules 9, 12 à 15, 16 |
| Avis après formation (contenu minimal) ; titre délivré par l'employeur | ED 6127 §7.2 + programme commandé | S29 | VÉRIFIÉ | Documents |
| Conduite à tenir en cas d'accident : trois actions, protéger, brûlures, dégagement d'urgence | INRS SST | S31, S33, S34, S35 | VÉRIFIÉ | Module 8 |
| Pas d'obligation de former les habilités au SST ; double compétence recommandée | Code du travail R. 4224-15/16 via INRS TS876 | S34 | VÉRIFIÉ (réponse INRS indicative) ; articles non relus | Module 8 |
| Études de cas d'accidents | INRS ED 325 | S32 | VÉRIFIÉ pour l'édition et les thèmes (fetch du PDF INRS : 26 cas, dont fusible en charge, mesure avec appareil en mauvais état, éclairage provisoire en local mouillé, toiture près d'une ligne, nettoyage de poste HT, personnel non qualifié)  ; chaque récit du module 23 comparé au texte et corrigé le 14/11/2026 | Module 23 |
| Réserve de 20 % de modules libres en tableau de logement | NF C 15-100 | S14, S40 | VÉRIFIÉ : trois sources concordantes (Eduscol, Promotelec, Legrand) ; norme elle-même non lue | Module 22 |
| Périmètre exact des opérations BR/BS/BE (remplacement, installation d'appareil) | NF C 18-510 compilée juin 2023 | S27, S37, S38, S39 | VÉRIFIÉ : CONFORME AU RÉFÉRENTIEL INRS (qui fait foi pour la formation) ; amendement A2 (juin 2023, applicable octobre 2024) précise les interventions sans seuil nouveau relevé ; texte payant non lu : relecture finale du formateur | Modules 21, 22 |
| Arrêté du 5 juillet 2024 (travaux d'ordre non électrique) et normes citées | Arrêté du 5 juillet 2024 | S26 | VÉRIFIÉ : texte publié au JO consulté en copie (distances 3 m / 5 m, visa de l'arrêté de 2013) | Registre |

Bilan : 14 vérifiés sans réserve, 0 avec réserve, 0 non vérifiables ici.

## Registre : limites déclarées par source

- S1 (lu) : La page ne mentionne pas le « remplacement d'un élément d'armoire » pour le BS. Elle ne définit pas le BC. NF C 18-510 non lue.
- S2 (lu) : Pas de courbes ni de valeurs de seuils ; temps de réaction donné seulement dans un extrait de FAQ.
- S3 (lu) : Ne mentionne ni le tore ni le mécanisme interne ni le temps de réaction. Cadre logement (NF C 15-100).
- S4 (extrait) : Extrait de recherche seulement ; copie hébergée sur un forum : remplacer par le document sur le site de Promotelec.
- S5 (lu) : Article de 1997 sur un produit précis ; ne parle pas de « spire de déphasage ».
- S6 (lu) : Affirme qu'un interrupteur différentiel coupe en cas de court-circuit ou de surcharge : non repris, contredit par S4.
- S7 (lu) : Renvoie à la NF C 15-100 pour le choix ; valeur de 3 kA citée pour le domestique, non reprise.
- S8 (lu) : Ne détaille ni le repérage des conducteurs, ni le serrage, ni la remise sous tension, ni les essais.
- S9 (lu) : Ne traite pas la vérification d'absence de tension. Cotes de dénudage propres au produit Legrand.
- S10 (extrait) : Extrait de recherche ; décrit un produit précis.
- S11 (extrait) : Extrait de recherche ; document à lire en entier pour la méthode de calcul.
- S12 (extrait) : Extrait de recherche ; contexte d'une étude de cas.
- S13 (relu le 14/11/2026 (réponse ciblée de l'outil de lecture)) : Formule donnée pour la tension ou le courant ; la page ne parle pas d'échauffement des connexions mais de connexions desserrées et de contacts usés.
- S14 (relu le 14/11/2026 (réponse ciblée de l'outil de lecture)) : Concerne les logements (NF C 15-100, édition de la fiche : 2018) ; la réserve peut être limitée à six modules par logement en immeuble collectif.
- S15 (extrait) : Citation de seconde main ; NF C 15-100 non lue.
- S16 (extrait) : Extrait de recherche ; source secondaire à confronter à la NF C 18-510 et au module 11.
- S17 (extrait) : Extrait de recherche.
- S18 (extrait) : Extrait de recherche ; à confirmer par une notice de constructeur.
- S19 (extrait) : Extrait de recherche ; contexte belge.
- S20 (extrait) : Extrait de recherche.
- S21 (extrait) : Extrait de recherche.
- S22 (lu) : NF C 18-510 non lue ; relecture indépendante non faite.
- S23 (lu) : Document non daté, non paginé ; état de la norme avant A1 et A2 non précisé ; ne donne pas de valeur pour la consignation.
- S24 (lu) : Ne mentionne pas l'amendement A1 ; date et auteur absents ; indique que les fusibles et disjoncteurs passent au BS (périmètre du BR à vérifier).
- S25 (extrait) : Extrait de recherche ; le détail de la mise à jour du BR n'est pas visible dans l'extrait.
- S26 (extrait) : Extrait de recherche ; l'extrait cite A1 mais pas A2 ; texte officiel à lire sur Légifrance.
- S27 (extrait) : Norme payante : le texte n'a pas été lu. Les limites de S23 et S24 restent à confirmer à ce texte.
- S28 (relu le 14/11/2026 (réponse ciblée de l'outil de lecture)) : La page ne donne aucune valeur de tension, d'intensité ou de section et ne mentionne aucun effet des amendements A1 ou A2 sur le BS ou le BR.
- S29 (lu (texte extrait du PDF de 52 pages)) : Antérieure à A2 (juin 2023) ; pas de section de conducteur dans la brochure ; renvoie à la NF C 18-510 pour la portée des symboles et les limitations.
- S30 (lu) : Édition remplacée, conservée pour tracer l'évolution ; ne pas enseigner à partir d'elle.
- S31 (lu (rubrique de secours)) : Ne distingue pas la basse et la haute tension dans les étapes de secours ; ne traite ni les brûlures ni le suivi médical ; les gestes détaillés du SST (ED 7000, guide des données techniques) n'ont pas été lus.
- S32 (lu par synthèse de page (outil de lecture), pas en lecture intégrale du PDF) : Édition confirmée le 14/11/2026 (2e édition 1993, réimpression août 2012, 26 cas : 13 contacts directs, 6 contacts indirects, 7 brûlures, incendies ou explosions) ; les thèmes de plusieurs cas du module 23 y figurent (fusible en charge, appareil de mesure en mauvais état, éclairage provisoire en local mouillé, toiture près d'une ligne, nettoyage d'un poste HT, personnel non qualifié) ; chaque récit du module 23 a été comparé au texte (cas 7, 11, 13, 15, 20, 23, 24, 26 de la brochure) et corrigé le 14/11/2026.
- S33 (lu (extraits : protéger, brûlures, défibrillation ; fichier du cloud SST fourni par Benoît le 14/11/2026)) : Lu par extraits ; le guide ne détaille pas la coupure d'une installation électrique, qui relève de l'habilitation.
- S34 (lu en entier (une page)) : Réponse indicative ; renvoie aux articles R. 4224-15 et R. 4224-16 du Code du travail, non relus ici.
- S35 (lu (extraits : protéger, brûlures)) : Aide-mémoire synthétique ; lu par extraits.
- S36 (lu (extrait de recherche, 14/11/2026) ; recoupé avec la figure de l'ED 6127 annexe 8.1.1 (page imprimée 40, vue visuellement)) : Extrait partiel de l'article ; l'annexe de l'arrêté (distances minimales d'approche par tension) n'a pas été relue en entier.
- S37 (lu (extraits de recherche, 14/11/2026)) : Extraits de recherche, page lue en partie.
- S38 (lu (extraits de recherche, 14/11/2026)) : Extraits ; peut précéder l'amendement A2 (juin 2023).
- S39 (lu (extraits de recherche, 14/11/2026)) : Texte de l'amendement non lu ; ne chiffre pas de nouveaux seuils pour BS et BR.
- S40 (lu (extraits de recherche, 14/11/2026)) : Règle de conception des logements ; norme NF C 15-100 non lue.