import time

heure = (23, 59, 55)
alarme = (23, 59, 57)

def afficher_heure(heure):
    heure_liste = list(heure)
    heures, minutes, secondes = heure_liste
    while True:
        if 0<=secondes<60 and 0<=minutes<60 and 0<=heures<24:
            secondes = (secondes + 1) % 60
            if secondes == 0:
                minutes = (minutes + 1) % 60
                if minutes == 0:
                    heures = (heures + 1) % 24

        time.sleep(1)
        regler_alarme(alarme, (heures, minutes, secondes))            
        print(f"{heures:02d}:{minutes:02d}:{secondes:02d}")


def regler_alarme(alarme, heure):
    if heure == alarme:
        print("C'est l'heure")

afficher_heure(heure)