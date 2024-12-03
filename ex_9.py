def dichoto(n):
    a, b = 1, 2
    for k in range(n):
        x = (a+b)/2
        if x**3 - x**2 -x -1 < 0 :
            a = x
        else :
            b = x
        print(k+1, x, x**3 - x**2 - x -1 < 0, a, b)
    return a, b

print(dichoto(int(input())))