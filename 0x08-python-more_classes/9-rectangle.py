#!/usr/bin/python3
class Rectangle:
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle instance with optional width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter method to retrieve the width of the rectangle."""
        return self._width

    @width.setter
    def width(self, value):
        """Setter method to set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self._width = value

    @property
    def height(self):
        """Getter method to retrieve the height of the rectangle."""
        return self._height

    @height.setter
    def height(self, value):
        """Setter method to set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self._height = value

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self._width * self._height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        return 2 * (self._width + self._height) if self._width > 0 and self._height > 0 else 0

    def __str__(self):
        """Return a string representation of the rectangle using print_symbol."""
        if self._width == 0 or self._height == 0:
            return ""
        
        rectangle_str = ""
        for _ in range(self._height):
            rectangle_str += str(self.print_symbol) * self._width + "\n"
        
        return rectangle_str.rstrip()

    def __repr__(self):
        """Return a string representation of the rectangle for recreation."""
        return f"Rectangle({self._width}, {self._height})"

    def __del__(self):
        """Print a message when an instance of Rectangle is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the rectangle with the bigger or equal area."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 = rect_1.area()
        area_2 = rect_2.area()

        return rect_1 if area_1 >= area_2 else rect_2

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle instance with width == height == size."""
        return cls(size, size)
