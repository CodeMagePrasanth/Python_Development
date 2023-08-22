num = 222
rev = 0
copy = num
while num != 0:
    rev = (rev*10)+(num%10)
    num //= 10
if (rev == copy):
    print('palindorme')
else:
    print('not palindorme')