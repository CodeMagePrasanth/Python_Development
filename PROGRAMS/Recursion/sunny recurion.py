def sunny(num,n):
    if (n**2 > num+1):
        return False
    if (n**2 == num+1):
        return True
    return sunny(num,n+1)
num = 8
if sunny(num,1):
    print('sunny')
else:
    print(' not sunny')