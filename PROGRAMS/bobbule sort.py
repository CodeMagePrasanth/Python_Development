
L = [54,63,3,6,2,66]
for k in range(len(L)-1):
    for m in range(len(L)-1-k):
        if L[m]>L[m+1]:
            L[m],L[m+1]=L[m+1],L[m]
    print(L)
print(L)