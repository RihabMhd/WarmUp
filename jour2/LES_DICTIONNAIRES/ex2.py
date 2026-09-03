produit = {
    "nom": "Ordinateur", "prix": 8500,
    "stock": 12, "categorie": 
"Informatique"
}

produit["prix"]=7900

produit["marque"]="lenovo"
produit["disponible"]=True

del produit['stock']
produit.pop('categorie')

print(produit)