'''
Short definition:
Interpolation search in Python is a search algorithm that finds the position of a target value in a sorted list by estimating its location based on the values at the ends of the search interval.

Steps:
1. Accept a sorted list (or array) and a target value as input.
2. Set the left and right boundaries of the search interval, initially the first and last indices of the list.
3. While the left boundary is less than or equal to the right boundary and the target value is within the range of the values at the boundaries:
   - Estimate the position of the target value using interpolation formula:
     `pos = left + ((target - arr[left]) * (right - left)) // (arr[right] - arr[left])`
   - Compare the value at the estimated position with the target value.
   - If they match, return the position.
   - If the value at the estimated position is greater than the target value, update the right boundary to be the position - 1.
   - If the value at the estimated position is less than the target value, update the left boundary to be the position + 1.
4. If the target value is not found after the loop, return -1 to indicate that it is not present in the list.

Note: Interpolation search works best on uniformly distributed sorted lists. If the data is not uniformly distributed, it may not provide significant improvements over binary search.
'''
L = [2,5,14,65,66,90]
low = 0
high= len(L)-1
user = 5
while low <= high and L[low] <= user <= L[high]:
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
