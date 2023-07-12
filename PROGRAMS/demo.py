num = [9,3,8,4,1,0,3,5,1,9]
res= []
count = 0
for a in num:
    for j in range(1,a+1):
        if a%j == 0:
            count+=1
            
if count==2:     
    for l in num:
        num+=1
        res.append(num)
else:
    res.append(num)
print(res)

        
            
