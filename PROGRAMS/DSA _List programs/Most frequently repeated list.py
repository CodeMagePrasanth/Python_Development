L = [12,13,12,12,3,12,13,2,3]
p = 0
for i in L:
    if (L.count(i) > p):
        p = L.count(i)
K = []
for i in L:
    if (L.count(i) == p) and (i not in L):
        print(i)
        L.append(i)