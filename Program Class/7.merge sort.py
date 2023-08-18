'''
# first  we have to divide to main logic,
# 1 --> divide the list into two part. so in the end we have three list right.

#     --> arr, left,right
# 2 --> merge the two list into one listed...
#    --> And sort the list by compare the left and right
#    --> and major one step is in the is logic ' every elements is not sorted so that'
#     ---> we have write one conditions for "Leftout value copy form Right arr and Left arr"

'''
# 1

def divide(arr):
    if len(arr) <= 1: # cause we have to divide untill one element
       # print(arr) # 0/p --> [18][15][17][12][19][14][13] altast we get this elements sepatetally
       return
    left = arr[ 0 : len(arr)//2 ]
    right = arr[ len(arr)//2 : ]
    divide(left)
    divide(right)
    merge(arr,left,right)
'''
# arr = [18, 15, 17, 12, 19, 14, 13]
# divide(arr)
#1  print(arr) # o/ p --> [18, 15, 17, 12, 19, 14, 13]
'''
# 2  this part is combaring the Left and Right and sorted list

def merge(arr, L , R ):
    ind = li = ri = 0
    while li < len(L) and ri < len(R) :
        if R[ri] < L[li]:
            arr[ind] = R[ri]
            ind += 1
            ri += 1
        else:
            arr[ind] = L[li]
            ind += 1
            li += 1
       # we don't no how many or which left so that we have right one condtion for "leftout values"
    while li < len(L):  #this part is some how missing elements we need to copt that "leftout values"
        arr[ind] = L[li]
        ind += 1
        li += 1
    while ri < len(R):
        arr[ind] = R[ri]
        ind += 1
        ri += 1

arr = [18, 15, 17, 12, 19, 14, 13]
divide(arr)
print(arr)

# O/P --> [12, 13, 14, 15, 17, 18, 19]