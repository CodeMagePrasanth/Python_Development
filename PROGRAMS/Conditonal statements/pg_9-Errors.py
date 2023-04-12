# loop errors:
# for and ehilw loops syntax error

# index error:
# for
# a = [6,5,3,6,3,6,5]
# for i in range(7):
#     print(a[6])

# while
# a = [1,2,3]
# while (a !=5):
#     print(a)
#     a[3] -=2

# zero division error
# while
# a = 0
# while (a<10):
#     print(10/a)
#     a +=1

# for

for n in range(10/0):
    print(n)