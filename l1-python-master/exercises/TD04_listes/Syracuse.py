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


def testeConjecture(n_max) :
    syracuse(n_max)
    if n_max == 1 :
        return True


print(testeConjecture(10000))