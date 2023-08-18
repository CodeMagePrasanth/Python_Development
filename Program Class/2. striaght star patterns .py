l=[4,2,1,6]
for i in range(max(l)):
    for j in range(len(l)):
        if i < l[j]:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

'''
O/p -->

* * * * 
* *   * 
*     * 
*     * 
      * 
      * 
'''