def b2d(num):
    dec = 0
    x = 1
    while (num != 0):
        rem = num%2
        dec += (rem * x)
        x = x*2
        num //= 10
    return dec

num = 10007
print(b2d(num))