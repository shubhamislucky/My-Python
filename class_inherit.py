# In this module we will learn about Inheritance
import class2

class ElectricCar(class2.Car):
    """ Represents aspects of a car, specific to electric vehicles. """

    def __init__(self, make, model, year):
        """ Initialize attributes of parent class. """
        super().__init__(make, model, year)


my_tesla = ElectricCar('tesla', 'model s', 2017)
print(my_tesla.get_descriptive_name())
