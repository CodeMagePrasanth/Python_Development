# prime number
# Defition of prime number:- if given number divisible with 1 and itself . then it is prime number
# Like we take one number 7, it is prime number or not
# Every number divisible with 1 so we start with 2 and -1(7-1) 6
# 2/7,3/7,4/7,5/7,6/7.
# if divied any number its not not prime number
# Ex:- 1 is not prime number (in condition is prime number two factors only prime number)
#
# num = 1
# count = 1
# for i in range(1,num+1):
#     if num%i==0:
#         count +=1
# if count==2:
#     print(' prime number')
# else:
#     print(' not prime number')
#
# num = 13
# while (num>9):
#     add = 0
#     while (num!=0):
#         add += (num%10)**2
#         num//=10
#     num =add
# if num==1:
#     print('hap')
# else:
#     print('not happ')

# num=3
# i =1
# while i**2 <=num+1 :
#     if i**2 == num+1:
#         print('sunny')
#         break
#     i+=1
# else:
#     print('not sunny')
num = 3
for i in range(0, num):
    for j in range(0, num-i-1):
        print(" ",end=" ")
    for j in range(0, i*2+1):
        print("*", end=" ")
    print()
for i in range(1, num):
    for j in range(0, i):
        print(" ",end=" ")
    for j in range(0, (num-i)*2-1):
        print("*", end=" ")
    print()