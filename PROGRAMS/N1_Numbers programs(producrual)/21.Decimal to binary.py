# binary is 1,2,4.

dec = 10
bin = 0
x = 1
while(dec != 0):
    rem = dec % 2
    bin +=  rem * x
    dec //= 2
    x *= 10
print(bin)

'''
Decimal = 13
binary=bin(Decimal)[2:]
print(binary)

o/p = 1101

'''