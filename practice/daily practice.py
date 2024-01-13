num = 5

fact = 1

for  i in range(1,num+1):
        fact*=i
print(fact)


def fact(num):
    fact = 1
    for i in range(1,num+1):
        fact*=i
    return fact

print(fact(5))

def fact(num):
    if num == 0:
        return 1
    return (num%10) * fact(num-1)

print(fact(5))
