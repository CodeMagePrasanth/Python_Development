def fascinating(num):
    sum = str(num*1) + str(num*2) + str(num*3)
    for i in range(1, 10):
        if str(i) not in sum:
            return False
    return True


num = 327
if fascinating(num):
    print('Fascinating number')
else:
    print(" Not Fascinating number")