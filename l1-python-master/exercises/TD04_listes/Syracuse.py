def syracuse(n) :
    while n != 1 :
        liste = []
        if n % 2 == 0 :
            n //= 2
            liste.append(n)
        elif n % 2 != 0 :
            n *= 3
            n += 1
            liste.append(n)
    return(n)


print(syracuse(3))


def testeConjecture(n_max):
    """ Teste la conjecture de Collatz pour toutes les valeurs de 2 à n_max """
    n_min = 1
    while n_min < n_max :
        n_min += 1
        n = n_min
        n = syracuse(n)
    if n == 1 :
        return True
    return False

print(testeConjecture(10000))




def tempsVol(n):
    """ Retourne le temps de vol de n """
    liste = []
    while n != 1 :
        if n % 2 == 0 :
            n //= 2
            liste.append(n)
        elif n % 2 != 0 :
            n *= 3
            n += 1
            liste.append(n)
    return len(liste)



def estCarreMagique(carre):
    """ Renvoie True si c'est un carre magique et False sinon"""
    cote = len(carre)
    cst_mag = 0
    for h in range(cote) :
        cst_mag += carre[0][h] 
    for i in range(1, cote) :
        somme = 0
        for j in range(cote) :
            somme += carre[i][j]
        if cst_mag != somme :
            return False
    for k in range(cote) :
        somme = 0
        for l in range(cote) :
            somme += carre[l][k]
        if cst_mag != somme :
            return False
    for m in range(cote) :
        somme = 0
        somme += carre[m][m]
    if cst_mag != somme :
        return False
    for n in range(cote) :
        somme = 0
        somme += carre[n][cote - n - 1]
    if cst_mag != somme :
        return False
    return True

carre_mag = [[4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 3, 13]]
carre_pas_mag = [[4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 7, 13]]
print(estCarreMagique(carre_mag))
print(estCarreMagique(carre_pas_mag))




from math import sqrt

def estNormal(carre):
    """ Retourne True si contient toutes les valeurs de 1 à n^2 où n est la taille 
        du carré, et False sinon """
    cote = len(carre)
    if str(int(sqrt(cote))) != "  "  :
        return False
    else : 
        return True

carre_mag = [[4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 3, 13]]
carre_pas_mag = [[4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 7, 13], [16, 2, 7, 13]]
print(estNormal(carre_mag))
print(estNormal(carre_pas_mag))