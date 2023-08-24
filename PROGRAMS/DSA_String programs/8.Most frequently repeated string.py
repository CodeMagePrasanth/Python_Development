# most frequently character in sting
s = 'python cython'
h = 0
for i in s:
    if s.count(i) > h:
        h = s.count(i)
l = []
for i in s:
    if s.count(i) == h and i not in l:
        l.append(i)
print(i)

