num = [3]
res=[]
while num!=1:
    count=0
    for a in num:
        for b in range(1,num+1):
            if a % b ==0:
                count+=1
