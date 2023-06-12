def strong(num,copy):
    add = 0
    while num != 0:
        rem = num % 10
        fact = 1
        for i in range(1, rem+1):
            fact *= i
        add += fact
        num //= 10
    return add==copy


num = 145
if strong(num,num):
    print('strong number')
else:
    print('not strong number')
