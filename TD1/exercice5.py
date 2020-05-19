#coding: utf-8

'''
ENONCE 5 :
Ecrire un programme qui saisit 5 variables de type entier au clavier et qui affiche leur somme. Utiliser une boucle
(for ou while ou do..while).

'''
import os

os.system("cls")
print("\n====================| EXERCICE 5 - TD1 |====================\n")

n = 5
i = 1
som = 0
while i <= n:
    correct = False
    print("\n\t\t[NOMBRE {0}]".format(i))
    while not(correct):
        try:
            som += int(input("\n-> ENTRER UN NOMBRE :")) 
            correct = True
            i+=1
        except ValueError :
            print("!! VEUILLEZ ENTRER UN NOMBRE ENTIER CORRECT !!")

os.system("pause")
print("\n====================>RESULTAT :<====================\n")
print("\t LA SOMME DES NOMBRES SAISIS EST:",som)
print("\n====================================================\n")