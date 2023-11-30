import time

heure = (23, 59, 55)#variable pour définir l'heure
alarme = (23, 59, 58)#variable pour définir l'alarme
choix_stop = (0, 0, 0)#variable qui me permet de mettre en pause à une heure définie

def afficher_heure(heure):#définition d'une fonction qui affichera l'heure en continue

    heure_liste = list(heure)#je converti ma variable 'heure' en liste et lui assigne une variable 'heure_liste' 
    heures, minutes, secondes = heure_liste#dans la liste 'heure_liste', j'assigne l'index[0] aux heures, l'index[1] aux minutes, l'index[2] aux secondes 

    while True:#j'initialise une boucle infinie qui mettra à jour l'heure
        if 0 <= secondes < 60 and 0 <= minutes < 60 and 0 <= heures < 24:#cette ligne permet de vérifier la plage horaire
            secondes = (secondes + 1) % 60 #incrémentation des secondes
            if secondes == 0:
                minutes = (minutes + 1) % 60 #incrémentation des minutes
                if minutes == 0:
                    heures = (heures + 1) % 24 #incrémentation des heures
                
        time.sleep(1) #ici je met une pause de 1 seconde avec le module .sleep avec de simuler les secondes

        regler_alarme(alarme, (heures, minutes, secondes)) #appel de la fonction pour vérifier l'alarme
        am_pm(heures, minutes, secondes, format_choisi) #appel de la fonction pour l'affichage de l'heure au format choisi
        stop(heures, minutes, secondes, choix_stop) #appel de la fonction qui me permettra de mettre en pause

format_choisi = input("Choisissez le format (24h ou am/pm): ") #ici je demande à l'utilisateur de choisir le format


def regler_alarme(alarme, heure): #définition de la fonction qui permet de regler l'alarme
    if heure == alarme: #ici je vérifie si l'heure correspond à l'alarme
        print("C'est l'heure :) :) :) :)") #si la condition est ok, ce message s'affiche


def am_pm(heures, minutes, secondes, format_choisi): #définition de la fonction qui permet de définir le format de l'heure

    if format_choisi.lower() == "24h": #ici correspond à la condition pour le format 24h 
        print(f"{heures:02d}:{minutes:02d}:{secondes:02d}") #affichage au format 24h

    elif format_choisi.lower() == "am/pm": #ici correspond à la condition pour le format am/pm
        suffixe = "AM" #initialisation du suffixe à "AM"
        if heures >= 12:
            suffixe = 'PM' #si les heures sont supérieures ou  égales à 12, suffixe = 'PM'
        if heures > 12:
            heures -= 12 #conversion en format 12h si heures > 12
        elif heures == 0:
            heures = 12 #conversion en format 12h si heures = 0

        print(f'{heures:02d}:{minutes:02d}:{secondes:02d} {suffixe}') #affichage au format am/pm

    else:
        print("Format non reconnu. Veuillez choisir entre '24h' ou 'am/pm'.") # si le format est invalide, ce message s'affiche

def stop(heures, minutes, secondes, choix_stop): #définition de la fonction qui gère ma pause
    if choix_stop == (heures, minutes, secondes): #verifie si l'heure correspond à mon variable 'choix_stop'
        pause_reponse = input("Pause, appuyer sur n'importe quelle touche puis 'entrer' pour reprendre): ") #si la condition est respecté, l'heure est suspendu et ce message s'affiche
        if pause_reponse.lower() == " ":
            print("Reprise de l'horloge.")
  


afficher_heure(heure) #enfin j'appel ma fontction pour afficher l'heure en continue