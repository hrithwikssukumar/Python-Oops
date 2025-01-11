class Rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self. breadth = breadth

    def get_area(self):
        area = self.length * self.breadth
        return area
    def get_perimeter(self):
        perimeter = 2*(self.length + self.breadth)
        return perimeter
rectangle_1 = Rectangle(4,5)
rectangle_1.get_area()
print(rectangle_1.get_area())

rectangle_1 = Rectangle(4,5)
rectangle_1.get_perimeter()
print(rectangle_1.get_perimeter())