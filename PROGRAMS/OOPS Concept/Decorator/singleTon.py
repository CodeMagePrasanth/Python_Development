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
