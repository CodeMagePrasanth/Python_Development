def tryn(num,sq):
    if num ==0:
        return True
    if (num%10 != sq%10):
        return False
    return tryn(num//10,sq//10)
num = 25
if tryn(num,num**3):
    print('Trimorpic')
else:
    print(' not Trimorpic')