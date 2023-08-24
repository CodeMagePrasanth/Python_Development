#  WAP to prin unique value in list

L = [12,12,42,2,3,2]
p = []
for i in L:
    if L.count(i) == 1:
        print(i)

# --> Output is : 42,3