# List
# WAP to print highest value in given list?

L = [12,452,2455,25,23]
high = L[0]
for i in range(1,len(L)):
    if L[i] > high :
        high = L[i]
print(high)

# --> Output is : 2455

# WAP to print highest value in given list?

L = [12,452,2455,25,23]
high = L[0]
for i in range(1,len(L)):
    if L[i] < high :
        high = L[i]
print(high)

# --> Output is : 12

# WAP to print sum of value in given list?

# L = [12,42,5,26]
# sum = 0
# for i in L:
#     sum += i
# print(sum)

# --> Output is : 85

#  another one easy way to sum value:

L = [12,42,5,26]
print(f'sum : {sum(L)}')

# --> Output is : sum : 85

# WAP to print maximum and Minimum value in given list?

L = [12,42,5,26]
print(f'Maximum : {max(L)}')
print(f'Minimum : {min(L)}')

# --> Output is : Maximum : 42 ,Minimum : 5
