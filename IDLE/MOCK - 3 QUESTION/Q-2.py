# Overriding (Encasulation)

class a:
    def method1(self):
        print ('m1 of class A')
class b(a):
    def method1(self):
        print ('m1 of class B')

obj =b()
obj.method1()


'''
OUTPUT: m1 of class B
(here overriding)

'''

# HOW to avoid Overriding

class A:
    def method3(self):
        print ('m1 of class A')
class B(A):
    def method4(self):
        A.__init__(self)
        print ('m1 of class B')

object = B()
object.method3()

'''
OUTPUT:
m1 of class B
m1 of class A


'''

