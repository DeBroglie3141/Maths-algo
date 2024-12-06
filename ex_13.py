from ex_12 import *

def egypt(a, b):

    liste_p = []
    a, b = min(a, b), max(a, b)

    p = b//a if b%a == 0 else int(b/a) + 1
    print('1 /', p, end=' + ')

    while a*p != b :
        f = simpl([(a*p - b), b*p])
        p = f[1] // f[0] if f[0]%f[1] == 0 else int(f[1] / f[0]) + 1
        print('1 /', p, end=' + ')

egypt(5, 6)

print('hello')