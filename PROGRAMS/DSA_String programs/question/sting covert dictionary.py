# WAP to covert string to Dictionary give string

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

# WAP to covert string to Dictionary give string
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
