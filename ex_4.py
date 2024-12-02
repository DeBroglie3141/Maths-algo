def max2(x, y):
    return x if (x>y) else y

max2(int(input()), int(input()))

def max3(x, y, z):
    return max2(x, max2(y, z))

max3(int(input()), int(input()), int(input()))