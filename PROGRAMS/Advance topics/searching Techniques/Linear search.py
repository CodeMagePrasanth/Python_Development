'''
Short definition:
Linear search in Python is a basic search algorithm that sequentially checks each element in a list until it finds a match or reaches the end of the list.

Steps:
1. Accept a list (or array) and a target value as input.
2. Start at the beginning of the list.
3. Iterate through each element of the list.
4. Compare the current element with the target value.
5. If a match is found, return the index of the element.
6. If the end of the list is reached without finding a match, return -1 to indicate that the target value is not present in the list.
'''

k = [9,4,10,44,6,3]
k.sort()
val = int(input('ENTER THE VALUES : '))
for a in range(len(k)):
    if k[a] == val:
        print(a)
        break
else:
    print(-1)