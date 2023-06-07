s = 'we want mock test'
l = s.split()
res = ''
for i in l:
    res += i[ : : -1]+' '
print(res)
print(res.strip())

# Output --> ew tnaw kcom tset

s = 'we want mock test'
l = s.split()
res = []
for i in l:
    res.append (i[ : : -1])
print(' '.join(res))

# Output --> ew tnaw kcom tset

# wap reverse the word without spilt / join methods

s = 'we want job'
ss = ''
res = []
for i in s:
    if i != ' ':
        ss += i
    else:
        res.append(ss[ : : -1])
        ss = ' '
res.append(ss[ : :-1])
print(res)

# o/p -->['ew', 'tnaw ', 'boj ']

# reverse
s = 'we want job'
l = s.split()
res = []
for i in l:
    res.append(i[ : :-1])
print(' '.join(res))


#o/p --> ew tnaw boj

# without slicing /split methods
s = 'we want job'
ss =''
res = ''
for i in s:
    if i == ' ':
        res = ss+' '+res
        ss=''
    else:
        ss+=i
res = ss+' '+res
print(res)

# o/p ---> job want we