def somme(A, B):
    C = []
    if len(A) > len(B):
        for i in range(len(B)):
            C.append(A[i] + B[i])
        C = C + A[:len(B)]
    else :
        for i in range(len(A)):
            C.append(A[i] + B[i])
        C = C + A[:len(A)]
    return C