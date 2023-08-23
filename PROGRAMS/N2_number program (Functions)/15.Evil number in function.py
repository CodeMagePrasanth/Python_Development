def evil(num):
    count = 0
    while (num != 0):
        if (num%2 == 1):
            count = count+1
        num//=2
    return count % 2 == 0

num = 9
if (evil(num)):
    print('Evil number')
else:
    print(' Not Evil number')