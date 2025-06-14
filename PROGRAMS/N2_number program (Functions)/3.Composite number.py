def composite(num):
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count += 1
    return count > 2


num = 5
if composite(num):
    print('Composite number')
else:
    print('Not composite number')