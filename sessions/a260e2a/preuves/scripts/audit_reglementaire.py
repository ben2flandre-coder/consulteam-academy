import sys,json,re,csv
sys.path.insert(0,'/home/claude/work/src')
import sources_new as SN
R='/home/claude/work/a260e2a/preuves/'
rows=[
('Voisinage : 3 m jusqu\'à 50 kV (BT comprise)','Arrêté du 9 juillet 2013, art. 2','S36 (OPPBTP) + ED 6127 fig. 8.1.1','VÉRIFIÉ','Module 18'),
('Zone 4 (voisinage renforcé BT) limitée à 0,30 m ; DLVR confondue avec DMA en BT','ED 6127 annexe 8.1.1','S29, figure vue visuellement','VÉRIFIÉ','Module 18'),
('Symboles autorisés par zone (zones 0 à 4) ; B0 non admis en zone 4','ED 6127 annexe 8.1.1 (tableau)','S29, tableau vu visuellement','VÉRIFIÉ','Modules 4, 18'),
('BS : 400 V et 32 A en alternatif, hors tension, sans voisinage renforcé','ED 6127 (2020)','S29','VÉRIFIÉ à l\'ED 6127 ; RÉSERVE : NF C 18-510 (2023) non lue','Module 5, 21'),
('BR : 500 V et 63 A en alternatif, connexion/déconnexion hors charge ; consignation pour son propre compte','ED 6127 (2020)','S29','VÉRIFIÉ à l\'ED 6127 ; RÉSERVE : NF C 18-510 (2023) non lue ; écart avec la version 2012 (1000 V) noté','Module 10'),
('Section BS (6 mm² Cu / 10 mm² Al), 600 V CC, 16 A CC','FAQ INRS','S28','RÉSERVE : source secondaire, brochure silencieuse sur la section','Module 5'),
('Programme de formation par symbole, durées pratiques minimales','ED 6127 §5','S29','VÉRIFIÉ à l\'ED 6127','Modules 9, 12 à 15, 16'),
('Avis après formation (contenu minimal) ; titre délivré par l\'employeur','ED 6127 §7.2 + programme commandé','S29','VÉRIFIÉ','Documents'),
('Conduite à tenir en cas d\'accident : trois actions, protéger, brûlures, dégagement d\'urgence','INRS SST','S31, S33, S34, S35','VÉRIFIÉ','Module 8'),
('Pas d\'obligation de former les habilités au SST ; double compétence recommandée','Code du travail R. 4224-15/16 via INRS TS876','S34','VÉRIFIÉ (réponse INRS indicative) ; articles non relus','Module 8'),
('Études de cas d\'accidents','INRS ED 325','S32','RÉSERVE : lu par synthèse de page, à comparer à la brochure','Module 23'),
('Réserve de 20 % de modules libres en tableau de logement','NF C 15-100','S14','RÉSERVE : source secondaire, norme non lue','Module 22'),
('Périmètre exact des opérations BR/BS/BE (remplacement, installation d\'appareil)','NF C 18-510 compilée juin 2023','S27','NON VÉRIFIABLE ICI : norme payante non lue ; à confirmer par le formateur','Modules 21, 22'),
('Arrêté du 5 juillet 2024 (travaux d\'ordre non électrique) et normes citées','Arrêté du 5 juillet 2024','S26','RÉSERVE : extrait de recherche ; texte officiel à lire sur Légifrance','Registre'),
]
n={'VÉRIFIÉ':0,'RÉSERVE':0,'NON':0}
for r in rows:
    k='VÉRIFIÉ' if r[3].startswith('VÉRIFIÉ') and 'RÉSERVE' not in r[3] else ('NON' if r[3].startswith('NON') else 'RÉSERVE')
    n[k]+=1
out=['# Audit de conformité réglementaire — A260E2A (14/11/2026)','','Affirmations réglementaires structurantes de la plateforme, avec la source lue et le niveau de vérification. Un contrôle exhaustif de la norme NF C 18-510 est impossible ici : norme payante non lue.','','| Affirmation | Texte de référence | Source du registre | Statut | Module |','|---|---|---|---|---|']
out+=['| '+' | '.join(r)+' |' for r in rows]
out+=['',f'Bilan : {n["VÉRIFIÉ"]} vérifiés sans réserve, {n["RÉSERVE"]} avec réserve, {n["NON"]} non vérifiables ici.','','## Registre : limites déclarées par source','']
for x in SN.SOURCES: out.append(f'- {x["id"]} ({x["acces"]}) : {x["limites"]}')
open(R+'audit-conformite-reglementaire.md','w',encoding='utf-8').write('\n'.join(out))
print(out[-len(SN.SOURCES)-6:-len(SN.SOURCES)-2]); print(n)
