print('Hill Number')

'''
n = 5
p =1
for i in range(n):
    for j in range(n-i):
        print(' ', end = ' ')
    for j in range(i+1):
        print(p, end = ' ')
    for j in range(i):
        print(p, end = ' ')
    print()
'''
'''
Hill Number
          1 
        1 1 1 
      1 1 1 1 1 
    1 1 1 1 1 1 1 
  1 1 1 1 1 1 1 1 1 

'''

n = 5
p =1
for i in range(n):
    for j in range(n-i):
        print(' ', end = ' ')
    for j in range(i+1):
        print(p, end = ' ')
    for j in range(i):
        print(p, end = ' ')
    p +=1
    print()

'''
Hill Number
          1 
        2 2 2 
      3 3 3 3 3 
    4 4 4 4 4 4 4 
  5 5 5 5 5 5 5 5 5 

'''