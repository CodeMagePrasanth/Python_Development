n = 5
j = n//2
k = 1
for i in range(1,n+1):
    print('{}{}'.format('  '*j,'* '*k))
    j = j-1 if i < n//2+1 else j+1
    k = k+2 if i < n//2+1 else k-2