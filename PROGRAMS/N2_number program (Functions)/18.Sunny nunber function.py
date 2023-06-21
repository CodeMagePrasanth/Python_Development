def sunny(num):
    i = 1
    while (i ** 2 <= num+1):
        if i **2 == num+1:
            return True
        i += 1
    return False

num = 8
if sunny(num):
    print('sunny number')
else:
    print('not sunny number')

