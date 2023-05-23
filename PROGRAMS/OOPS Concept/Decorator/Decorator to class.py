def outer(args):
    def inner():
        n = args()
        return n
    return inner
@outer
class A:
    def __init__(self):
        print('hleo')
obj = A()