class Rectangle:
    area = 0
    perimeter = 0
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return (f"Площа {self.calculate_area()} та периметр {self.calculate_perimeter()}. Ширина - {self.width} та висота - {self.height}.")

