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