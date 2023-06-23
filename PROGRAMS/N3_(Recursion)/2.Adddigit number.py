def AddDigit(num):
    if num == 0:
        return 0
    return num % 10 +AddDigit(num//10)


print(AddDigit(1023))