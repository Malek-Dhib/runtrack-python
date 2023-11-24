def arrondir_notes(liste_notes):
    notes_arrondies = []
    for note in liste_notes:
        if note < 40:
            notes_arrondies.append(note)
        else:
            multiple_de_5_superieur = ((note // 5) + 1) * 5
            if multiple_de_5_superieur - note < 3:
                notes_arrondies.append(multiple_de_5_superieur)
            else:
                notes_arrondies.append(note)
    return notes_arrondies

liste_notes = [37, 42, 83, 78, 92, 65, 57, 97, 43, 48, 33, 38, 88]
notes_arrondies = arrondir_notes(liste_notes)
print("Liste des notes arrondies :", notes_arrondies)
