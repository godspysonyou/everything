class People:
    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height

    @property
    def bmi(self):
        return self.weight / (self.height ** 2)

p1 = People('egon', 75, 1.85)
print(p1.bmi)

import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius**2

    @property
    def perimeter(self):
        return 2*math.pi*self.radius


c = Circle(10)
print(c.radius)
print(c.area)
print(c.perimeter)

