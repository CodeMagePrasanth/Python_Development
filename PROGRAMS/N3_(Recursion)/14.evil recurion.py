def evil(num,count):
    if num ==0:
        return count
    if (num%2 == 1):
        count += 1
    return evil(num//2,count)
num= 18
if (evil(num,0)%2 == 0):
    print('evil number')
else:
    print(' not evil number')