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