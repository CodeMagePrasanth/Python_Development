def perfect(num,i,sum):
    if (i == num//2+1) :
        return sum
    if (num % 1 == 0):
        sum += i
    return perfect(num,i+1,sum)
num = 28
if (num == perfect(num,1,0)):
    print('perfect num')
else:
    print(' not perfect num')