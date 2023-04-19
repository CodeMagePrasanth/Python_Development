def arm(num):
    add = 0
    count = len(str(num))
    while num != 0:
        rem = num % 10
        add += rem ** count
        num //= 10
    return add

num = 153
if num ==arm(num):
    print('arm strong number')
else:
    print('not armstrong number ')