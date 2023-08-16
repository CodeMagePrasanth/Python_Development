def quick_sort(L):
    if len(L) <= 1:
        return L
    pivot = L[0]
    left = [num for num in L[1 : ] if num <= pivot]
    right = [num for num in L[1 : ] if num > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

L = [18, 14,20,25,40,11,9,15]
print(quick_sort(L))