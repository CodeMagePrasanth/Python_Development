def fasci(total,n):
    if (n<10):
        if str(n) not in total:
            return False
        return True and fasci(total,n+1)
    return True
num = 327
total = str(num)+str(num*2)+str(num*3)
if fasci(total,1):
    print('fascinating')
else:
    print(' not fascinating')