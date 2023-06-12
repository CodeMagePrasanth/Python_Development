num = 145
add = 0 
copy = num
while(num != 0):
    rem = num%10
    fact = 1
    for i in range(1,rem+1):
        fact*=i
    add+=fact
    num=num//10
if (add == copy):
    print('strong number')
else:
    print('not strong number')