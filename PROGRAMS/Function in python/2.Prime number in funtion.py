'''
#  Prime number
# Q1--> WAP to Check given number is prime or not
#  Note:- if given number is prime funtion should return True otherwise return False

def prime(n):
    count = 0
    for a in range (1,n+1):
        if (n % a == 0):
            count +=1
    if (count == 2):
        return True
    return False

print(prime(3))
print(prime(14))
print(prime(11))

'''

'''
#  Prime number
# Q2  --> WAP to print prime number  40 to 80

def primenum(num):
    count = 0
    for i in range (1,num+1):
        if (num%i == 0) :
            count +=1
    return count == 2

for i in range (40,80):
    if (primenum(i)):
        print(i)
'''

'''
# Q3  --> WAP to print prime number  40 to 80

def primenum(num):
    count = 0
    for i in range (1,num+1):
        if (num%i == 0) :
            count +=1
    return count == 2

for i in range (70,20,-1):
    if (primenum(i)):
        print(i)
'''


#  prime number
# Q5---> to prime first 5 prime number

def prime_count(num):
    count = 0
    for i in range(1, num+1):
        if (num % i == 0):
            count += 1
    return count == 2

i = 1
count= 1
while (count != 4):
    if (prime_count(i)):
        print(i)
        count+=1
    i+=1
'''
def prime_count(num):
    count = 0
    for i in range(1, num+1):
        if (num % i == 0):
            count += 1
    return count == 2

for i in range (70,20,-1):
    if (prime_count(i)):
        print(i)

print('\n')

i = 1
count= 1
while (count != 6):
    if (prime_count(i)):
        print(i)
        count +=1
    i +=1

print('\n')

for i in range (70,20,-1):
    if (prime_count(i)):
        print(i)

'''