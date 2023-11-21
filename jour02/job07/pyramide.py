chaine = "abcdefghijklmnopqrstuvwxyz" * 10

i = 1
while i <= len(chaine):
    ligne = chaine[:i]
    print(ligne, end="\n")  
    i += 2
