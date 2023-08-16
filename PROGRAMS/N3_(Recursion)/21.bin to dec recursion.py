def b2d(num,x):
    if num == 0:
        return 0
    return (num%10) * x + b2d(num//10,x*2)


num  = 1001
print(b2d(num,1))
