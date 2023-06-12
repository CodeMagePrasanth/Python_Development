def fact(num):
    if num == 0:
        return 1
    return (num%10) * fact(num-1)
def add(num):
    if num == 0:
        return 0
    return fact(num%10) + add(num//10)


num = 145
print('Strong number' if (num == add(num)) else 'Not Strong number' )
