from abc import ABC, abstractmethod
class Animal(ABC):
    @staticmethod
    def Speak(self):
        pass
    def Walk(self):
        print('Walk with 4 legs')
class Dog(Animal):
    def Speak(self):
        print('BOW BOW')
class Cat(Animal):
    def Speak(self):
        print('meow meow')
class Cow(Animal):
    def Speak(self):
        print('amnbaa')
ob1 = Dog()
ob2 = Cat()
ob3 = Cow()

ob1.Speak()
ob2.Speak()
ob3.Speak()

ob1.Walk()
ob2.Walk()
ob3.Walk()

'''
Output
BOW BOW
meow meow
amnbaa
Walk with 4 legs
Walk with 4 legs
Walk with 4 legs
'''
