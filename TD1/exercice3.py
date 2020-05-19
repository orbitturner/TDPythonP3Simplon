#coding:utf-8

'''
ENONCE : 
Exercice 3:
Version 1 :
Faire un programme qui saisit 3 résistances : R1, R2 et R3.
Calculer et afficher la résistance en série : R1 + R2 +R3
Calculer et afficher la résistance en parallèle : (R1 * R2 * R3) / (R1*R2 + R2*R3 + R1*R3)
Version 2 :
Demander a l’utilisateur d’indiquer son choix.
S’il entre la valeur 1, calculer et afficher la fréquence en série.
S’il entre la valeur 2, calculer et afficher la fréquence en parallèle.
'''
import os

# GLOBALS 
r1, r2, r3 = 0.0, 0.0, 0.0
rs, rp = 0.0, 0.0
# FONCTION QUI RECUPERE ET CONTROLE LA SAISIT DES VALEURS PAR L'USER
def pickResistances():
    valTester = False
    global r1, r2, r3, rs, rp
    while valTester != True:
        try:
            r1 = float(input("\n→ Veuillez Saisir la première resistance: "))
            r2 = float(input("\n→ Veuillez Saisir la deuxième resistance: "))
            r3 = float(input("\n→ Veuillez Saisir la troisième resistance: "))
            valTester = True
        except ValueError:
            valTester = False
            print("!! SAISISSEZ DES NOMBRES REELS VALIDES !!")
            os.system("pause")
            os.system("cls")
            continue
    rs = r1 + r2 + r3
    rp = (r1 * r2 * r3) / (r1*r2 + r2*r3 + r1*r3)

def afficher(a):
    if a == 1:
        print("\n→ La Resistance en serie est égale à :", rs)
    else:
        print("\n→ La Resistance en serie est égale à :", rp)

loaded = True
os.system("cls")

# PROGRAM STARTED 
while loaded:
    print("\n====================| EXERCICE 3 - TD1 |====================\n")
    print("\t 1 ----> APPLICATION 1")
    print("\t 2 ----> APPLICATION 2")
    print("\t 3 ----> \t QUITTER")
    print("===========================================================")

    choiceCondition = False

    while choiceCondition == False: 
        try:
            choice = int(input("\n Veuillez faire un Choix:  "))
            choiceCondition = True
        except ValueError:
            print("! VEUILLEZ ENTRER UN NOMBRE ENTIER VALIDE !")
            os.system("pause")
            os.system("cls")
            continue

    # VERSION 1 - EXO 3
    if choice == 1:
        # STARTING V1
        os.system("cls")
        print("\n-------------------> EXO 3 - APP1 <-------------------\n")
        # recuperation des Variables
        pickResistances()
        afficher(1)
        afficher(2)
        print("")
        os.system("pause")
        continue
        # ENDING V1

    # VERSION 2 - EXO 3
    elif choice == 2:
        # STARTING V2
        os.system("cls")
        print("\n-------------------> EXO 3 - APP2 <-------------------\n")
        # recuperation des Variables
        pickResistances()
        os.system("cls")
        print("\n\t1..................RESISTANCE EN SERIE")
        print("\t2..............RESISTANCE EN PARALLELE")
        correct = False

        while correct == False: 
            try:
                choixUser = int(input("\n → Faites un Choix:  "))
                correct = True
            except:
                print("! VEUILLEZ ENTRER UN NOMBRE ENTIER VALIDE !")
                os.system("pause")
                os.system("cls")
                continue
        if choixUser == 1:
            afficher(1)
            os.system("pause")
            continue
        elif choixUser == 2:
            afficher(2)
            os.system("pause")
            continue
        else:
            print("!! CHOIX INCORRECTE !!")
            os.system("pause")
            os.system("cls")
            continue
    # EXITING THE PROGRAM
    elif choice == 3:
        os.system("cls")
        print("Fermeture du programme....")
        os.system("pause")
        exit()
    # OTHER INCORRECT VALUES
    else:
        print("!! Ce Choix n'Existe Pas !!")
        os.system("pause")
        os.system("cls")
        continue