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