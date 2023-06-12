#  WAP to covert given string to uppercase
# note: without using in-build methods

s = 'PytHon@123'
res = ''
for i in s:
    if ('a' <= i <= 'z'):
        res += chr(ord(i)-32)
    else:
        res += i
print(res)

# Output :-- PYTHON@123

print('\n')

#  WAP to covert given string to lowercase
# note: without using in-build methods


s = 'PytHon@123'
res = ''
for i in s:
    if ('A' <= i <= 'Z'):
        res += chr(ord(i)+32)
    else:
        res += i
print(res)

# Output :-- python@123

#  WAP