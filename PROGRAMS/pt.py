'''num = [9,3,8,4,1,0,3,5,1,9]
count = 0
res=[]
for i in num:
    for k in range(1,i+1) :
        if i%k ==0:
                count+=1
    if count==2:
        res.append(i+1)
    else:
        print('m')
'''
num= 9384
res=[]
count=0
for i in range(1,num//10):
    print(i)
    if num%i==0:
        count+=1
    num//=10
if count==2:
    res.append(num)
else:
    print('h')
