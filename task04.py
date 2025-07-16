class Shape:
    def area(self):
        raise NotImplementedError("Bu metod hali chaqirilmagan.")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height
    
def main():
    shapes = [
        Circle(radius=5),
        Rectangle(width=4, height=6),
        Triangle(base=3, height=7)
    ]

    for shape in shapes:
        print(f"Area: {shape.area()}")

if __name__ == "__main__":
    main()