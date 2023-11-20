nom_produit = "Switch"
prix_unitaire = 300
quantite_en_stock = 25

print("Produit:", nom_produit)
print("Prix unitaire:", prix_unitaire)
print("Quantité en stock:", quantite_en_stock)
print()

quantite_achat = int(input("Combien d'unités souhaitez-vous acheter ? "))

quantite_en_stock -= quantite_achat

prix_unitaire *= 1.1  

# Afficher à nouveau les informations du produit après la mise à jour
print("\nAprès l'achat et l'inflation :")
print("Produit:", nom_produit)
print("Nouveau prix unitaire après inflation :", prix_unitaire)
print("Nouvelle quantité en stock après achat :", quantite_en_stock)
