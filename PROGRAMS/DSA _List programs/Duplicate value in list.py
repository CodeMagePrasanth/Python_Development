# WAP to print Duplicate values in given list?

L = [12,12,12,13,13,11]
p = []
for i in L:
    if (L.count(i)>1) and (i not in p):
        print(i)
        p.append(i)