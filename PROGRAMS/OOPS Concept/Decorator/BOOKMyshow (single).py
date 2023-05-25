# def outer(arg):
#     d = {}
#     def inner():
#         if arg not in d:
#             d[arg] = arg()
#         return d[arg]
#     return inner
# @outer
# class JohnWick1:
#     def __init__(self):
#         self.tickets = 100
#     def booking(self):
#         print('welcome to world films')
#         n = int(input('Enter number of Tickets :'))
#         if self.tickets >= n:
#             self.tickets = self.tickets - n
#             print('tickets booked successfully')
#         else:
#             print('Tickets is not avaliable')
# def BookMyShow():
#     obj = JohnWick1()
#     obj.booking()
#
# BookMyShow()
# BookMyShow()
# BookMyShow()

def outer(arg):
    d = {}
    def inner():
        if arg not in d:
            d[arg] = arg()
        return d[arg]
    return inner
@outer
class JohnWick1:
    def __init__(self):
        self.tickets = 100
    def booking(self):
        print('welcome to JHON Wick 1')
        n = int(input('Enter number of Tickets :'))
        if self.tickets >= n:
            self.tickets = self.tickets - n
            print('tickets booked successfully')
        else:
            print('Tickets is not avaliable')
class JohnWick2:
    def __init__(self):
        self.tickets = 100
    def booking(self):
        print('welcome to JHON Wick 2')
        n = int(input('Enter number of Tickets :'))
        if self.tickets >= n:
            self.tickets = self.tickets - n
            print('tickets booked successfully')
        else:
            print('Tickets is not avaliable')
class JohnWick3:
    def __init__(self):
        self.tickets = 100
    def booking(self):
        print('welcome to JHON Wick 3')
        n = int(input('Enter number of Tickets :'))
        if self.tickets >= n:
            self.tickets = self.tickets - n
            print('JHON WICK 3 tickets booked successfully')
        else:
            print('Tickets is not avaliable')
def BookMyShow():
    print('''1.JOHN WICK 1
    2.JOHN WICK 2
    3.JOHN WICK 3''')
    option =int(input('Choose the one movie : '))
    if (option == 1):
        obj = JohnWick1()
        obj.booking()
    elif (option == 2):
        obj = JohnWick2()
        obj.booking()
    elif (option == 3):
        obj = JohnWick3()
        obj.booking()
    else:
        print('sorry only option')
BookMyShow()
BookMyShow()
BookMyShow()


'''
OUTPUT: 
1.JOHN WICK 1
    2.JOHN WICK 2
    3.JOHN WICK 3
Choose the one movie : 3
welcome to JHON Wick 3
Enter number of Tickets :100
JHON WICK 3 tickets booked successfully
1.JOHN WICK 1
    2.JOHN WICK 2
    3.JOHN WICK 3
Choose the one movie : 2
welcome to JHON Wick 2
Enter number of Tickets :100
tickets booked successfully
1.JOHN WICK 1
    2.JOHN WICK 2
    3.JOHN WICK 3
Choose the one movie : 1
welcome to JHON Wick 1
Enter number of Tickets :100
tickets booked successfully
'''