def add(num):
    if num == 0:
        return 0
    return (num%10)**2 + add(num//10)
def happy(num):
    if num < 10:
        return num
    return happy(add(num))
num = 23
if (happy(num) == 1):
    print('happy number')
else:
    print('not happy number')