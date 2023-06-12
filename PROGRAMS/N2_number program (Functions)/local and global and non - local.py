'''
# Name space in python

# Local variable

def fun():
    x =100
    print(f'Local : {x}')

x = 150
fun()
print(f'Global : {x}')

# o/p    ---- Local : 100

# Global variable :

def fun():
    print(f'Local : {x}')

x = 150
fun()
print(f'Global : {x}')

# O/P
Local : 150
Global : 150

# local and Global

def fun():
    x =24
    print(f'Local : {x}')

x = 150
fun()
print(f'Global : {x}')

# O/P --

Local : 24
Global : 150

# Error

def fun():
    x +=24
    print(f'Local : {x}')

x = 150
fun()
print(f'Global : {x}')


# O/P -----UnboundLocalError: cannot access local variable 'x' where it is not associated with a value

# global keyword using to  modify in the local space

def fun():
    global x  # O/P ---> is out both global and local same only we use global keywords
    x = 24
    print(f'Local : {x}')

global x
x = 150
fun()
print(f'Global : {x}')

# O/P

Local : 24
Global : 24

# global keyword using to  modify in the Global space

def fun():
    x = 24
    print(f'Local : {x}')

global x
x = 150
fun()
print(f'Global : {x}')

# O/P --->
Local : 24
Global : 150

'''