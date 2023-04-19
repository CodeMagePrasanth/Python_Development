def disarium(num,p):
    add = 0
    while num != 0:
        rem = num % 10
        add += rem ** p
        num //= 10
        p-=1
    return add

num = 135
if (num == disarium(num,len(str(num)))):
    print('Disarium number')
else:
    print('not Disarium number ')