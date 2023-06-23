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
L= []
X = [i for i in range(1,102) if i%2 == 0 ]
print(X)
