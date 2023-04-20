def perfect(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += sum+i
    return sum


num = 9
if perfect(num):
    print('Perfect Number')
else:
    print('Not Perfect Number')
