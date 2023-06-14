n = 5
f,s = 0,1
for i in range(n):
    print(f)
    f,s=s,f+s
print('\n')

n = 5
f,s = 0,1
for i in range(n):
    curr = f
    f,s=s,f+s
print(curr)