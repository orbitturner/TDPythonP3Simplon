#coding: utf-8

'''
ENONCE 9 : Ecrire un algorithme qui donne la durée de vol en heure minute connaissant l'heure de départ et
l'heure d'arrivée.

'''
import os

# STARTING OF THE PROGRAM
os.system("cls")
print("\n====================| EXERCICE 9 - TD1 |====================\n")

# RECUPERATION & CONTROLE DES VALEURS SAISIES
correct = False
while not(correct):
    try:
        print("\n\t\t[HEURE DE DEPART]")
        hd = int(input("-> VEUILLEZ DONNER L'HEURE DE DEPART: "))
        md = int(input("-> VEUILLEZ DONNER LA MINUTE DE DEPART: "))

        print("\n\t\t[HEURE DE D'ARRIVE]")
        ha = int(input("-> VEUILLEZ DONNER L'HEURE DE D'ARRIVE: "))
        ma = int(input("-> VEUILLEZ DONNER LA MINUTE DE D'ARRIVE: "))
        assert hd >= 0 and md >= 0 and ha >= 0 and ma >= 0 
    except ValueError:
        print("\n!! VOUS AVEZ SAISI UNE VALEUR INCORRECTE !!")
        continue
    except AssertionError:
        print("\n!! LA VALEUR DOIT ETRE SUPERIEUR OU EGALE A 0 !!")
        continue
    else:
        correct = True

# CALCULS
if ma > md:
    hvol = ha - hd
    mvol = ma - md
    print("\n===============================>RESULTAT :<===============================\n")
    print("\n-> LA DUREE DU VOL SERA DE {}H:{}mn".format(hvol,mvol))
    print("\n==========================================================================\n")
else:
    hvol = ha - hd - 1
    mvol = ma + 60 - md
    print("\n===============================>RESULTAT :<===============================\n")
    print("\n-> LA DUREE DU VOL SERA DE {}H:{}mn".format(hvol,mvol))
    print("\n==========================================================================\n")
    os.system("pause")