def strong(num, copy):
    add = 0
    while num != 0:
        rem = num % 10
        fact = 1
        for i in range(1, rem+1):
            fact *= i
        add += fact
        num //= 10
    return add


num = 123
if strong(num, num):
    print('Strong number')
else:
    print('Not strong number')
