def palindorme(num,x):
    if num ==0:
        return 0
    return (num%10)* x + palindorme(num//10,x//10)
num = 121
if num==palindorme(num,10**(len(str(num))-1)):
    print('palindomre ')
else:
    print(' not palindomre ')