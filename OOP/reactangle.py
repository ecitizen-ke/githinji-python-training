#!/usr/bin/env python3

class Rectangle:
    # Class attributes to store default length and width
    length = 0
    width = 0

    # The @classmethod decorator in Python is used to define a method that operates on the class itself 
    # rather than on instances of the class. When a method is decorated with @classmethod, 
    @classmethod
    def set_dimensions(cls, length, width):
        cls.length = length
        cls.width = width

    @classmethod
    def area(cls):
        return cls.length * cls.width

# Set the dimensions
Rectangle.set_dimensions(5, 4)

# Calculate and print the area
print("Area of rectangle:", Rectangle.area())