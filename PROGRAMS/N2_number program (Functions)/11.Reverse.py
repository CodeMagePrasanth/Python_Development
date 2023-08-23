def reverse(num,copy):
    rev = 0
    while num != 0 :
        rev = (rev*10) + (num%10)
        num //= 10
    return copy==rev


num = 999
print(reverse(num,num))