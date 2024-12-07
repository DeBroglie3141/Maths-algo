def somme(A, B):
    A.reverse(); B.reverse()
    max_len = max(len(A), len(B))
    C = [a + b for a, b in zip(A, B)]
    C += A[len(B):] if len(A) > len(B) else B[len(A):]
    C.reverse()
    return C

# Tests
A = [1, 2, 3, 4, 5]
B = [6, 7, 8]
print(somme(A, B))
