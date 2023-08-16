def position(L,first,last):
    pivot = L[first]
    leftind = first+1
    rightind = last
    while True:
        while leftind <= rightind and pivot >= L[leftind]:
            leftind += 1
        while leftind <= rightind and pivot <= L[rightind]:
            rightind -= 1
        if leftind > rightind:
            break
        else:
            L[leftind],L[rightind] = L[rightind],L[leftind]
    L[first],L[rightind] = L[rightind],L[first]
def Quick(L,first,last):
    if first < last:
        p = position(L, first,last)
        Quick(L,first,p-1)
        Quick(L,p+1,last)
        
L = [6,9,0,3,7]
Quick(L,0,len(L)-1)

