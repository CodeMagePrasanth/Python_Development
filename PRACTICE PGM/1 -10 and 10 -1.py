# n = 11
# for i in range(1,11):
#      print(i , end='')
#      print(' ',n-i)

# a,b=1,10
# while (a !=11):
#     print(a,b)
#     a+=1
#     b-=1

a,b = 1,10
for i in range(a,b):
    print('{}{}'.format(a,b))
    a+=1
    b-=1