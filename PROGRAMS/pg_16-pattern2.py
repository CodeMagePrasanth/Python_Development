# To print 1 to 5 star
# Ex : usin for loop

#     *
#    **
#   ***
#  ****
# *****

# for loop

n = 5
for a in range(1,n+1):
    print('  ' * (n-a), '@ ' * (a))

# onther for loop ways

n = 5
for A in range(0,n+1):
    print('{}{}'.format('  ' * (n-A) , '$ ' * (A)))

# reverse order

n=7
for b in range(5,n+1,-1):
    print(' ' * (n-b),'#' * (b))

# whhile loop
n = 5
a = 1
while (a != n):
    print('{}{}'.format('  ' * (n-a), '! ' * (a)))
    a +=1

# reverse order while loop

k = 0
b = 5
while (b != k):
    print('{}{}'.format('  ' * (k-b),'* ' * (b)))
    b -= 1

n = 5
a = n
while (a != 0):
    print('{}{}'.format('  ' * (n-a),'% ' * (a)))
    a -= 1