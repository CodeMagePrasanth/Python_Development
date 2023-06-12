def reverse(num,copy):
    rev = 0
    while num != 0 :
        rem = (rev*10) + (num%10)
        num //= 10
    return copy==rem


num = 1221
print(reverse(num,num))