#coding: utf-8

'''
ENONCE 15 : Ecrire un algorithme qui demande un nombre de départ, et qui calcule la somme des entiers jusqu'à
ce nombre. Par exemple si l'on tape 4, l’algorithme doit calculer : 1 + 2 + 3+ 4 = 10 Réécrire l'algorithme qui calcule
cette fois la moyenne !
PROGRAMME APP1

'''
import os

# STARTING OF THE PROGRAM
os.system("cls")
print("\n====================| EXERCICE 15 - TD1 |====================\n")

# RECUPERATION & CONTROLE DES VALEURS SAISIES
correct = False
while not(correct):
    try:
        nombre = abs(int(input("-> VEUILLEZ SAISIR UN NOMBRE ENTIER: ")))
    except ValueError:
        print("\n!! VOUS AVEZ SAISI UNE VALEUR INCORRECTE !!")
        continue
    else:
        correct = True
print("")

# V1 ou V2
exact = False
while not(exact):
    try:
        print("\n==================================================================\n")
        print("\t\t--> QUE VOULEZ-VOUS CALCULER ? <--")
        print("\n\t==> 1 ............. LA SOMME DES ENTIERS")
        print("\n\t==> 2 ............. LA MOYENNE DES ENTIERS")
        print("\n==================================================================\n")
        choice = int(input("-> VEUILLEZ SAISIR UN NOMBRE ENTIER: "))
        assert choice == 1 or choice == 2
    except ValueError:
        print("\n!! VOUS AVEZ SAISI UNE VALEUR INCORRECTE !!")
        os.system("pause")
        os.system("cls")
        continue
    except AssertionError:
        print("\n!! VEUILLEZ FAIRE UN CHOIX ENTRE 1 & 2 !!\n")
        os.system("pause")
        os.system("cls")
        continue
    else:
        exact = True
print("")

# CALCULS
som = 0
i = 1 
while i < nombre:
    som += i
    i+=1

# AFFICHAGES
print("\n===============================>RESULTAT :<===============================\n")
# CASING
if choice == 1:
    print("\n\t\tLA SOMME DES CHIFFRES DE 1 à {0} DONNE {1}: \n".format(nombre, som))
    os.system("pause")
else:
    print("\n\t\tLA MOYENNE DES CHIFFRES DE 1 à {0} DONNE {1}: \n".format(nombre, (som/i)))
print("\n==========================================================================\n")
os.system("pause")