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

7

