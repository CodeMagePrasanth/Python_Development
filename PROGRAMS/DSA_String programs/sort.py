s = 'I2S QUES4TION EX3AM THI1S'
d = {}
l= s.split()
for word in l:
    num = ''
    ss = ''
    for ch in word:
        if ('0' <= ch <= '9'):
            num += ch
        else:
            ss += ch
    d[int(num)]= ss
print(d)

# Output --> {2: 'IS', 4: 'QUESTION', 3: 'EXAM', 1: 'THIS'}

s = 'I2S QUES4TION EX3AM THI1S'
d = {}
l= s.split()
for word in l:
    num = ''
    ss = ''
    for ch in word:
        if ('0' <= ch <= '9'):
            num += ch
        else:
            ss += ch
    d[int(num)]= ss

n = ''
l = list(d.keys())
l.sort()
for i in l:
    n += d[i]+' '
print(l)
print(n)
print(n.strip())

# output :-- THIS IS EXAM QUESTION