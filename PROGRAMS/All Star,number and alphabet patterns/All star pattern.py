# 1

for i in range(1,6):
        print('* '*i)

'''
*
* *
* * *
* * * *
'''

# 2

for i in range(5,0,-1):
        print('* '*i)
'''
* * * * *
* * * *
* * *
* *
*
'''

# 3

n = 5
for i in range(1,n+1):
  print('{}{}'.format('  '*(n-i),'* '*i))
'''
    *
  * *
* * *
'''

# 4

n = 5
for i in range(5,0,-1):
        print('{}{}'.format('  '*(n-i),'* '*(i)))

'''
* * *
  * *
    *
'''

# 5

n = 5
for i in range(1,n+1):
        print('* '*i)
for j in range(4,0,-1):
        print('* '*j)

'''
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*

'''

# 6

n = 5
for i in range(1,n+1):
        print('  '*(n-i),'* '*i)
for j in range(4,0,-1):
        print('  '*(n-j),'* '*(j))

'''
         *
       * *
     * * *
   * * * *
 * * * * *
   * * * *
     * * *
       * *
         *
'''
# 7

'''
for i in range(1,6):
    print('* '*i )
*
* *
* * *
* * * *
* * * * *
'''
'''
for i in range(5,0,-1):
    print('* '*i)

* * * * * 
* * * * 
* * * 
* * 
* 
'''
'''
n = 5
for i in range(1,n+1):
    print('{}{}'.format('- '*(n-i),'* '*(i)))

        * 
      * * 
    * * * 
  * * * * 
* * * * * 
'''
'''
n = 5
for i in range(5,0,-1):
    print('{}{}'.format('* '*(i),'- '*(n-i)))

* * * * * 
* * * * - 
* * * - - 
* * - - - 
* - - - - 
'''
'''
n = 5
for i in range(1,n+1):
    print('{}{}{}'.format('  '*(n-i),'* '*(i),'* '*(i-1)))

        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 
'''
'''
n = 5
for i in range(5,0,-1):
    print('{}{}{}'.format('  '*(n-i),'* '*(i),'* '*(i-1)))

* * * * * * * * * 
  * * * * * * * 
    * * * * * 
      * * * 
        *
'''
'''
n = 5
for i in range(1,n+1):
    print('{}{}{}'.format('  '*(n-i),'* '*i,'* '*(i-1)))
for i in range(4,0,-1):
    print('{}{}{}'.format('  '*(n-i),'* '*(i),'* '*(i-1)))

        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 
  * * * * * * * 
    * * * * * 
      * * * 
        * 
'''
'''

for i in range(1,4):
    print('* '*i)
for j in range(2,0,-1):
    print('* '*j)

* 
* * 
* * * 
* * 
* 
'''
# for i in range(1,4,-1):
#     print('* '*i)
# for j in range(2,0,-1):
#     print('* '*j)

# ternary opertor
'''

n = 5
j = 1
for i in range(1,n+1):
    print('* '*(j))
    j = j+1 if i<n//2+1 else j-1

* 
* * 
* * * 
* * 
* 

'''

'''
n = 5
j = 2
k = 1
for i in range(1,n+1):
    print('{}{}'.format('  '*(j),'* '*(k)))
    j = j-1 if i < n//2+1 else j+1
    k= k+1 if i < n//2+1 else k-1

    * 
  * * 
* * * 
  * * 
    *
'''
'''
n = 5
j = n//2
k = 1
for i in range(1,n+1):
    print('{}{}'.format('  '*(j),'* '*(k)))
    j = j-1 if i < n//2+1 else j+1
    k= k+2 if i < n//2+1 else k-2

    *
  * * *
* * * * *
  * * *
    * 

'''