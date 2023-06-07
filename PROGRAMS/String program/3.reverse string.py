# 'Reverse sting'
# 1 way of positive Indexing
s = 'ABC'
res = ''
for i in range(2,-1,-1):
    res += s[i]
print(res)

# Output --> CBA

# 2 way of negative indexing

k = 'PYTHON'
rev = ''
for x in range(len(k)-1,-1,-1):
    rev += k[x]
print(rev)