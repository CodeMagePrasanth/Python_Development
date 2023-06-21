def Reverse(num):
    rev = 0
    while num != 0:
        rev = (rev * 10) + (num % 10)
        num //= 10
    return rev
def prime(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count = count + 1
    return count == 2

num = 13
rev = Reverse(num)
if (num != rev and prime(num) and prime(rev)):
    print('Emrip number')
else:
    print(' Not Emrip number')