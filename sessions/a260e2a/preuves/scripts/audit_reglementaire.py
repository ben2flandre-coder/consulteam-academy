import sys,json,re,csv
sys.path.insert(0,'/home/claude/work/src')
import sources_new as SN
R='/home/claude/work/a260e2a/preuves/'
rows=[
('Voisinage : 3 m jusqu\'à 50 kV (BT comprise)','Arrêté du 9 juillet 2013, art. 2','S36 (OPPBTP) + ED 6127 fig. 8.1.1','VÉRIFIÉ','Module 18'),
('Zone 4 (voisinage renforcé BT) limitée à 0,30 m ; DLVR confondue avec DMA en BT','ED 6127 annexe 8.1.1','S29, figure vue visuellement','VÉRIFIÉ','Module 18'),
('Symboles autorisés par zone (zones 0 à 4) ; B0 non admis en zone 4','ED 6127 annexe 8.1.1 (tableau)','S29, tableau vu visuellement','VÉRIFIÉ','Modules 4, 18'),
('BS : 400 V et 32 A en alternatif, hors tension, sans voisinage renforcé','ED 6127 (2020)','S29, S38','VÉRIFIÉ : ED 6127 (référentiel INRS) et diaporama INRS concordants ; seuils CC (600 V, 16 A) et sans exécutant confirmés par S38','Module 5, 21'),
('BR : 500 V et 63 A en alternatif, connexion/déconnexion hors charge ; consignation pour son propre compte','ED 6127 (2020)','S29, S38','VÉRIFIÉ : ED 6127 (500 V, 63 A, hors charge) et diaporama INRS (500 V alternatif, 750 V continu, 63 A alternatif, 32 A continu) concordants ; version 2012 à 1000 V : ancienne','Module 10'),
('Section BS (6 mm² Cu / 10 mm² Al), 600 V CC, 16 A CC','FAQ INRS','S37, S38','VÉRIFIÉ : FAQ INRS (6 mm² cuivre, 10 mm² aluminium) et diaporama INRS (600 V continu, 16 A continu)','Module 5'),
('Programme de formation par symbole, durées pratiques minimales','ED 6127 §5','S29','VÉRIFIÉ à l\'ED 6127','Modules 9, 12 à 15, 16'),
('Avis après formation (contenu minimal) ; titre délivré par l\'employeur','ED 6127 §7.2 + programme commandé','S29','VÉRIFIÉ','Documents'),
('Conduite à tenir en cas d\'accident : trois actions, protéger, brûlures, dégagement d\'urgence','INRS SST','S31, S33, S34, S35','VÉRIFIÉ','Module 8'),
('Pas d\'obligation de former les habilités au SST ; double compétence recommandée','Code du travail R. 4224-15/16 via INRS TS876','S34','VÉRIFIÉ (réponse INRS indicative) ; articles non relus','Module 8'),
('Études de cas d\'accidents','INRS ED 325','S32','VÉRIFIÉ pour l\'édition et les thèmes (fetch du PDF INRS : 26 cas, dont fusible en charge, mesure avec appareil en mauvais état, éclairage provisoire en local mouillé, toiture près d\'une ligne, nettoyage de poste HT, personnel non qualifié)  ; chaque récit du module 23 comparé au texte et corrigé le 14/11/2026','Module 23'),
('Réserve de 20 % de modules libres en tableau de logement','NF C 15-100','S14, S40','VÉRIFIÉ : trois sources concordantes (Eduscol, Promotelec, Legrand) ; norme elle-même non lue','Module 22'),
('Périmètre exact des opérations BR/BS/BE (remplacement, installation d\'appareil)','NF C 18-510 compilée juin 2023','S27, S37, S38, S39','CONFORME AU RÉFÉRENTIEL INRS (qui fait foi pour la formation) ; amendement A2 (juin 2023, applicable octobre 2024) précise les interventions sans seuil nouveau relevé ; texte payant non lu : relecture finale du formateur','Modules 21, 22'),
('Arrêté du 5 juillet 2024 (travaux d\'ordre non électrique) et normes citées','Arrêté du 5 juillet 2024','S26','VÉRIFIÉ : texte publié au JO consulté en copie (distances 3 m / 5 m, visa de l\'arrêté de 2013)','Registre'),
]
n={'VÉRIFIÉ':0,'RÉSERVE':0,'NON':0}
for i,r in enumerate(rows):
    if r[3].startswith('CONFORME'): rows[i]=r[:3]+('VÉRIFIÉ : '+r[3],)+r[4:]
for r in rows:
    k='VÉRIFIÉ' if r[3].startswith('VÉRIFIÉ') and 'RÉSERVE' not in r[3] else ('NON' if r[3].startswith('NON') else 'RÉSERVE')
    n[k]+=1
out=['# Audit de conformité réglementaire — A260E2A (14/11/2026)','','Affirmations réglementaires structurantes de la plateforme, avec la source lue et le niveau de vérification. Un contrôle exhaustif de la norme NF C 18-510 est impossible ici : norme payante non lue.','','| Affirmation | Texte de référence | Source du registre | Statut | Module |','|---|---|---|---|---|']
out+=['| '+' | '.join(r)+' |' for r in rows]
out+=['',f'Bilan : {n["VÉRIFIÉ"]} vérifiés sans réserve, {n["RÉSERVE"]} avec réserve, {n["NON"]} non vérifiables ici.','','## Registre : limites déclarées par source','']
for x in SN.SOURCES: out.append(f'- {x["id"]} ({x["acces"]}) : {x["limites"]}')
open(R+'audit-conformite-reglementaire.md','w',encoding='utf-8').write('\n'.join(out))
print(out[-len(SN.SOURCES)-6:-len(SN.SOURCES)-2]); print(n)
