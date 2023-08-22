'''
1.not a palindrome
2.number should be prime
3.reversed og given number should be prime
'''
num = 10
rev  = 0
copy = num
while num != 0:
    rev = (rev*10)+(num%10)
    num //= 10
if (rev != copy):
    for i in range(2,copy//2+1):
        if (copy %i == 0):
            print('not emrip')
            break
    else:
        for i in range(2,rev//2+1):
            if (rev % i == 0):
                print('not e')
                break
            else:
                print('emrip rev')
                break
else:
    print('emrip')