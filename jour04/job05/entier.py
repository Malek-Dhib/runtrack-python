def remplacer_element_par_somme(liste, index):
    if 0 < index < len(liste) - 1:
        somme_voisins = liste[index - 1] + liste[index + 1]
        liste[index] = somme_voisins

L = [1, 2, 3, 4, 5]

print("Liste initiale :", L)

deuxieme_valeur = L[1]
print("Deuxième valeur de la liste :", deuxieme_valeur)

remplacer_element_par_somme(L, 3)
print("Liste après remplacement :", L)

derniere_valeur = L[-1]
print("Dernière valeur de la liste :", derniere_valeur)
