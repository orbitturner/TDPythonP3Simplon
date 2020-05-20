#coding: utf-8

'''
ENONCE 16 : Faire un programme qui calcule et affiche la division de a par b 
par soustractions successives

'''
import os

# STARTING OF THE PROGRAM
os.system("cls")
print("\n====================| EXERCICE 16 - TD1 |====================\n")

# RECUPERATION & CONTROLE DES VALEURS SAISIES
correct = False
while not(correct):
    try:
        a = int(input("-> VEUILLEZ SAISIR UN NOMBRE ENTIER: "))
        b = int(input("-> VEUILLEZ SAISIR UN NOMBRE ENTIER: "))
        assert b != 0
    except ValueError:
        print("\n!! VOUS AVEZ SAISI UNE VALEUR INCORRECTE !!")
        continue
    except AssertionError:
        print("\n\t!! NOUS NE POUVONS PAS DIVISER PAR 0 !!")
        continue
    else:
        correct = True
print("")

# CALCULS
quotient = 0
# CAS NEGATIF
if a < 0 or b < 0:
    signe = -1
else:
    signe = 1
a = abs(a)
b = abs(b)
while a >= b:
    a -= b
    quotient += 1

# AFFICHAGE
print("\n===============================>RESULTAT :<===============================\n")
print("\n\t\tLA DIVISION PAR SOUSTRACTION SUCCESSIVE DE",a,"ET",b,"EST: ",quotient,"\n")
print("\n==========================================================================\n")
os.system("pause")
    