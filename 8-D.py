import math

# Base class
class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


# Circle subclass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius


# Triangle subclass
class Triangle(Shape):
    def __init__(self, a, b, c, height):
        self.a = a
        self.b = b
        self.c = c
        self.height = height

    def area(self):
        return 0.5 * self.a * self.height

    def perimeter(self):
        return self.a + self.b + self.c


# Square subclass
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side


# Create objects
circle = Circle(5)
triangle = Triangle(3, 4, 5, 4)
square = Square(6)

# Display results
print("Circle Area:", circle.area())
print("Circle Perimeter:", circle.perimeter())

print("Triangle Area:", triangle.area())
print("Triangle Perimeter:", triangle.perimeter())

print("Square Area:", square.area())
print("Square Perimeter:", square.perimeter())