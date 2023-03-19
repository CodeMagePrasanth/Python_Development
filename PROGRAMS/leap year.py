year = 10
if (year % 100 == 0 and year % 400 == 0):
    print('Leap Year')
elif (year % 4 == 0 and year % 100 !=0):
    print(' Leap year')
else:
    print('Not leap year')