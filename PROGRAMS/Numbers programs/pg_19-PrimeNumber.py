# WAP to print Prime Number or Not
# Ex: 5

num = 2
count = 0
for i in range(1,num+1):
    if (num %i == 0):
        count += 1
if (count == 2):
    print('Prime Number')
else:
    print('Not prime number')

# break

numb = 11
count = 0
for i in range(1,numb+1):
    if (numb % i== 0):
        count+=1
if (count==2):
    print('prime number')
else:
    print('Not prime')

n = 2
if (n>1):
    for i in range(2,n//2):
        if (n % i== 0):
            print(' n prime')
            break
    else:
        print('prime')
else:
    print(' n prime')

