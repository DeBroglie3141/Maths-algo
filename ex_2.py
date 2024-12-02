def bissextile(n):
    return n%4 == 0 if n%100 != 0 else n%400 == 0
print(bissextile(int(input())))