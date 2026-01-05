import math
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    def __abs__(self):
        return math.hypot(self.x, self.y)
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    def __bool__(self):
        return bool(abs(self))