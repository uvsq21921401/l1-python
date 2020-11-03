#temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes

def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    tempsEnHeure = temps[0] * 24 + temps[1]
    heureEnMinute = tempsEnHeure * 60 + temps[2]
    resultatenS = heureEnMinute * 60 + temps[3]
    return resultatenS 

#temps = (3,23,1,34)
#print(type(temps))
#print(tempsEnSeconde(temps))


def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    Seconde_final = seconde % 60
    SecondeEnMinute = seconde // 60
    Minute = SecondeEnMinute % 60
    MinuteEnHeure = SecondeEnMinute // 60
    Heure = MinuteEnHeure % 24
    Jour = MinuteEnHeure // 24
    return (Jour, Heure, Minute, Seconde_final)
    
#temps = secondeEnTemps(100000)
#print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")

#fonction auxiliaire ici

def afficheUnitéTemps(nb, unité):
    if nb == 0 :
        return
    if nb == 1 :
        print(nb, unité, end=" ")
        return
    if nb > 1 :
        print(nb, unité + "s", end=" ")
        return
    
def afficheTemps(temps):
    afficheUnitéTemps(temps[0], "Jour")
    afficheUnitéTemps(temps[1], "Heure")
    afficheUnitéTemps(temps[2], "Minute")
    afficheUnitéTemps(temps[3], "Seconde")
    return
    
#afficheTemps((1,0,14,23))    

def demandeTemps(temps):
    jour = int(input("Saisir un nombre"))
    heure = int(input("Saisir un nombre"))
    while heure > 24 or heure < 0:
        heure = int(input("Erreur ! Saisir un nombre entre 0 et 24"))
    minute = int(input("Saisir un nombre"))
    while minute < 0 or minute > 60 :
        minute = int(input("Erreur ! Saisir un nombre entre 0 et 60"))
    seconde = int(input("Saisir un nombre"))
    while seconde < 0 or seconde > 60 :
        seconde = int(input("Erreur ! Saisir un nombre entre 0 et 60"))
    return (jour, heure, minute, seconde)

#afficheTemps(demandeTemps(temps))

def sommeTemps(temps1,temps2):
    temps1 = tempsEnSeconde(temps1)
    temps2 = tempsEnSeconde(temps2)
    tempsTotal = temps1 + temps2
    afficheTemps(secondeEnTemps(tempsTotal))
    return
    
#sommeTemps((2,3,4,25),(5,22,57,1))

"""calcul un temps - un pourcentage et appeler la fonction en échangeant l'ordre des arguments"""
def proportionTemps(temps,proportion):
    if type(proportion) != type(4.0):
        (temps, proportion) = (proportion, temps)
    temps = tempsEnSeconde(temps)
    temps_pourcentage = int(temps * proportion)
    return secondeEnTemps(temps_pourcentage)

#afficheTemps(proportionTemps(0.2, (2,0,36,0)))


""" Dite si une année est bissextile pour retire le bon nb de jour dans une année """
def bissextile_1(année, jour):
    if année % 4 == 0 and not (année % 100 != 0 and not (année % 400 == 0)):
        jour -= 366 #bissextile
    else :
        jour -= 365 #pas bissextile
    return jour

"""donne le temps écoulé"""
def tempsEnDate(temps):
    date = [0, temps[0], temps[1], temps[2], temps[3]]
    while date[1] > 365 :
        date[1] = bissextile_1(date[0], date[1])
        date[0] += 1
    return date

def afficheDate(date = -1):
    if (type(date) == (type(0))):
        return
    afficheUnitéTemps(date[0] + 1970, "Année")
    afficheUnitéTemps(date[1], "Jour")
    afficheUnitéTemps(date[2], "Heure")
    afficheUnitéTemps(date[3], "Minute")
    afficheUnitéTemps(date[4], "Seconde")
    return

#temps = secondeEnTemps(1000000000)
#afficheTemps(temps)
#afficheDate(tempsEnDate(temps))
#afficheDate()

import time
afficheDate(time.time())