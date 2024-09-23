
# class keyword defines a class
from typing import Any


class Car:
    # in java you'd declare all attributes here

    # constructor
    def __init__(self, make, model) -> None:
        self.odometer = 0
        self.make = make
        self.model = model
        odometer = 0 # this is not an attribute (no "self.")

    # a method
    def drive(self, distance: float) -> None:
        self.odometer += distance

my_car = Car('lexus', 'is300')
my_car.drive(100)

# subclass this way
class Toyota(Car):

    def __init__(self, model) -> None:
        super().__init__('Toyota', model)



# make a class that behaves like a "callable" (i.e. a function)
class MyFunc:

    def __init__(self, num1) -> None:
        self.num1 = num1
    
    def __call__(self, num2) -> Any:
        return self.num1 + num2

mf = MyFunc(5)
print(mf(3))