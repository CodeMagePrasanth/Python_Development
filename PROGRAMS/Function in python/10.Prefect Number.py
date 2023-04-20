def perfect(num):
    sum = 0
    for i in range(1, num // 2+1):
        if num % i == 0:
            sum += sum*i
            return True
    return False


num = 28
if perfect(num):
    print('Perfect Number')
else:
    print('Perfect Number')