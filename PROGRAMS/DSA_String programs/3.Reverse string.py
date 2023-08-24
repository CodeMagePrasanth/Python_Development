#3.1 'Reverse sting'
# 1 way of positive Indexing
s = 'ABC'
res = ''
for i in range(2,-1,-1):
    res += s[i]
print(res)

# Output --> CBA

#  --> 2 way of negative indexing

k = 'PYTHON'
rev = ''
for x in range(len(k)-1,-1,-1):
    rev += k[x]
print(rev)

k = 'PYTHON'
rev = ''
for x in range(len(k)-1,-1,-1):
    print(k[x],end='')

#  3 Reverse (Join)

s = 'we want mock test'
ss = ''
res =''
for i in s:
    if (i == ' '):
       res += ' '+ss+res
       ss =' '
    else:
        ss += i
res = ss +res
print(res)

# Out put ---test we  want we  mock we  want we

# 4 reverse word

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

# 3.3 wap reverse the word without spilt / join methods

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

# 3.4 reverse
s = 'we want job'
l = s.split()
res = []
for i in l:
    res.append(i[ : :-1])
print(' '.join(res))


#o/p --> ew tnaw boj

#3.5  without slicing /split methods
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