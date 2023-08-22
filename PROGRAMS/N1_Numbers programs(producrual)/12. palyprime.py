num = 11
rev = 0
copy = num
while num != 0:
    rev = (rev*10) + (num % 10)
    num //= 10
if (rev == copy and copy > 1):
    for i in  range(2,copy//2+1):
        if copy % i ==0:
            print('Not polyprime')
            break
        else:
            print('polyprime')
            break
else:
    print('Not polyprime')
