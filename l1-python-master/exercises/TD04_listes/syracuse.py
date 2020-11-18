#Part 2
 #Retourne la liste des valeurs de la suite en partant de n jusqu'à 1


def syracuse(n) :
    while n != 1 :
        if n % 2 == 0 :
            n /= 2
        elif n % 2 != 0 :
            n *= 3
            n += 1
    return(n)

print(syracuse(3))