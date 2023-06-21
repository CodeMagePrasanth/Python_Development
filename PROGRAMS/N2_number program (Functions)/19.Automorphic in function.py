def auto(num,square):
    while num != 0:
        if (num % 10) != (square%10):
            return False
        num //= 10
        square //= 10
    return True

num = 25
square= num ** 2
if auto(num,square):
    print('Automorphic number')
else:
    print(' Not Automorphic number')