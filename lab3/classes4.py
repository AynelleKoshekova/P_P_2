import math

class Point:
    def __init__(self, x, y):
        """Initializes the Point with given coordinates (x, y)."""
        self.x = x
        self.y = y

    def show(self):
        """Displays the coordinates of the point."""
        print(f"Point coordinates: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        """Moves the point to new coordinates (new_x, new_y)."""
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        """Computes and returns the Euclidean distance to another Point."""
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

# Example usage:
p1 = Point(3, 4)
p2 = Point(6, 8)

p1.show()  # Expected: (3, 4)
p2.show()  # Expected: (6, 8)

print("Distance between p1 and p2:", p1.dist(p2))  # Expected: 5.0

p1.move(10, 12)
p1.show()  # Expected: (10, 12)
