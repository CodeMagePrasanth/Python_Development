num = 25
sq = num**2
while (num != 0):
    # rem1 = num%10
    # rem2 = sq%10
    # if (rem1 !=rem2):
    if (num%10 != sq%10):
        print('not automorphic')
        break
    num//=10
    sq//=10
else:
    print('automorphic')
