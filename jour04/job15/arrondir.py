ma_liste = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

ma_liste_arrondie = [int(nombre + 0.5) for nombre in ma_liste]

print("Liste arrondie :", ma_liste_arrondie)

def bubble_sort(liste):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(liste) - 1):
            if liste[i] > liste[i + 1]:
                liste[i], liste[i + 1] = liste[i + 1], liste[i]
                swapped = True

bubble_sort(ma_liste_arrondie)

ma_liste_triee = []
while ma_liste_arrondie:
    minimum = ma_liste_arrondie.pop(0)
    ma_liste_triee.append(minimum)

print("Liste triée en ordre croissant :", ma_liste_triee)
