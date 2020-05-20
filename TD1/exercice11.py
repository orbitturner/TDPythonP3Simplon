#coding: utf-8

'''
ENONCE 11 : Ecrire un algorithme calculateur permettant la saisie du premier entier (a) de l'opération (+ ou – ou *
ou / : sont des caractères) et du deuxième entier (b) et qui affiche le résultat.

'''
import os

# STARTING OF THE PROGRAM
os.system("cls")
print("\n====================| EXERCICE 11 - TD1 |====================\n")

# RECUPERATION & CONTROLE DES VALEURS SAISIES
correct = False
while not(correct):
    try:
        a = int(input("-> VEUILLEZ DONNER LE PREMIER ENTIER A: "))
        oper = input("-> CHOISISSEZ L'OPERATEUR ['/' - '*' - '+' - '-'] :")
        b = int(input("-> VEUILLEZ DONNER LE DEUXIEME B: "))
        assert oper.__len__() == 1
        if oper != '/' and oper != '*' and oper != '+' and oper != '-':
            raise NameError
    except ValueError:
        print("\n!! VOUS AVEZ SAISI UNE VALEUR INCORRECTE !!")
        continue
    except NameError:
        print("\n!! VEUILLEZ SAISIR UN OPERATEUR VALIDE !!\n")
    except AssertionError:
        print("\n!! L'OPERATEUR NE DOIT PAS DEPASSER UN CARACTERE !!\n")
    else:
        correct = True
print("")

# CALCULS & AFFICHAGE
if oper == '+':
    os.system("pause")
    print("\n===============================>RESULTAT :<===============================\n")
    print("\t\t LA SOMME DE",a,"ET DE",b,"DONNE :",a + b)
    print("\n==========================================================================\n")
else:
    if oper == '-':
        os.system("pause")
        print("\n===============================>RESULTAT :<===============================\n")
        print("\t\t LA SOUSTRACTION DE",a,"ET DE",b,"DONNE :",a - b)
        print("\n==========================================================================\n")
    else:
        if oper == '*':
            os.system("pause")
            print("\n===============================>RESULTAT :<===============================\n")
            print("\t\t LA MULTIPLICATION DE",a,"ET DE",b,"DONNE :",a * b)
            print("\n==========================================================================\n")
        else:
            if b == 0:
                print("!! DIVISION PAR 0 IMPOSSIBLE !!")
            else:
                os.system("pause")
                print("\n===============================>RESULTAT :<===============================\n")
                print("\t\t LA DIVISION DE",a,"ET DE",b,"DONNE :",a / b)
                print("\n==========================================================================\n")
os.system("pause")