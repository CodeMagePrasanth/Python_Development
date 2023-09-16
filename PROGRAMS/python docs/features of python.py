# Croos-paltform
import os
os_name=os.name
print(f'runnung on {os_name} os')

# o/p--> runnung on nt os(Window new techonolgy)

# Scripting language
# import shutil
#
# source_file = "data.txt"
# destination_folder = "backup/"
# shutil.copy(source_file, destination_folder)


#  functional programming language:

def greet(name):
    print('Hello ' +  name)

greet('Alice')

# o/p--> Hell0 Alice

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says woof!")

my_dog = Dog("Buddy")
my_dog.bark()

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)
