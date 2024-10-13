import math

# Base class - Shape
class Shape:
    def area(self):
        """This method should be overridden by derived classes."""
        raise NotImplementedError("Subclasses must override the area method.")

# Derived class - Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        """Initialize the rectangle's dimensions."""
        self.length = length
        self.width = width

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.length * self.width

# Derived class - Circle
class Circle(Shape):
    def __init__(self, radius):
        """Initialize the circle's radius."""
        self.radius = radius

    def area(self):
        """Calculate and return the area of the circle using π * radius^2."""
        return math.pi * (self.radius ** 2)


from polymorphism_demo import Shape, Rectangle, Circle

def main():
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()
