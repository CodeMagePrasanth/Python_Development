def arm(num, p):
    add = 0
    while num != 0:
        rem = num % 10
        add += rem ** p
        num //= 10
    return add


num = 153
if num == arm(num, len(str(num))):
    print('arm strong number')
else:
    print('not armstrong umber ')