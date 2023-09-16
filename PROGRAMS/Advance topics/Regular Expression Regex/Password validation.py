# how to valid password
import re
user=input("Enter the password")
Pass=re.findall('[a-zA-Z]+(\w+d+|\d+\w+)',user)
if Pass and len(user)>=8 and ' 'not in user:
    print('vaild')
else:
    print('NOt valid')