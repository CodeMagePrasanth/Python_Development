def pronic(num,n):
    if (n*(n+1) <= num):
        if (n*(n+1) == num):
            return True
        return False or pronic(num,n+1)
    return False
num = 12
if pronic(num,1):
    print('pronic')
else:
    print(' not pronic')