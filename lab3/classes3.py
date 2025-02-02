class Shape:
    def area(self):
        """Returns the default area, which is 0."""
        return 0
class Rectangle(Shape):
    def __init__(self, length, width):
        """Initializes the Rectangle with given length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.length * self.width
shape = Shape()
print("Shape area:", shape.area())  

rectangle = Rectangle(4, 6)
print("Rectangle area:", rectangle.area())  