# WAP to print first 5 fibonacci number
class fib:
    def __init__(self,total):
        self.f=0
        self.s=1
        self.total=total
    def __iter__(self):
        return self
    def __next__(self):
        rect= self.f
        self.f,self.s=self.s,self.f+self.s
        self.total+=1
        return rect
ob = fib(1)
x = iter(ob)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
