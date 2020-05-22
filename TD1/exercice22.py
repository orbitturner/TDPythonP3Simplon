#coding: utf-8

'''
ENONCE 22 : On propose de saisir N entiers différents entre 1 et 100 (N étant un entier naturel compris entre 10 et
50) puis afficher la plus longue séquence croissante tout en précisant la position du premier nombre de cette
séquence.
'''
import os

# STARTING OF THE PROGRAM
welcMsg = "\n\t\t--> HELLO {0} !!<--\n".format(os.getlogin())
os.system("cls")

print("\n====================| EXERCICE 22 - TD1 |====================\n")
print(welcMsg.center(len(welcMsg), " "))

# RECUPERATION & CONTROLE DES VALEURS SAISIES POUR LA TAILLE DE LA LISTE
correct = False
while not(correct):
    try:
        print("\n\t\t[(: CREATION DE LA LISTE DE VALEUR :)]")
        nbVal = int(input("-> COMBIEN DE VALEUR VOULEZ-VOUS SAISIR ?: "))
        assert nbVal >= 10 and nbVal <= 50
    except ValueError:
        print("\n!! VOUS AVEZ SAISI UNE VALEUR INCORRECTE !!")
        continue
    except AssertionError:
        print("\n!! SAISISSEZ UNE VALEUR ENTRE 10 ET 50 !!")
    else:
        # nbVal -= 1
        # nbVal -1 car on part de 0
        correct = True
print("")

# CREATION & REMPLISSAGE DE LA LISTE
tabVal = []# Liste Vide Agissant come un tableau
print("\n\t\t[(: REMPLISSAGE DE LISTE DES VALEURS :)]\n")
for i in range(0, nbVal):
    ok  = False
    while not(ok):
        try:
            print("\n\t\t\t[VALEUR N°",i+1,"]")
            tabVal.append(int(input("\n-> ENTRER UNE VALEUR : ")))
        except ValueError:
            print("\n!! VOUS AVEZ SAISI UNE VALEUR INCORRECTE !!")
        else:
            ok = True

# DETERMINATION DE LA SOUS SEQUENCE
longest = 0 
cpt = 0
for i in range (0,nbVal):
    if(i != nbVal-1):
        if(tabVal[i] < tabVal[i+1]):
            cpt += 1
            lastValPos = i + 1
            if cpt == 1:
                initialPos = i
        else:
            # TEST IF ITS NOT THE LONGEST SUBSEQUENCE
            if(cpt > longest):
                longest = cpt
                starting = initialPos
                ending = lastValPos
            initialPos = 0
            cpt = 0
            lastValPos = 0

# AFFICHAGE DU RESULTAT
os.system("pause")
print("\n===============================>RESULTAT :<===============================\n")
print("\n\t➡ LA PLUS LONGUE SOUS SEQUENCE A UNE LONGUEUR DE: ",longest+1)
print("\n\t➡ ELLE DEBUTE A LA POSITION : ",starting)
print("\n\t➡ ELLE SE TERMINE A LA POSITION: ",ending)
print("\n\t---------------| AFFICHAGE DE LA SOUS SEQUENCE |----------------")
print("\t\t", end=" ")
for i in range(starting,ending):
        print(tabVal[i], end=" - ")
print("\n==========================================================================\n")
os.system("pause")