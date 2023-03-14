### CONDITIONAL STATEMENTS (if, else, elif).###

#if when given condition is True control goes to inside if block code.

# if examples

age=48
if age>18:
    print('you are an adult')

##if when given condition is False control goes to inside if block code.

# else examples

age=16
if age>18:
    print('you are adult')
else:
    print("you are not an adult")

### elif exampels

age = 18
if age < 18:
    print("You are a minor")
elif age >= 18 and age < 65:
    print("You are an adult")
else:
    print("You are a senior citizen")

### few examples

if 4>=2:
    print('hi')
else:
    print('heloo')

#Ex-1

s='abcde'
ch='X'
if (ch is s):
    print("Yes,{}".format(s.index(ch)))
else:
    print('No')

#Ex_2

s='ABCDE'
ch='D'
if (ch in s):
    print("Yes,{}".format(s.index(ch)))
else:
     print('No')

#Ex_3

s="PYTHON"
ch="T"
if (ch is not s):
    print("Yes,{}".format(s.index(ch)))
else:
    print("No")