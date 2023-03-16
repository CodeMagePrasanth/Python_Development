'''
year = 2020
if (year%4==0 and year%100==0 and year%400==0):
    print('Leap Year')
else:
    print('Not Leap Year')

'''
year = int(input("Enter  a year:"))
if (year % 4==0):
    if (year % 100==0):
        if (year % 400==0):
            print(year,'Leap year')
        else:
            print(year,'not Leap year')
    else:
        print(year,'Not leap year')
else:
    print(year,'Not leap Year')