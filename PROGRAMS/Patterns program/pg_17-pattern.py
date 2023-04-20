#  half diamind pattern program

# *
# **
# ***
# **
# *

# to print using 'for' loop
# way1
# for i in range(1,4):
#     print('*' * (i))
# for j in range(2,0,-1):
#     print('*' * (j))

# 2nd way

n = 5
b = 1
for a in range(1,n+1):
    print('* ' * b)



# 3rd way

# n = 5
# b = 1
# for a in range(1,n+1):
#     print('* ' * b)
#     b = b+1 if a<n//2+1 else b-1
