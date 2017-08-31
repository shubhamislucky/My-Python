# in this module we will learn about classes

class Dog():
    """ A simple attempt to model a dog """

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name + " is now sitting.")

    def rollover(self):
        print(self.name + " rolled over.")

# Making an Instance from a class
my_dog = Dog('Julie', 5)
print(my_dog.__doc__)

# Accessing attributes
print("My dog's name is " + my_dog.name + ".")
print("My dog is " + str(my_dog.age) + " years old.")

# Calling methods
my_dog.sit()
my_dog.rollover()

# Creating multiple instances of class
my_dog = Dog('Julie', 5)
your_dog = Dog('Willie', 4)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()

print("Your dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()
