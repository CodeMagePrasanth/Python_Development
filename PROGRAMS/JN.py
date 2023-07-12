'''
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input("enter THe number : ").strip())
if 1 <= n <= 100:
    if n %2 == 1:
        print('Weird')
    elif n % 2 == 0 and 2 <= n <= 5 :
        print('Not Weird')
    elif n % 2 == 0 and 6 <= n <= 20:
        print('weird')
    elif n % 2 == 0 and n >= 20:
        print('Not Weird')

#2
if __name__ == '__main__':
    a = int(input("enter the : "))
    b = int(input("enter : " ))
    print(a + b)
    print(a - b)
    print(a * b)

__main__':
    n = int(input("ente : "))
    for i in range(n):
            print(i**2)

if __name__ == '__main__':
    n = int(input(" enter :"))
    for i in range(1,n+1):
        print(i,end='')
'''
'''
def is_leap(year):
    leap = False
    if year % 4 != 0 and year % 400 != 0 and year % 100 != 0 :
        return True

year = int(input(" entet : "))
print(is_leap(year))
'''
def is_leap(year):
    leap = False
    if year % 100 == 0:
        if year % 400 == 0:
            return True 
        if year % 4 == 0:
                return True        
    return leap

year = int(input(" : "))
print(is_leap(year))
