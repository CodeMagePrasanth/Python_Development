num = 49
while(num > 9):
    add = 0
    while (num != 0):
        add += (num%10)**2
        num //= 10
    num = add
if num == 1:
    print('Happy number')
else:
    print('not Happy number')