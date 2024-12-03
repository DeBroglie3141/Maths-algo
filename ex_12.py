def egal(f, g):
    return f[0] * g[1] == g[0] * f[1]

def pgcd(a, b):
    p, r = a, b
    while r != 0:
        p, r = r, p % r
    return p

def simpl(f):
    return [f[0] // pgcd(f[0], f[1]), f[1] // pgcd(f[0], f[1])]

def inverse(f):
    return [f[1], f[0]]

def opp(f):
    return [-f[0], f[1]]

def produit(f, g):
    return simpl([f[0] * g[0], f[1] * g[1]])

def somme(f, g):
    return simpl([f[0] * g[1] + f[1] * g[0], f[1]*g[1]])
