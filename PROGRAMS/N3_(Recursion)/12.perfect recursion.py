def perfect(num,i,sum):
    if (i == num//2+1) :
        return sum
    if (num % i == 0):
        sum += i
    return perfect(num,i+1,sum)
num = 6
if (num == perfect(num,1,0)):
    print('perfect num')
else:
    print(' not perfect num')