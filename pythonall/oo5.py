from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius * self.radius

    def perimeter(self):
        return 2 * pi * self.radius


circle = Circle(10)
area1 = circle.area()
per1 = circle.perimeter()
print(area1, per1)

class Ring:
    def __init__(self,radius_outside, radius_inside):
        self.outside_circle = Circle(radius_outside)
        self.inside_circle = Circle(radius_inside)

    def area(self):
        return self.outside_circle.area() - self.inside_circle.area()

    def perimeter(self):
        return self.outside_circle.perimeter() + self.inside_circle.perimeter()

ring = Ring(10, 5)
print(ring.perimeter())
print(ring.area())