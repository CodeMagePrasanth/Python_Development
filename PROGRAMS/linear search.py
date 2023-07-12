
L = [12,3,43,535,67,75,46,-4,49,-11,(12)]
L.sort()
print(L)
user = int(input('enter value to search :'))
for a in range(len(L)):
    if L[a]==user:
        print(a)
        break
else:
    print(-1)

'''
binary search 
L = [8,4,435,35,2,674,84,884]
L.sort()
user = int(input('Enter values : '))
slow = 0
high = len(L)-1
while low <= high:
    mid = (low + high)//2
    if user > L[mid]:
        low = mid+1
    elif user < L[mid]:
        high = mid-1
    elif user == L[mid]:
        print(mid)
        break
else:
    print(-1)
            
'''
