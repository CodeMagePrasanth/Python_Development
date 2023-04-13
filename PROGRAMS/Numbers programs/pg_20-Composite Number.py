# Logic 1
# we are division

# num = 14
# count = 0
# for a in range(1,num+1):
#     if (num%a==0):
#         count+=1
# if (count>2):
#     print('composite')
# else:
#     print('not composite')

# Logic 2

num = 14
for i in range(2, num//2+1):
    if num % i == 0:
        print('composite')
        break
else:
    print('Not Composite')
