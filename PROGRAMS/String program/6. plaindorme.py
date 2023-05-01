
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