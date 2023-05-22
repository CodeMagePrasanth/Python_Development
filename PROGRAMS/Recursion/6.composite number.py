def prime(num,i):
    if i == num+1:
        return 0
    return (1 if (num%i == 0) else 0) + prime(num,i+1)

num = 6
if (prime(num,1) > 2):   # ---> if more the 2 factors is composite
    print('Composite')
else:
    print('not Composite')