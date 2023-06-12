
print(' Left Triangle number ')

n = 5
p = 1
for i in range(n):
    for j in range(1,i+1):
        print('-', end = ' ')
    for j in range(i,n):
        print(p, end = ' ')
    p += 1
    print()


'''
Output :--
Left Triangle Star

1 1 1 1 1 
- 2 2 2 2 
- - 3 3 3 
- - - 4 4 
- - - - 5 
'''
