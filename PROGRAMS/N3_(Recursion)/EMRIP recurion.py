def rev(num,x):
    if num ==0:
        return 0
    return (num%10)* x + rev(num//10,x//10)
def prime(num,i):
    if (i == num//2+1):
        return True
    if (num%i ==0):
        return False
    return prime(num,i+1)
num = 17
l = len(str(num))-1
if (num == rev(num,10**l) and (prime(num,2)) and (prime(rev(num,10**l),2))):
    print(' EMRRIP')
else:
    print(' not EMRIP')