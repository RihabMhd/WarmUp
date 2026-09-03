from functools import reduce

ventes = [
    {"produit": "PC", "categorie": "Informatique", "prix": 8000, "quantite": 2},
    {"produit": "Souris", "categorie": "Accessoire", "prix": 150, "quantite": 10},
    {"produit": "Clavier", "categorie": "Accessoire", "prix": 300, "quantite": 5},
    {"produit": "PC", "categorie": "Informatique", "prix": 8000, "quantite": 1},
    {"produit": "Écran", "categorie": "Informatique", "prix": 2500, "quantite": 3}
]

nombre_vente=len(ventes)
ca=0
for v in ventes:
    ca=ca+v['prix']*v['quantite']

print(ca)

max=ventes[0]["prix"]
prd_cher=[x for x in ventes if x["prix"]>=max]
print(prd_cher)
quantites=list(map(lambda x:x["quantite"],ventes))
quantite=reduce(lambda x,y:x+y,quantites)
print(quantite)

for v in ventes:
    print(v['categorie'],";",v['prix']*v['quantite'])
print("----------------------------------------------------------")
quantites={}
for i in range(len(ventes)):
    if ventes[i]['categorie'] not in quantites:
        quantites[ventes[i]['categorie']]=1
    else:
        quantites[ventes[i]['categorie']]=quantites[ventes[i]['categorie']]+1
    

print(quantites)