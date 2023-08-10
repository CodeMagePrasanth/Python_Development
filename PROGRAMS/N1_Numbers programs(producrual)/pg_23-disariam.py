num = 135
add = 0
count = (len(str(num)))
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
