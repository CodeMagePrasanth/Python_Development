# Rectangle patterns

for i in range(5):
    for j in range(6):
        print('*',end=' ')
    print()

# Increasing triangle pattern
a = 5
for i in range(1,a+1):   # onther ways  (1,a+1),
    for j in range(i):
        print('*',end=' ')
    print()

# Decreasing triangle

a = 6
for i in range(a):
    for j in range(i,a):
        print('*',end=' ')
    print()

# right sided triangle

a = 5
for i in range(a):
    for j in range(i,a):
        print(' ',end=' ')
    for j in range(i+1):
        print('$',end=' ')
    print()


a = 5
for i in range(a):
    for j in range(i+1):
        print('*',end=' ')
    for j in range(i,a):
        print(' ',end=' ')
    print()
