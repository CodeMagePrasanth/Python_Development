num = 192
sum = str(num*1)+str(num*2)+str(num*3)
for i in range(1,10):
    if str(i) not in sum:
        print('Not Fasinating')
        break
else:
    print('Fasinating')
