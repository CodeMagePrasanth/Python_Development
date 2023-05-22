def disarium(num,p):
    if num==0:
        return 0
    return (num%10) ** p + disarium(num//10,p-1)

num = 135
if num == disarium(num,len(str(num))):
    print('disarium number')
else:
    print(' not disarium  number')
#
# print('Armstrong number' if num == arm(num, len(str(num))) else 'not ArmStrong Number')