'''
print('Right Triangle number')

n = 5
p =1
for i in range(n):
    for j in range(n-i):
        print(' ', end = ' ')
    for j in range(i+1):
        print(p, end =' ')
    print()
'''
'''
Output :--

1 
1 1
1 1 1
1 1 1 1
1 1 1 1 1

'''
'''
Decreasing order number in print number

1
2 2
3 3 3
4 4 4 4
5 5 5 5 5

n = 5
p = 1
for i in range(n):
    for j in range(n - i):
        print(' ', end=' ')
    for j in range(i + 1):
        print(p, end=' ')
    p += 1
    print()
'''
n = 5
p = 1
for i in range(n):
    for j in range(n - i):
        print(' ', end=' ')
    for j in range(i + 1):
        print(p, end=' ')
    p += 1
    print()

