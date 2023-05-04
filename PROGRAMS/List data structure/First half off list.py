'''
# 1. WAP to print first half off the given List:
# 1 way
A = [11,11,12,17,18,25,20,21]
print(A[ : 4 ])

# --> out put is : [11, 11, 12, 17]

# 2nd way

B = [11,11,12,17,18,25,20,21]
print(B[ : -4 :])

# --> out put is : [11, 11, 12, 17]

# 2. WAP to print second half of the given List:

C = [11,11,12,17,18,25,20,21]
print(C[ 4 :  ])

# --> out put is : [18, 25, 20, 21]

# 4. WAP to print values in even index position  the given List:

D = [11,11,12,17,18,25,20,21]
print(D[ : len(D) : 2 ])

# --> out put is : [11, 12, 18, 20]

'''
# WAP to print Even value in the given List:

E = [11,11,12,17,18,25,20,21]
res =[]
for i in E:
    if (i%2 == E[0]) :
       res +=i
print(i)
