class shape:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y

    def area(self):
        print("undefined area")

    def perimeter(self):
        print("undefind parameter")

    def move(self, x, y):
        self.x += x
        self.y += y

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color
    
class Rectangle(shape):
    def __init__(self, color, x, y, width, height):
        super().__init__(color, x, y)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
class Circle(shape):
    def __init__(self, color, x, y, radius):
        super().__init__(color, x, y)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
    
    def perimeter(self):
        return 2 * 3.14 * self.radius
    
if __name__ == '__main__':
    rectangle = Rectangle('blue', 0, 0, 5 ,3)
    circle = Circle('red', 0, 0, 5)

    print(f"rectangle area: {rectangle.area()}")
    print(f"rectangle perimeter: {rectangle.perimeter()}")
    
    print(f"Circle area: {circle.area()}")
    print(f"Circle Perimeter: {circle.perimeter()}")

    rectangle.move(2, 3)
    print(f"Rectangle position: ({rectangle.x}, {rectangle.y})")

    circle.set_color('green')
    print(f"circle color: {circle.get_color()}")