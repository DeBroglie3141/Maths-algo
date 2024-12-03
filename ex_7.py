def factorielle():
    n = int(input())
    if n < 0 :
        return 'Wtf'
    elif n == 0 :
        return 1
    
    for i in range(1,n):
        n *= i
    return n

def hyperfactorielle():
    n = int(input())
    if n < 0 :
        return 'Wtf'
    elif n == 0 :
        return 1
    
    for i in range(1,n+1):
        n*= i**i
    return n

def superfactorielle():
    n = int(input())
    if n < 0 :
        return 'Wtf'
    elif n == 0 :
        return 1
    t = factorielle(n)
    for i in range(1,n):
        t *= factorielle(i)
    return t

def hyperpuissance():
    a, n =int(input()), int(input())
    if n == a == 0 :
        return 'Wtf'
    t = a
    for _ in range(n-1):
        t = t**a
    return t
    
print(hyperpuissance())


#Résultats
#10! = 3628800
#30! = 265252859812191058636308480000000
#H(4) = 27648
#H(5) = 86400000
#sF(4) = 288
#sF(5) = 34560
#2ii4 = 256
#9ii2 = 387420489
