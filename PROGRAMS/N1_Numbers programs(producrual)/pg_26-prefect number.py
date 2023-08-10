num = 6
sum = 0
for i in range(1, num):
    if num % i == 0:
        sum += i
if sum == num:
    print('Perfect Number')
else:
    print('Not Perfect Number')

LL=int(input('Enter number : '))
UL=int(input('Enter number : '))
for n in range(LL,UL+1):
    sum = 0
    for i in range(1,n//2+1):
        if n%i==0:
            sum+=i
    if n== sum:
        print(n)

'''
Enter number : 1
Enter number : 10
6
'''