def factorial(num):
    if num == 0:
        return 0
    return (num%10) * factorial(num//10)
num = 5
print(factorial(num))