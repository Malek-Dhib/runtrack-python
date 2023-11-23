def est_mot_plus_long(mot, longueur):
    longueur_mot = 0
    for caractere in mot:
        longueur_mot += 1
    return longueur_mot > longueur

def my_long_word(longueur, phrase):
    mots = phrase.split()
    mots_plus_longs = [mot for mot in mots if est_mot_plus_long(mot, longueur)]
    resultat = " ".join(mots_plus_longs)
    return resultat

resultat = my_long_word(4, "de ce que l'on sait, laplateforme est là pour aider à s'améliorer en programmation, ainsi de coder via différentes plateformes comme python.")
print("Output :", resultat)
