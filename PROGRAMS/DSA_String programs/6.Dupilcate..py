l = 'a a  a b'
d = ''
for i in l:
    if l.count(i)>1 and i not in d:
        d += i
print(d)

# 2

# S = 'MALAYALAM'

# pc = ''
# for i in S:
#     if (i not in pc):
#         print('{} = {}'.format(i,S.count(i)))
#     pc += i
#
S = 'MALAYALAM'
pc = []
for i in S:
    if (i not in pc):
        print('{} = {}'.format(i,S.count(i)))
    pc += i

# O/P --> M = 2 A = 4 L = 2 Y = 1