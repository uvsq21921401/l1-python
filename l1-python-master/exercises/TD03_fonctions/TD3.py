#temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes

def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    tempsEnHeure = temps[0] * 24 + temps[1]
    heureEnMinute = tempsEnHeure * 60 + temps[2]
    resultatenS = heureEnMinute * 60 + temps[3]
    return resultatenS 

temps = (3,23,1,34)
print(type(temps))
print(tempsEnSeconde(temps))   


def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    Seconde_final = seconde % 60
    SecondeEnMinute = seconde // 60
    Minute = SecondeEnMinute % 60
    MinuteEnHeure = SecondeEnMinute // 60
    Heure = MinuteEnHeure % 24
    Jour = MinuteEnHeure // 24
    return (Jour, Heure, Minute, Seconde_final)
    
temps = secondeEnTemps(100000)
print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")

#fonction auxiliaire ici

def afficheTemps(temps):
    afficheUnitéTemps(temps[0], "Jour")
    afficheUnitéTemps(temps[1], "Heurs")
    afficheUnitéTemps(temps[2], "Minute")
    afficheUnitéTemps(temps[3], "Seconde")
    return
    
afficheTemps((1,0,14,23))    

def afficheUnitéTemps(nb, unité) :
    if nb == 0 :
        return
    if nb == 1 :
        print(nb, unité)
        return
    if nb > 1 :
        print(nb, unité + "s")
        return
    