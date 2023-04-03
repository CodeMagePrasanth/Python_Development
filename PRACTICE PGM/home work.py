num = 1
bin = 0
x = 1
while(num !=0):
    rem = num%2
    bin += rem*x
    num //=2
    x *=10
print(bin)