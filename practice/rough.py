def fact(num):
    if num ==0:
        return 1
    return num%10 * fact(num-1)

num = 5
print(fact(num))