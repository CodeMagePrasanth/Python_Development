#  WAP to covert given string to uppercase
# 1.1 note: without using in-build methods

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

# 1.2  WAP to covert given string to lowercase
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
print()

# 1.3 WAP Swap case

s = 'PytHon@123'
res = ''
for i in s:
    if ('A' <= i <= 'Z'):
        res += chr(ord(i)+32)
    elif ('a' <= i <= 'z'):
        res += chr(ord(i) - 32)
    else:
        res += i
print(res)



# 1.4 Question
# s = "Be ConSisTent"
# res = ''
# for i in s:
#     if ('A' <= i <= 'Z'):
#         res += chr(ord(i)+32)
#     elif ('a' <= i <= 'z'):
#         res += chr(ord(i)-32)
#     else:
#         res += i
# print(res)


# 1.6 reverse  it


s = "Be ConSisTent"
res = ''
for i in s:
    if ('A' <= i <= 'Z'):
        res += chr(ord(i) + 32)
    elif ('a' <= i <= 'z'):
        res += chr(ord(i) - 32)
    else:
        res += i
for i in range(-1,-12,-1):
    res += s[i]
    print(res)

# question 2
# 1.7 WAP to covert string to Dictionary give string

s = 'I2S QUES4TION EX3AM THI1S'
d = {}
for word in s.split():
    num =''
    ss = ''
    for ch in word:
        if ('0' <= ch <= '9'):
            num += ch
        else:
            ss += ch
    d[int(num)] = ss
print(d)

# output --> {2: 'IS', 4: 'QUESTION', 3: 'EXAM', 1: 'THIS'}

# 1.8 WAP to covert string to Dictionary give string
# and sort method using

s = 'I2S QUES4TION EX3AM THI1S'
d = {}
l = s.split()
for word in l:
    num = ss = ''
    for ch in word:
        if ('0' <= ch <= '9'):
            num += ch
        else:
            ss += ch
    d[int(num)] = ss
print(d)
N=''
m = list(d.keys())
m.sort()
for i in m:
    N += d[i]+' '
print(N)
print(N.strip())

# output -->
#  {2: 'IS', 4: 'QUESTION', 3: 'EXAM', 1: 'THIS'}
#  THIS IS EXAM QUESTION
