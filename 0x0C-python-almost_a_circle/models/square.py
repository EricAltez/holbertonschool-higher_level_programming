#!/usr/bin/python3
"""
Square module
"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """Square class"""

    @property
    def size(self):
        """ getter for size """
        return self.width

    @size.setter
    def size(self, size):
        """ setter for size """
        self.width = size
        self.heigt = size

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str overriding """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

