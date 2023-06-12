def reverse(num,x):
    if num == 0:
        return 0
    return (num%10) * x + reverse(num//10,x//10)


num = 1234
l = len(str(num))-1
print(reverse(num,10**l))