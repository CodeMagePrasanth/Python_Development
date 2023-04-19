def disarium(num):
    add = 0
    count = len(str(num))
    while num != 0:
        rem = num % 10
        add += rem ** count
        num //= 10
        count-=1
    return add

num = 135
if num == disarium(num):
    print('Disarium number')
else:
    print('not Disarium number ')