''' pronic program'''


def pronic(num,i):
    while (i * (i + 1) <= num):
        if i * (i + 1) == num:
            return True
            break
        i += 1
    return False


num = 12
if pronic(num,1):
    print('pronic number')
else:
    print('not pronic')

