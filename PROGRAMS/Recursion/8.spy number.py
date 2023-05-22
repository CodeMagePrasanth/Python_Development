def add(num):
    if num ==0:
        return 0
    return num%10 + add(num//10)
def mul(num):
    if num ==0:
        return 1
    return num%10 * mul(num//10)

num = 123
if (add(num) == mul(num)):
    print ('spy')
else:
    print (' not spy')