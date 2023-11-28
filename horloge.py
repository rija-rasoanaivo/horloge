import time

heure = (23, 59, 55)
alarme = (23, 59, 58)

def afficher_heure(heure):
    heure_liste = list(heure)
    heures, minutes, secondes = heure_liste
    while True:
        if 0 <= secondes < 60 and 0 <= minutes < 60 and 0 <= heures < 24:
            secondes = (secondes + 1) % 60
            if secondes == 0:
                minutes = (minutes + 1) % 60
                if minutes == 0:
                    heures = (heures + 1) % 24

        time.sleep(1)
        regler_alarme(alarme, (heures, minutes, secondes))
        am_pm(heures, minutes, secondes, format_choisi)
format_choisi = input("Choisissez le format (24h ou am/pm): ")


def regler_alarme(alarme, heure):
    if heure == alarme:
        print("C'est l'heure :) :) :) :)")


def am_pm(heures, minutes, secondes, format_choisi):
    if format_choisi.lower() == "24h":
        print(f"{heures:02d}:{minutes:02d}:{secondes:02d}")
    elif format_choisi.lower() == "am/pm":
        suffixe = "AM"
        if heures >= 12:
            suffixe = 'PM'
        if heures > 12:
            heures -= 12
        elif heures == 0:
            heures = 12

        print(f'{heures:02d}:{minutes:02d}:{secondes:02d} {suffixe}')
    else:
        print("Format non reconnu. Veuillez choisir entre '24h' ou 'am/pm'.")


afficher_heure(heure)