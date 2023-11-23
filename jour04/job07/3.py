def compter_multiples_de_trois(liste):
    multiples_de_trois = [nombre for nombre in liste if nombre % 3 == 0]
    nombre_de_multiples_de_trois = len(multiples_de_trois)
    return nombre_de_multiples_de_trois

L = [8, 24, 48, 2, 16]

nombre_de_multiples = compter_multiples_de_trois(L)

print("Nombre de multiples de 3 dans la liste :", nombre_de_multiples)
