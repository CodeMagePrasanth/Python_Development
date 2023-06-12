l = 'a a  a b'
d = ''
for i in l:
    if l.count(i)>1 and i not in d:
        d += i
print(d)
