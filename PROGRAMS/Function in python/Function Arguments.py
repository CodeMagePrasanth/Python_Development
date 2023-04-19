'''

there are 5 function arguments
1. Positional aguments
3. Default arguments
4. varibale arguments
4.1 Variable length keywords arguments
4.2 Variable length non - keywords arguments
'''
'''
# positional arguments

def positional_arg(name,id,city):
    print(f' A : {name}')
    print(f' B : {id}')
    print(f' C : {city}')

positional_arg('prasanth',12,'benguluru')
print('\t')
positional_arg(12,'prasanth','benguluru')
'''
'''
## keyword arguments:

def keyword_arg(name,age,gender):
    print(f'Name :- {name}')
    print(f'Age :- {age}')
    print(f'Gender :- {gender}')

keyword_arg(name = 'prasanth',age = 20 ,gender = 'Male') # age 20
print('\t')
keyword_arg('prasanth',18,'male')  # age 18
'''
'''
# Default arguments

def default_arg(name = None,age = None, gender = None):
    print(f'Name :- {name}')
    print(f'Age :- {age}')
    print(f'Gender :- {gender}')
    
default_arg()
print('\t')
default_arg( name = 'prasanth',age = '25' ,gender = 'Male')

'''
'''
# Variable arguments
# there are two
# 1. Variable length keyword arguments
# 2. Variable length Non - keyword arguments

def var_keyword_arg(*args):
    print('gender')
    print('hellow world')
    print(f' agrs : {args}')
var_keyword_arg(4,43)
'''
# Variable lenth non-keyword arguments
def var_non_keyword_arg(**kwarg):
    print('gender')
    print('hellow world')
    print(f'kwargs : {kwarg}')
var_non_keyword_arg(name = 'prasanth',college = 'paavai engineering clg')