def diviseurs(n):
    liste_diviseurs = [n]
    for i in range(1,int(n**0.5)  + 1):
        if n%i == 0 :
            liste_diviseurs.append(i)
    liste_diviseurs.sort()
    return liste_diviseurs

def is_prime(n):
    return str(n) + ' est premier' if len(diviseurs(n)) == 2 else str(n) + " n'est pas premier"

def parfaits(n):
    return [i for i in range(1,n+1) if sum(diviseurs(i)) == 2*i]

print(is_prime(5))
