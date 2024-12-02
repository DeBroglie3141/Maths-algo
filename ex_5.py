def hms(N=int(input())):
    h = N // 3600
    N -= h*3600
    m = N // 60
    N -= m*60
    s = N
    return h, m, s

print(hms())