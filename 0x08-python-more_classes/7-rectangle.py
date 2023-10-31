#!/usr/bin/python3


"""
This module defines a Rectangle class that represents a rectangle shape.
"""

class Rectangle:
    """
    Rectangle class defines a rectangle by its width and height.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    # Rest of the class implementation...

    def __del__(self):
        """
        Performs cleanup when the instance is deleted.
        Prints a farewell message.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
