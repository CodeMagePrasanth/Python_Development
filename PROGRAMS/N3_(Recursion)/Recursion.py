# ---> what is recursion and examples
'''
 Repeat Itself
 --> a function we put in side of the same function

'''
# infinite time 'hii helo' the output
# end of the output recursion
'''
def fun():
    print('hii heloo')
    fun()


fun()
'''
# ---> Output : is infinite time hii helloo and
# N3_(Recursion) Error : maximum N3_(Recursion) deepth exceeded while pickling on object.

# Ex :--- WAP to print 1 to 10

def number(n):
    print(n)
    if n==-10:
        return
    number(n-1)


number(-1)