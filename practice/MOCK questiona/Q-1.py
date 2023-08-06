# WAP to justify the mro() method by on example

class a:
    print('this is A')
class b(a):
    print('this is B')
class c(a):
    print('this is C')
class d(b,c):
    print('this is D')

obj = d()
print(d.mro())
print(d.__mro__)

'''
OUTPUT
QUESTION\QUESTION 1.py
this is A
this is B
this is C
this is D
[<class '__main__.d'>, <class '__main__.b'>, <class '__main__.c'>, <class '__main__.a'>, <class 'object'>]
(<class '__main__.d'>, <class '__main__.b'>, <class '__main__.c'>, <class '__main__.a'>, <class 'object'>)
'''
