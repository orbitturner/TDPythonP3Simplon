#coding: utf-8

'''
ENONCE 10 : Ecrire un algorithme qui lit trois valeurs entières (A, B et C) et qui permet de les trier par échanges
successifs Et enfin les afficher dans l'ordre .

'''
import os

def switch(a,b):
    a, b = b, a
    return a, b

# STARTING OF THE PROGRAM
os.system("cls")
print("\n====================| EXERCICE 10 - TD1 |====================\n")

# RECUPERATION & CONTROLE DES VALEURS SAISIES
correct = False
while not(correct):
    try:
        a = int(input("-> VEUILLEZ DONNER LA VALEUR DE A: "))
        b = int(input("-> VEUILLEZ DONNER LA VALEUR DE B: "))
        c = int(input("-> VEUILLEZ DONNER LA VALEUR DE C: "))
        # assert hd >= 0 and md >= 0 and ha >= 0 and ma >= 0 
    except ValueError:
        print("\n!! VOUS AVEZ SAISI UNE VALEUR INCORRECTE !!")
        continue
    else:
        correct = True
print("")

# CALCULS
if a > b:
    a,b = switch(a,b)
    if b > c:
        b,c = switch(b,c)
        if a > b:
            a, b = switch(a, b)
else:
    if b > c:
        b, c = switch(b,c)
        if a > b:
            a, b = switch(a,b)

# AFFICHAGE
os.system("pause")
print("\n===============================>RESULTAT :<===============================\n")
print("\t\t A - B - C DANS L'ORDRE DONNE :",a,b,c)
print("\n==========================================================================\n")