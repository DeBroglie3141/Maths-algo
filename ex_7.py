def factorielle(n = int(input())):
    if n < 0 :
        return 'Wtf'
    elif n == 0 :
        return 1
    
    for i in range(1,n):
        n *= i
    return n

print(factorielle())

def hyperfactorielle(n=int(input())):
    if n < 0 :
        return 'Wtf'
    elif n == 0 :
        return 1
    
    for i in range(1,n+1):
        n*= i**i
    return n

print(hyperfactorielle())

def superfactorielle(n=int(input())):
    if n < 0 :
        return 'Wtf'
    elif n == 0 :
        return 1
    t = factorielle(n)
    for i in range(1,n):
        t *= factorielle(i)
    return t

print(superfactorielle())

def hyperpuissance(a=int(input()), n=int(input())):
    if n == a == 0 :
        return 'Wtf'
    
    
    


#Résultats
#10! = 3628800
#30! = 265252859812191058636308480000000
#H(4) = 27648
#H(5) = 86400000
#sF(4) = 288
#sF(5) = 34560
#2ii4 = 
#9ii2 = 
