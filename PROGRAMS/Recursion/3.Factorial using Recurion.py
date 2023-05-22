def factorial(num):
    if num == 0:
        return 1
    return (num%10) * factorial(num-1)
num = 5
print(factorial(num))