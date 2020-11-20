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
        syracuse(n)
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



