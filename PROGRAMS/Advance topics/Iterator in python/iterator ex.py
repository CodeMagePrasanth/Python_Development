# L = [10,12]
# x = iter(L)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))

# class a:
#     def __init__(self,start,end):
#         self.start = start
#         self.end = end
#     def __iter__(self):
#         return self
#     def __next__(self):
#         curr = self.start
#         if curr > self.end:
#             raise StopIteration
#         self.start += 1
#         return curr
# obj = a(1,10)
# x = iter(obj)
# while True:
#     print(next(x))

#
# def spy(num):
#     a=0
#     m=1
#     while(num!=0):
#         a+=num%10
#         m*=a
#         num//=10
#     return a%m
# num = 24
# if spy(num):
#     print('spy')
# else:
#     print('not spy')