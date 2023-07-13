n = 7
num = 97
for i in range (0,n):
    for j in range(0,i+1):
        ch = chr(num)
        print(ch,end='')
        num+=1
    print()
# output -->
'''
a
bc
def
ghij
klmno
pqrstu
vwxyz{|

'''