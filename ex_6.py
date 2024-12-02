N, a, b = int(input()), 0, 2

for k in range(N+1):
    a = (2+a)**0.5
    b = 2*b/a
print(b)