def outer(args):
    def Inner(a,b):
        if a>b:
            args(a,b)
        else:
            args(b,a)
    return Inner
@outer
def add(a,b):
    print(a + b)
add(1,9)