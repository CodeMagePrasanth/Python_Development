def perfect(num):
    sum = 0
    for i in range(1, num//2+1):
        if num % i == 0:
            sum += i
    return sum


num = 28
if perfect(num):
    print('Perfect Number')
else:
    print('Not Perfect Number')
