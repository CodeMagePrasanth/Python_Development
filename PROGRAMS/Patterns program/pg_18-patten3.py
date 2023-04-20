#  - - *
#  - * * *
#  * * * * *
#  - * * *
#  - - *

# n=5 (iteration) ,
# space 2 , '*' 1 , i - 1
# space 1 , '*' 3 , i - 3
# space 0 , '*' 5 , i - 5
# space 1 , '*' 3 , i - 3
# space 2 , '*' 1 , i - 1

n = 5
m = n//2
k = 1
for a in range(1,n+1):
    print('{}{}'.format(' ' * (m),'*' * (k)))
    m = m-1 if a<n//2+1 else m+1
    k = k+2 if a<n//2+1 else k-2
