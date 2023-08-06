# constructor chaining
# by using class name.

class a:
    def __init__(self):
        print('hello')
class b(a):
    def __init__(self):
        a.__init__(self)
        print('hi')
obj=b()


# o/p -->
'''
hello
hi
'''

# by using super() method
# self is not mandatory
class a:
    def __init__(self):
        print('hello')
class b(a):
    def __init__(self):
        print('hi')
        super().__init__()
obj=b()

# o/p -->
'''
hi 
hello
'''