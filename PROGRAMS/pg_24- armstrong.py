num = 153
count = len(str(num))
add = 0
copy = num
while (num != 0):
    rem = num % 10
    add = add + (rem**count)
    num = num // 10
if(add == copy):
    print('Armstrong')
else:
    print('Not Armstorng')