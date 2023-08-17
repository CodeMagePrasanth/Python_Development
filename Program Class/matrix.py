l=[[1,2,3],[4,5,6],[7,8,9]]
# for i in range(0,3):
#     for j in range(2,-1,-1):
#         print(l[j][i],end=' ')
#     print()

# for i in range(2,-1,-1):
#     for j in range(0,3):
#         print(l[j][i],end=' ')
#     print()


add=0
add1=0
for i in range(0,3):
    for j in range(0,3):
        if i==0:
            add+=l[i][j]
        if i==2:
            add1+=l[i][j]
print(add+add1)
