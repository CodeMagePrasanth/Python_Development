# WAP to print Prime Number or Not
# Ex: 5

# num = 2
# count = 0
# for i in range(1,num+1):
#     if (num %i==0):
#         count+=1
# if (count==2):
#     print('Prime Number')
# else:
#     print('Not prime number')

# break

num = 11
count = 0
for i in range(1,num+1):
    if (num % i== 0):
        count+=1
if (count==2):
    print('prime number')
else:
    print('Not prime')