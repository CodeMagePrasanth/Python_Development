# # n = 5
# # j = n//2
# # k = 1
# # for i in range(1,n+1):
# #     print('{}{}'.format('  '*j,'* '*k))
# #     j = j-1 if i < n//2+1 else j+1
# #     k = k+2 if i < n//2+1 else k-2
#
# a,b,c,d =(1,2,3,4,5)
# print(a,b,c,d)


# l = [i**2 for i in range(1,2000)]
# G = (i**2 for i in range(1,2000))
# print(l.__sizeof__())
# print(G.__sizeof__())

# l = [1,2,3,4]
# k =[]
# for i in range(0,len(l)):
#     for j in range(i+1,len(l)+1):
#         k.append((l[i:j]))
# print(k)
# L= []
# X = [i for i in range(1,102) if i%2 == 0 ]
# print(X)

# a = 15
# b = 20
# if a >b:
#     smaller=b
# else:
#     smaller=a
# for i in range(1,smaller+1):
#     if (a % i ==0 and b%i==0):
#         hcf = i
# print(f"Hcf of {a} and {b} is {hcf}")

# n = 10
# count=0
# for i in range(2,n+1):
#     is_prime =True
#     for j in range(2,i):
#         if i%j==0:
#             is_prime=False
#             break
#     if is_prime:
#         print(i,end=',')
#         count +=1
# print(f"total number is : {count}")

# s = '  copy assignment'
# newStr=''
# for i in range(len(s)):
#     if i==0 or s[i-1] == ' ':
#         newStr += s[i].upper()
#     else:
#         newStr += s[i]
# print(newStr)

# import re
# s ='hai python'
# x=re.match('h',s)
# print(x)