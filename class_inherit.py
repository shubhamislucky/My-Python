# In this module we will learn about Inheritance


class Car():
    """ A simple attempt to represent a car. """

    def __init__(self, make, model, year):
        """ Initialize attributes to describe a car. """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """ Return a neatly formatted descriptive name. """
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """ print a statement showing the car's mileage. """
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, reading):
        """
        Set the odometer reading to a given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if reading > self.odometer_reading:
            self.odometer_reading = reading
        else:
            print("You can's roll back an odometer !")

    def increment_odometer(self, increment):
        """ Add the given amount to the odometer reading. """
        self.odometer_reading += increment


class ElectricCar(Car):
    """ Represents aspects of a car, specific to electric vehicles. """

    def __init__(self, make, model, year):
        """ Initialize attributes of parent class. """
        super().__init__(make, model, year)


my_tesla = ElectricCar('tesla', 'model s', 2017)
print(my_tesla.get_descriptive_name())
