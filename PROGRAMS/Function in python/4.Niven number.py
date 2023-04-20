# ---> Niven number

# ---> for ex:24

def Niven(num,copy):
    add = 0
    while(num != 0):
        add += (num%10)
        num //= 10
    return add%copy
num = 312
if Niven(num,num):
    print('Niven number')
else:
    print('Not niven number')