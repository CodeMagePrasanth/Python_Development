def addSqure(num):
    add = 0
    while(num != 0):
        rem = num%10
        add += (rem**2)
        num //= 10
    return add
def happy(num):
    while(num>9):
        num = addSqure(num)
    return num == 1

num = 49
if (happy(num)):
    print('Happy number')
else:
    print(' Not Happy number')