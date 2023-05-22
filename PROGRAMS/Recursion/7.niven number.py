def niven(num):
    if num == 0:
        return 0
    return num %10 + niven(num//10)

num = 132
if (num % niven(num) ==0):
    print('niven number')
else:
    print('not Niven number')