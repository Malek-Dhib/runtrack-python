def distance_to_toilettes(nombre_marches, hauteur_marche_cm):
    nombre_jours_semaine = 7
    nombre_descendre_remontee_par_jour = 2
    hauteur_marche_m = hauteur_marche_cm / 100  

    distance_par_descendre_remontee = 2 * nombre_marches * hauteur_marche_m * nombre_descendre_remontee_par_jour
    distance_par_jour = distance_par_descendre_remontee * nombre_jours_semaine

    return distance_par_jour

nombre_marches = 190
hauteur_marche_cm = 20

distance_par_semaine = distance_to_toilettes(nombre_marches, hauteur_marche_cm)
print(f"Pour {nombre_marches} marches de {hauteur_marche_cm} cm, le gardien parcourt {distance_par_semaine:.2f} m par semaine.")
