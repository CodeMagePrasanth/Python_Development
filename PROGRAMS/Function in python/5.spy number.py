# ---> spy number
#
# def sum(num):
#     add = 0
#     while (num != 0):
#         add += (num%10)
#         num //= 10
#     return add
# def product(add):
#     mul = 1
#     while (num != 0):
#         mul *= add
#     return mul

def spy(num):
    add = 0
    mul = 1
    while (num != 0):
        add += num % 10
        mul *= add
        num //= 10
    return add % mul

num = 123
if spy(num):
    print('Spy number')
else:
    print('Not spy number')
