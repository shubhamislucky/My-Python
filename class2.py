# classes continued
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

    def update_odometer(self,reading):
        """
        Set the odometer reading to a given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if reading > self.odometer_reading:
            self.odometer_reading = reading
        else:
            print("You can's roll back an odometer !")

    def increment_odometer(self,increment):
        """ Add the given amount to the odometer reading. """
        self.odometer_reading += increment


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# Modifying attribute values
my_new_car.odometer_reading = 100
my_new_car.read_odometer()

# Modifying attribute's value through a method
my_new_car.update_odometer(130)
my_new_car.read_odometer()

# Incrementing odometers value by function
my_new_car.increment_odometer(50)
my_new_car.read_odometer()
