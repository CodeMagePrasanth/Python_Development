# n=int(input('ENTER THE VALUE'))
# k = 1
# s = 0
# for i in range(n,0,-1):
#     print(' '*s,end='')
#     for j in range(1,i+1):
#         print(k,end=' ')
#         k+=1
#     print()
#     s +=1
# '''
# ENTER THE VALUE5
# 1 2 3 4 5
#  6 7 8 9
#   10 11 12
#    13 14
#     15
# '''

# # 2
# n = int(input('Enter the value : '))
# s = 0
# for i in range(n,0,-1):
#     print('{}{}{}'.format(' '*(n-i),'*'*i,'*'*(i-1)))
'''
*****
 ***
  *
'''
# 3

# n = 5
# k = 1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(k,end='')
#         k+=1
#     print()
# '''
# 1
# 23
# 456
# 78910
# 1112131415
# '''
#
# #
# n = 5
# k = 1
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(k,end='')
#         k+=1
#     print()
# '''
# 1 2 3 4 5
# 6 7 8 9
# 10 11 12
# 13 14
# 15
# '''

n = 4
m = 1
for i in range(0,n):
    for j in range(0,n-i-1):
        print(' ',end='')
    for k in range(0,i*2+1):
        print(m,end='')
    print()
    m +=1
'''
   1
  222
 33333
4444444
'''
# 5
n = 4
m = 1
for i in range(n,0,-1):
    for j in range(0,n-i+1):
        print(' ',end='')
    for k in range(0,i*2-1):
        print(m,end='')
    print()
    m +=1
'''
 1111111
  22222
   333
    4

'''

# n = 5
# m = 1
# for i in range(1,n+1):
#     print('{}{}{}'.format(' '*(n-i),'m'*i,'m'*(i-1)))

# n = 5
# for i in range(n,0,-1):
#     print('{}{}{}'.format(' '*(n-i),'*'*i,'*'*(i-1)))