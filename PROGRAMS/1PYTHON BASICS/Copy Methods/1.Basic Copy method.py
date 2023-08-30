# Basic of Copy method in python
# by using "=" assenments operator
list1=[[1,2,3,4],['a','b','c','d']]
list2=list1
print(list1)#[[1, 2, 3, 4], ['a', 'b', 'c', 'd']]
print(list2)#[[1, 2, 3, 4], ['a', 'b', 'c', 'd']]
list1[0][1]=9
print(list1)#[[1, 9, 3, 4], ['a', 'b', 'c', 'd']]
print(list2)#[[1, 9, 3, 4], ['a', 'b', 'c', 'd']]

print(id(list1) == id(list2))# True
