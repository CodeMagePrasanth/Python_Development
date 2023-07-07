num = [3,8,4,1,0,3,5,1,9]
count = 0
res=[]
for i in num:
    for k in range(1,i+1) :
        if i%k ==0:
            count+=1
    if count==2:
        res.append(i+1)
        count-=2
    elif count>=2 or count<=1:
        res.append(i)
        count-=count
print(res)