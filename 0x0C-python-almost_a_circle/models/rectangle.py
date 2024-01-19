#!/usr/bin/python3
"""Module for Rectangle class"""
from models.base import Base


"""
Define a subclass Rectangle that inherits from Base
"""
class Rectangle(Base):
    """Using class constructor initialise class atrributes"""
    def __init__(self, width, height, x=0, y=0, id=None):

        """Initialize a new Rectangle instance"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be > 0")
        else:
            self.__x = x

        if not isinstance(x, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be > 0")
        else:
            self.__y = y


        super().__init__(id)

    @property
    def width(self):
        """Get width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width of rectangle and add validation logic"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get width of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set width of rectangle and add validation logic"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get width of rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set width of rectangle and add validation logic"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get width of rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set width of rectangle and add validation logic"""
        if not isinstance(value, int):
            raise TypeError("Y must be an integer")
        if value < 0:
            raise ValueError("Y must be >= 0")
        self.__y = value

    def area(self):
        """Computes area of this rectangle"""
        return self.__width * self.__height

    def display(self):
        """Displays and prints an instance"""
        s = '\n' * self.__y + \
            (' ' * self.__x + '#' * self.__width + '\n') * self.__height
        print(s, end='')

    def __str__(self):
        """__str__ method returns string info about this rectangle"""
        return '[{}] ({}) {}/{} - {}/{}'.format(type(self).__name__, self.id, self.x, self.y, self.width, self.height)

    def update(self, *args):
        """Add update method to assigns an argument"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]

