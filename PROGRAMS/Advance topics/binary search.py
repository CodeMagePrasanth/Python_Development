'''
Short definition:
Binary search in Python is an efficient search algorithm that finds the position of a target value in a sorted list by repeatedly dividing the search interval in half.

Steps:
1. Accept a sorted list (or array) and a target value as input.
2. Set the left and right boundaries of the search interval, initially the first and last indices of the list.
3. While the left boundary is less than or equal to the right boundary:
   - Calculate the middle index of the current search interval.
   - Compare the value at the middle index with the target value.
   - If they match, return the middle index.
   - If the middle value is greater than the target value, update the right boundary to be the middle index - 1.
   - If the middle value is less than the target value, update the left boundary to be the middle index + 1.
4. If the target value is not found after the loop, return -1 to indicate that it is not present in the list.
'''

j = [1,2,3,4]
j.sort()
val = 4
low = 0
high=len(j)-1
while low <= high:
    mid = (low + high)//2
    if val > j[mid]:
        low = mid+1
    elif val < j[mid]:
        high = mid-1
    elif val == j [mid]:
        print(mid)
        break
else:
    print(-1)
