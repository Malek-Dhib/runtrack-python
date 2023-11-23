def trier_liste_croissante(liste):
    longueur = 0
    for _ in liste:
        longueur += 1

    for i in range(longueur):
        for j in range(0, longueur - i - 1):
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]

ma_liste = [7, 11, 42, 39, 2]

print("Liste initiale :", ma_liste)

trier_liste_croissante(ma_liste)

print("Liste triée dans l'ordre croissant :", ma_liste)
