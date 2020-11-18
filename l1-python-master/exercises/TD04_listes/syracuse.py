 def syracuse(n):
    """ Retourne la liste des valeurs de la suite en partant de n jusqu'à 1 """
    liste =[]
    while n != 1 :
        if n % 2 == 0 :
            n //= 2
            liste.append(n)
        elif n % 2 != 0 :
            n *= 3
            n += 1
            liste.append(n)
    return(liste)

print(syracuse(3))