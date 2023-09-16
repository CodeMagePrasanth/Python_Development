
L=['[11,12,13]','[1,2,3]','[200,5]']
x = []
for i in L:
    print(i)
    x.append(eval(i))
print(x)
'''

L=['[11,12,13]','[1,2,3]','[200,5]']
x = []
for i in L:
    z=[]
    c=''
    for j in i:
        if j.isdigit():
            c+=j
        else:
            if len(c) >0:
                z.append(int(c))
                c=''
    x.append(z)
print(x)
            
'''
# example of eval funtion
#  it take a single argument and return evaluating the expression
x = 10
y = 20
expression = "x + y"
result = eval(expression)
print(result)  # Output will be 30
