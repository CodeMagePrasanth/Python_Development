def fib(n):
    f,s=0,1
    for i in range(0,n):
        yield f
        f,s=s,f+s
g = fib(3)
try :
    while True:
        print(next(g))
except StopIteration:
    print('complete...')