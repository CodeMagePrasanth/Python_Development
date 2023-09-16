# To count the Alphabets. digits, Special charaters, Space, Vowels

import re

S ='P1ytH2on Jspiders @123#'

Alpha = re.findall('[a-zA-Z]',S)
print(Alpha)
# o/p--> ['P', 'y', 't', 'H', 'o', 'n', 'J', 's', 'p', 'i', 'd', 'e', 'r', 's']
digits = re.findall('\d',S)
print(digits,len(digits))
# o/p-->  ['1', '2', '1', '2', '3'] 5
SPC = re.findall('\w',S)
print(SPC,len(SPC))
# o/p--> ['P', '1', 'y', 't', 'H', '2', 'o', 'n', 'J', 's', 'p', 'i', 'd', 'e', 'r', 's', '1', '2', '3'] 19

Space = re.findall('\s',S)
print(Space)
print(len(Space))
# o/p--> [' ', ' ']
# 2

Vowels = re.findall('[aeiouAEIOU]',S)
print(Vowels)
print(len(Vowels))
# ['o', 'i', 'e', 'I']
# 4
