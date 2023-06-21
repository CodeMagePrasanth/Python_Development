def reverse(num):
    rev = 0
    while num !=0:
        rev = (rev*10) + (num%10)
        num //= 10
    return rev
def prime(num):
    count= 0
    for i in range(1,num+1):
        if num%i == 0:
            count=count+1
    if (count == 2):
        return True
    return False
num = 11
if (num == reverse(num) and prime(num)):
    print('paly prime')
else:
    print(' Not paly prime')