def somme_valeurs_paires(liste):
    valeurs_paires = [nombre for nombre in liste if nombre % 2 == 0]
    somme = sum(valeurs_paires)
    return somme

L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]

somme_des_paires = somme_valeurs_paires(L)

print("Somme des valeurs paires dans la liste :", somme_des_paires)
