def tri(num,cube):
    while num != 0:
        if (num % 10) != (cube%10):
            return False
        num //= 10
        cube //= 10
    return True

num = 75
cube= num ** 3
if (tri(num,cube)):
    print('trimorphic number')
else:
    print(' Not trimorphic number')