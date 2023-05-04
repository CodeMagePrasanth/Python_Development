# WAP to print Duplicate values in given list?

L = [10,10,10,20,30,40,50,50]
K = []
for i in L:
    if i not in K:
        K.append(i)
print(K)


