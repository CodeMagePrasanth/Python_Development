def arm(num,p):
    if num == 0:
        return 0
    return (num%10)**p + arm(num//10,p)


num = 10
# if num == arm(num, len(str(num))):
#     print('ArmStrong Number')
# else:
#     print(' not ArmStrong Number')

print('Armstrong number' if num == arm(num, len(str(num))) else 'not ArmStrong Number')