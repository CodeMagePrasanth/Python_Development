class add:
    def __init__(self,start,end):
        self.start=start
        self.end=end

    def __iter__(self):
        return self

    def __next__(self):
        curr= self.start
        if curr > self.end:
            raise StopIteration
        self.start+=1
        return curr

ob = add(1,10)
x = iter(ob)
print(next(x))




# while True:
#     print(next(x)) # inifiate lop
