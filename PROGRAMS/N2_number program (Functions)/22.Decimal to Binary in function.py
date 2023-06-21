def d2b(num):
    bin = 0
    x = 1
    while (num != 0):
        rem = num%2
        bin = bin + (rem * x)
        x = x*10
        num //= 2
    return bin

num = 17
print(d2b(num))