# WAP to print this patten
# 1 2 3 4 5
# 2 1 2 3 4
# 3 2 1 2 3
# 4 3 2 1 2
# 5 4 3 2 1
<<<<<<< HEAD
#
# n = 5
# a = 0
# for i in range(1,6,):

num = 153
copy = num
count = len(str(num))
add = 0
while ( num != 0 ):
    rem = num%10
    add = add + (rem**count)
    num = num//10
if (copy == add):
    print('armstrong')
else:
    print('not armstrong')
=======

n = 5
a = 0
for i in range(1,6,):
>>>>>>> dcb00c5d389ebb6289484380afc87a832f55e4d2
