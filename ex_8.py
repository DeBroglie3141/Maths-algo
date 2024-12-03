def truc():
    liste = []
    for i in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    if i**3 + j**3 + k**3 + l**3 == 1000*i + 100*j + 10*k + l :
                        liste.append(1000*i + 100*j + 10*k + l)
    print(*liste)

truc()

print([i**3 + j**3 + k**3 + l**3 for i in range(10) for j in range(10) for k in range(10) for l in range(10) if i**3 + j**3 + k**3 + l**3 == 1000*i + 100*j + 10*k + l])


# 0 1 153 370 371 407