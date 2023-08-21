bin = 1010
dec = 0
x = 1
while(bin!=0):
    rem = bin%10
    dec += (rem)*x
    bin//=10
    x*=2
print(dec)
'''
binary='1101'
deci =int(binary, 2)
print(deci)


o/p = 13
'''