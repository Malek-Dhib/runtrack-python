def time_to_text(minutes):
    if isinstance(minutes, int) and minutes >= 0:
        heures = minutes // 60
        minutes_restantes = minutes % 60

        if heures == 0:
            print(f"{minutes} minutes")
        elif heures == 1:
            print(f"{heures} heure et {minutes_restantes} minutes")
        else:
            print(f"{heures} heures et {minutes_restantes} minutes")
    else:
        print("Le nombre de minutes n'est pas un entier positif.")

time_to_text(120)
time_to_text(75)
time_to_text(45)
time_to_text(0)
time_to_text(-10)
time_to_text(90.5)

