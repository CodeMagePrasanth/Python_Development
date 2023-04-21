print("Left Triangle Star")

# n = 5
# for i in range(n):
#     for j in range(1,i+1):
#         print('-',end = ' ')
#     for j in range(i,n):
#         print('*', end = ' ')
#     print()

'''
Output :-- Left Triangle Star

* * * * * 
- * * * * 
- - * * * 
- - - * * 
- - - - * 

'''

n = 5
p = 1
for i in range(n):
    for j in range(1,i+1):
        print('-',end = ' ')
    for j in range(i,n):
        print(p, end = ' ')
    p+=1
    print()

