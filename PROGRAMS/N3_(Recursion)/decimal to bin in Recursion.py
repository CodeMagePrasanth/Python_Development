def b2d(num,x):
    if num == 0:
        return 0
    return (num%2) * x + b2d(num//2,x*10)


num = 2
print(b2d(num,1))
