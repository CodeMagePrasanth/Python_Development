
# palindrome in string
'''

s = 'MALAYALAM'
for i in range(0, len(s)//2):
    if (s[i] != s[-i-1]):
        print('Not Palindrome')
        break
    else:
        print('Palindrome')

'''

# WAP t print number of times each character occured in a given string
'''
k = 'MALAYALAM'
pc = ''
for i in k :
    if (i not in pc):
        print('{} = {}'.format(i,k.count(i)))
    pc + i

# output -->
M = 2
A = 4
L = 2
A = 4
Y = 1
A = 4
L = 2
A = 4
M = 2

'''

#  plaindorme

# s = 'aba'
# res = ''
# for i in range(len(s)-1,-1,-1):
#     res += s[i]
# print(res)
# if (res == s):
#     print('palndotme')
# else:
#     print('not planimfopr')
#

# Sub plaindorme

s = 'malayalam'
for i in range(0,len(s)//2):
    if (s[i] != s[-i-1]):
        print(' not palindorme')
        break
else:
    print('plaindrome')

s ='PYTHON'
rev = ''
for i in range(-1,-7,-1):
    rev += s[i]
if (rev == s):
    print('Palindrome')
else:
    print('Not palindrome')