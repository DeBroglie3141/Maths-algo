def somme(A, B):
    A.reverse(); B.reverse()
    max_len = max(len(A), len(B))
    C = [a + b for a, b in zip(A, B)]
    C += A[len(B):] if len(A) > len(B) else B[len(A):]
    C.reverse()
    return C

def produit(A, B):
    C = [0] * (len(A) + len(B) - 1) 
    for i in range(len(A)) :
        for j in range(len(B)):
            C[i+j] += A[i] * B[j]
    C.reverse()
    return C

def eval(P, a):
    n = 0
    for i in range(len(P)):
        n += P[i]*(a**i)
    return n

# Tests
A = [1, 2]
B = [-2, 3, 4]
print(somme(A, B))
print(produit(A, B))
print(eval(B, -2))
