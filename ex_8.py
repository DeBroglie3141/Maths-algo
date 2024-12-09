def truc():
    liste = []
    for i in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    if n := i**3 + j**3 + k**3 + l**3 == 1000*i + 100*j + 10*k + l :
                        liste.append(n)
    print(*liste)

truc()

print([n for i in range(10) for j in range(10) for k in range(10) for l in range(10) if (n := i**3 + j**3 + k**3 + l**3 == 1000*i + 100*j + 10*k + l)])


# 0 1 153 370 371 407