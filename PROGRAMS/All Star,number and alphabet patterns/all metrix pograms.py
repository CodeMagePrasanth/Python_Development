# All the metrix programs

#1 3X3 metrix

L=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(0,3):
    for j in range(0,3):
        print(L[i][j],end=' ')
    print()
'''
o/p 
1 2 3 
4 5 6 
7 8 9 
'''
#2 90^ right side

n=3
f=0
s=0
for i in range(n):
    for j in range(n):
        print([j][i],end='')
    print()