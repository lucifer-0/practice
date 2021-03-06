import math


class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self


    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)


    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self


    def __mul__(self, other):
        return Point(self.x * other, self.y * other)


    def __imul__(self, other):
        self.x *= other
        self.y *= other
        return self
        

    def __truediv__(self, other):
        return Point(self.x / other, self.y / other)


    def __itruediv__(self, other):
        self.x /= other
        self.y /= other
        return self


    def __floordiv__(self, other):
        return Point(self.x // other, self.y // other)


    def __ifloordiv__(self, other):
        self.x //= other
        self.y //= other
        return self

    
    def distance_from_origin(self):
        return math.hypot(self.x, self.y)


    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


    def __repr__(self):
        return "Point({0.x!r}, {0.y!r})".format(self)


    def __str__(self):
        return "({0.x!r}, {0.y!r})".format(self)


    

    
