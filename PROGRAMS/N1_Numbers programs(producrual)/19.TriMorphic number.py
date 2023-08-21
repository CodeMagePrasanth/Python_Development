num = 25
cube = num**3
while (num != 0):
    # rem1 = num%10
    # rem2 = sq%10
    # if (rem1 !=rem2):
    if (num%10 != cube%10):
        print('not trimorphic')
        break
    num//=10
    cube//=10
else:
    print('trimorphic')
