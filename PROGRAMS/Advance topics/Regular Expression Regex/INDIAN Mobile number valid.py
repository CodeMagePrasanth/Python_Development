# How to vaild the indian Mobile number
import re
user=input(" Enter your number :")
Number=re.findall('[+]91-[6-9]\d{9}',user)
if Number :
    print('Number Vaild')
else:
    print('Number is invalid')