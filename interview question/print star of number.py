# l = [1,4,5,3]

L = [1,4,5,3]
print(L)
for i in L:
    if L.count(i):
        print('{}'.format('*'*i))

'''        
# Output
[1, 4, 5, 3]
*
****
*****
***
'''


L = [1,4,5,3]
print(L)
for i in L:
    if L.count(i):
        print('{}'.format('*'*i))
