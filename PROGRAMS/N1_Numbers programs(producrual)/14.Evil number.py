num = 9
count = 0
while num != 0:
    if num%2 == 1:
        count+= 1
    num//= 2
if (count%2==0):
    print('Evil number')
else:
    print('Not Evil Number')