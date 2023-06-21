def auto(num,sq):
    if num ==0:
        return True
    if (num%10 != sq%10):
        return False
    return auto(num//10,sq//10)
num = 25
if auto(num,num**2):
    print('Auto morphic')
else:
    print(' not Auto morphic')