def afficher_produits(type, saison):
    if type == "fruits":
        if saison == "hiver":
            print("Orange, mandarine et kiwi")
        elif saison == "ete":
            print("Poire, fraise, cassis")
        else:
            print("Saison non prise en charge")
    elif type == "legume":
        if saison == "hiver":
            print("Carotte, topinambour, endive")
        elif saison == "ete":
            print("Artichaut, aubergine, navet")
        else:
            print("Saison non prise en charge")
    else:
        print("Type non pris en charge")

afficher_produits("fruits", "hiver")
afficher_produits("fruits", "ete")
afficher_produits("legume", "hiver")
afficher_produits("legume", "ete")
