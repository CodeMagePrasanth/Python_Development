def rev(num,x):
    if num ==0:
        return 0
    return (num%10)* x + rev(num//10,x//10)
def prime(num,i):
    if (i == num//2+1):
        return True
    if (num%i ==0):
        return False
    return prime(num//10,i+1)
num = 14
if rev(num,10**(len(str(num)))-1) and prime(num,2):
    print('palyprime')
else:
    print(' not palyprime')