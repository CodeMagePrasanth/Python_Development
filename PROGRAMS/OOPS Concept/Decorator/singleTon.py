'''
def outer(arg):
    d = {}
    def inner():
        if (arg not in d):
            d[arg] = arg()
        return d[arg]
    return inner
@outer
class A:
    def __init__(self):
        print('hello world')
obj = A()
print(obj)

'''
# book my show

# 1 create empty dictonary
def singleton(cls):
    d={}
    def inner():
        if (cls not in d): #logic here weather object is there not
            d[cls] = cls()
    return inner()
@singleton
class jhonwick:
    def __init__(self):
        self.t=420

    def booking(self):
        print('booking your tickts')
        n =int(input('enter your count : '))
        if (self.t >= n):
            self.t = self.t -n
            print('Your tickets booked successfully')
        else:
            print('House full')
@singleton
class jhonwick2():
    def __init__(self):
        self.t=420

    def booking(self):
        print('booking your tickts')
        n = int(input('enter your count : '))
        if (self.t >= n):
            self.t = self.t - n
            print('Your tickets booked successfully')
        else:
            print('House full')


def Bookmyshow():
    print('Choose your fav : \n 1.jhonwick\n 2.jhonwick2')
    option= int(input('Enter your number :'))
    if option == 1:
        ob = jhonwick()
        ob.booking()
    elif option==2:
        ob = jhonwick2()
        ob.booking()
    else:
        print('only listed moives')
while True:
    Bookmyshow()