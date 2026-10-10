# Bonifay A2604QA — registre de production, 10 octobre 2026

## Mission

Documents Consul Team consultés dans Drive : ordre de mission A2604QA, CPS signé et DOCSESSION A2604QA. Session 12–13 octobre 2026, Bonifay La Garde, 6 participants. La liste porte B0 H0V, BS et BE Manœuvre ; le titre administratif « BE/HE BS » ne suffit pas à inclure HE Manœuvre. Aucune donnée nominative, coordonnées privées ou condition financière n'est publiée.

Durée annoncée 10,5 h ; les horaires reçus totalisent 10 h (08:30–12:00 / 13:30–16:30 le 12, 08:30–12:00 le 13). Écart signalé, sans inventer de créneau. Confirmation Consul Team nécessaire pour l'organisation réelle.

## Origine et périmètre

Le fichier `cours/base.html` est la copie byte à byte du cours DGA `sessions/a2604ma/cours/index.html`, au commit 385f9926493ec4a06a51d796167905935e6f1cc9. Le chargeur et `bonifay.js` adaptent la session, le suivi local, les cas métiers et le déroulé. Les ressources incorporées à la base sont conservées. Aucun fichier DGA, PMS ou autre session n'est modifié.

## Sources externes effectivement consultées

- [FAQ INRS habilitation](https://www.inrs.fr/risques/electriques/habilitation-electrique-foire-aux-questions) : limites BS, opérations admissibles, B0/H0/H0V, BE Manœuvre. Consultation 10/10/2026.
- [INRS habilitation électrique](https://www.inrs.fr/risques/electriques/habilitation-electrique.html) : formation, évaluation des savoirs et savoir-faire, rôle de l'employeur. Consultation 10/10/2026.
- [Arrêté du 9 juillet 2013](https://www.legifrance.gouv.fr/loda/id/JORFTEXT000027736209/) : dimensions du voisinage en champ libre. Consultation 10/10/2026.
- [MémoForma](https://memoforma.fr/) : référence de niveau éditorial demandée par l'utilisateur, aucune planche copiée et aucune affiliation.

NF C 18-510 et amendements applicables : référentiel visé, texte consolidé intégral non fourni à cette production. La vérification ciblée ci-dessus ne constitue pas une certification de conformité de l'ensemble du cours hérité. Les notices, le titre réel et les prescriptions du site complètent le support. Les vidéos héritées restent des ressources repérées : leur lecture intégrale et leur validation ne sont pas revendiquées.

## Corrections de l'évaluation, dans la copie Bonifay uniquement

- Q13 : « voisinage renforcé » BT pour le seuil 0,30 m, au lieu de « voisinage simple ».
- Q14 et Q28 : remplacement à l'identique / raccordement sur circuit en attente ; aucune autorisation générale de pose ou modification.
- Q30 : contexte précisé (manœuvre BT en local à risques particuliers) pour éviter de rendre toute commande normale soumise à BE Manœuvre.
- Q21 : outillage prescrit pour intervention BS, formulation contextualisée.
- Q25 : IP55 devient une exigence explicite du scénario, sans règle universelle pour toute prise extérieure.
- Q37 : réponse correcte 400 V CA (index 1).
- Q38 : 6 mm² cuivre admis, en plus des 1,5 et 2,5 mm² (indices 0,1,2).
- CSV : séparateur de lignes réel ; stockage séparé A2604QA.
- Résultat : seuil pédagogique interne, sans avis favorable automatique ni délivrance d'habilitation.

## Visuels nouveaux et prompts

- `bs-limites.svg`, `roles.svg`, `vat-controles.svg` : schémas originaux déterministes, texte contrôlé, source FAQ INRS. Ils sont génériques, sans inventaire supposé du site.
- `reperer.webp` : création avec l'outil intégré d'images. Prompt : illustration technique professionnelle, fond blanc, armoire fermée derrière balisage, travailleur à l'extérieur signalant une rallonge détériorée, sans manipulation, sans distances ni certifications inventées. Titre « REPÉRER AVANT D’AGIR ».
- `vat-dispositif.webp` : création avec l'outil intégré d'images. Prompt : dispositif VAT bipolaire générique avec deux sondes et câble, hors circuit, sans marque ni certification, séquence « Contrôler avant / Vérifier l’absence de tension / Contrôler après », selon notice.

Les illustrations générées ne désignent aucun modèle approuvé. Leur géométrie ne remplace pas une notice fabricant. Les planches de règles utilisent du texte vectoriel contrôlé pour éviter les erreurs de génération.
