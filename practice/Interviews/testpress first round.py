'''
s ='codecode'
rev_string = ''
for word in range(len(s)-1, -1, -1):
    rev_string += s[word]
print(rev_string)


def prime_number(number):
    count = 0
    for i in range(1,number+1):
        if (number % i == 0):
            count += 1
    if (count == 2):
        return 'Yes'
    return 'No'
number = 3
print(prime_number(number))
'''
# num =988
# rev=0
# while num != 0:
#     rem = num%10
#     rev = (rev*10)+rem
#     num//=10
# print(rev)

# def Number(value):
#     Reversed_number = 0
#     while value != 0 :
#         Reversed_number = Reversed_number*10 + (value%10)
#         value //= 10
#     return Reversed_number
# value=988
# print(Number(value))

# def largest_number(List):
#     List = sorted(map(str,List), reverse = True)
#     return ''.join(List)
#
# L =[54, 546, 548, 60]
# print(largest_number(L))


# L = [54, 546, 548, 60]
# high = L[0]
# k = []
# for i in range(1,len(L)):
#     if (L[i] > high):
#         high=L[i]
#         k = high
#     else:
#         if (L[i] < high):
#             k = L[i]
# print(high)

# L = [54, 546, 548, 60]
# high=L[0]
# for i in (1,len(L)):
#     if (L[i] > high):
#         high = L[i]
# print(high)

# L = [54, 546, 548, 60]
# maximum = max(L)
# minimum = min(L)
# print(maximum,minimum)

