num = 135
count = (len(str(num)))
add = 0
copy = num
while (num!=0):
    rem = num % 10
    add += (rem**count)
    num = num//10
    count -= 1
if (add==copy):
    print('Disariam Number')
else:
    print('Not Disariam Number')
