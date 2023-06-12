num = 55
add = 0
val = num
while (num!=0):
    rem = num%10
    add += rem
    num //= 10
if (val % add==0):
    print('Niven Number')
else:
    print('Not Niven Number')