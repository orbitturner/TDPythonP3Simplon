#coding: utf-8

'''
ENONCE 23 : La multiplication des lapins. 
'''
import os

# STARTING OF THE PROGRAM
welcMsg = "\n\t\t--> HELLO {0} !!<--\n".format(os.getlogin())
os.system("cls")

print("\n====================| EXERCICE 23 - TD1 |====================\n")
print(welcMsg.center(len(welcMsg), " "))

# SETTING UP ALL VARIABLES REQUIRED FOR CALCULATIONS
nbRabbits = 0
cptM = 0
limit = 1_000_000_000
fn0_Month = 0
fn1_Month = 2

# CALCULATING
print("\n===============================>RESULTAT :<===============================\n")
while(nbRabbits < limit):
    nbRabbits = fn1_Month+fn0_Month
    fn0_Month = fn1_Month
    fn1_Month = nbRabbits
    cptM += 1
    if cptM == 12:
        print("\n\t➡ LE NOMBRE DE LAPIN AU BOUT D'UN AN EST : ",nbRabbits)
# ENDING
print("\n\t➡ LE MILLIARD DE LAPIN SERA DEPASSE AU BOUT DE",cptM,"MOIS\n")
print("\n==========================================================================\n")
os.system("pause")