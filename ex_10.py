def secante(a, b, n):
    a, b = abs(a), abs(b)
    a, b = min(a, b), max(a, b)
    for _ in range(n):
        c = (f(b)*a - f(a)*b) / (f(b) - f(a))
        if f(c) > 0 :
            b = c
        elif f(c) < 0 :
            a = c
        else :
            return 'f(' + c + '= 0'
    return abs(c)

def f(x):
    return x**2 -2

print(secante(int(input()), int(input()), int(input())))