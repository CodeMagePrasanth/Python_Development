'''binary search'''
L = [2,5,14,65,66,90]
low = 0
high= len(L)-1
user = int(input('enter values :'))
while low <= high and low <= user <= high:
    pos = int(low+((high-low)/(L[high]-L[low]))*(user-L[low]))
    if user < L[pos]:
        high=pos-1
    elif user > L[pos]:
        low = pos+1
    elif user == L[pos]:
        print(pos)
        break
else:
    print(-1)
