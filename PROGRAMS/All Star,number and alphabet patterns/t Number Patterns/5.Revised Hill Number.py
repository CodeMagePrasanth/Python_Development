print(' Revised Hill Number')


n = 5
p = 1
for i in range(n):
    for j in range(i+1):
        print(' ', end = ' ')
    for j in range(i+1,n+1):
        print(p, end = ' ')
    for k in range(n-i-1):
        print(p, end = ' ')
    print()


'''
 Revised Hill Number
  1 1 1 1 1 1 1 1 1 
    1 1 1 1 1 1 1 
      1 1 1 1 1 
        1 1 1 
          1 

'''
'''
n = 5
p =1
for i in range(n):
    for j in range(i+1):
        print(' ', end = ' ')
    for j in range(i+1,n+1):
        print(p, end = ' ')
    for k in range(n-i-1):
        print(p, end = ' ')
    p+=1
    print()
'''
'''
 Revised Hill number

  1 1 1 1 1 1 1 1 1 
    2 2 2 2 2 2 2 
      3 3 3 3 3 
        4 4 4 
          5 
          

'''
'''
n = 5
p =1
for i in range(n):
    for j in range(i+1):
        print(' ', end = ' ')
    for j in range(i+1,n+1):
        print(p, end = ' ')
    p+=1
    for k in range(n-i-1):
        print(p, end = ' ')
    p +=1
    print()
    
output:--

 Revised Hill Number

  1 1 1 1 1 2 2 2 2 
    3 3 3 3 4 4 4 
      5 5 5 6 6 
        7 7 8 
          9 
'''