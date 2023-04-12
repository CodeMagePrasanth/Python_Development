bin = 1010
dec = 0
x = 1
while(bin!=0):
    rem = bin%10
    dec += (bin%10)*x
    bin//=10
    x*=2
print(dec)