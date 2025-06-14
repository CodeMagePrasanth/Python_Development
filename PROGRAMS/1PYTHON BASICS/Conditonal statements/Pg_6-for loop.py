# for loop syntax: for varName in seqence:

# range
R = range(10)
for ran in R:
    print(ran)

#string
S = 'Code Mage Prasanth'
for name in S:
    print(name)

#list
L = [10,20,20,True ,False,'The Hacker',(56),[12,13,14],{12,3,4,5},{'a':12}]
for val in L:
    print(val)

#tuple
T = (98,45,   34,(89,67,),'this',10,20,20,True ,False,'The Hacker',(56),[12,13,14],{12,3,4,5},{'a':12})
for valu in T:
    print(valu)

#set
Set = {12,88,77,'code',10,20,20,True ,False,'The Hacker'}
# print(value)
for value in Set:
    pass

#dict
D = {1:'this',2:'is',3:'python','a':12}
for key in D:
    print(key)