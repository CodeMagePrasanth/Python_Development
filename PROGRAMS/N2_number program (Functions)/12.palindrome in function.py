def palindorme(num):
    rev = 0
    while(num != 0):
        rem = num % 10
        rev = (rev*10) +rem
        num //= 10
    return rev

num=121
if (num == palindorme(num)):
    print('Palindrome')
else:
    print('NotPalindrome')