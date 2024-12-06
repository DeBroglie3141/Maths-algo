def diviseurs(n):
    liste_diviseurs = [n]
    for i in range(1,n//2 + 1):
        if n%i == 0 :
            liste_diviseurs.append(i)
    liste_diviseurs.sort()
    return liste_diviseurs

def is_prime(n):
    if len(diviseurs(n)) == 2 :
        return str(n) + ' est premier'
    else :
        return str(n) + " n'est pas premier"
    

def parfaits(n):
    return [i for i in range(1,n+1) if sum(diviseurs(i)) == 2*i]
