import cmath, math, itertools, json
# Exemple FICTIF : 8 circuits monophasés (phase-neutre), charges résistives (cos φ = 1), courants d'emploi donnés (A)
circuits = [("C1",16),("C2",16),("C3",10),("C4",10),("C5",8),("C6",6),("C7",6),("C8",4)]
avant = {"C1":"L1","C2":"L1","C3":"L1","C4":"L2","C5":"L2","C6":"L3","C7":"L3","C8":"L3"}
rot = {"L1":1, "L2":cmath.exp(-2j*math.pi/3), "L3":cmath.exp(2j*math.pi/3)}
def bilan(aff):
    I={p:sum(a for n,a in circuits if aff[n]==p) for p in("L1","L2","L3")}
    N=sum(I[p]*rot[p] for p in I)
    moy=sum(I.values())/3
    desq=max(abs(I[p]-moy) for p in I)/moy*100        # formule S13 : écart max / moyenne x 100
    return I,abs(N),moy,desq
# méthode : plus gros circuit d'abord sur la phase la moins chargée
aff={}; cur={"L1":0,"L2":0,"L3":0}
for n,a in sorted(circuits,key=lambda x:-x[1]):
    p=min(cur,key=lambda k:cur[k]); aff[n]=p; cur[p]+=a
apres=aff
# optimum par énumération exhaustive (3^8 = 6561 affectations)
best=None
for combo in itertools.product(("L1","L2","L3"),repeat=len(circuits)):
    af={n:p for (n,_),p in zip(circuits,combo)}
    I,N,moy,d=bilan(af)
    key=(max(I.values())-min(I.values()),N)
    if best is None or key<best[0]: best=(key,af,I,N,d)
out={}
for nom,af in(("avant",avant),("apres_methode",apres),("optimum_enumeration",best[1])):
    I,N,moy,d=bilan(af)
    out[nom]=dict(affectation=af,courants_par_phase=I,courant_neutre_A=round(N,2),moyenne_A=round(moy,2),desequilibre_pct=round(d,1))
out["nb_affectations_testees"]=3**len(circuits)
out["hypotheses"]="charges résistives, cos φ = 1, circuits monophasés phase-neutre, courants d'emploi fictifs ; pas d'harmoniques ; ordre des phases L1,L2,L3 à 120°"
# preuve complémentaire : 3 courants égaux -> neutre nul
I,N,_,_=bilan({n:"L1" for n,_ in circuits}); out["tout_sur_L1"]=dict(courant_neutre_A=round(N,2),total_A=sum(a for _,a in circuits))
eq=abs(10*rot["L1"]+10*rot["L2"]+10*rot["L3"]); out["trois_courants_egaux_10A_neutre_A"]=round(eq,6)
json.dump(out,open("/home/claude/work/a260e2a/preuves/calcul-equilibrage.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print(json.dumps(out,ensure_ascii=False,indent=1))
