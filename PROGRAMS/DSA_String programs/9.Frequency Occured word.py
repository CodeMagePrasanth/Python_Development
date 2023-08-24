# most frequently word in given string
s = 'Engineering the the '
p = s.split()
k = 0
for i in p:
    if(p.count(i) > k):
        k = s.count(i)
L = []
for i in p:
    if (p.count(i) == k) and (i not in L):
        print(i)
        L.append(i)

# Output is = the
