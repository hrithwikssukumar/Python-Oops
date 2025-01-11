class Circle:
    pi=3.14 #class object attribute

    def __init__(self,radius=7):
        self.radius = radius
    def get_circumference(self):
        circum = 2*self.pi*self.radius
        return circum
    def get_area(self):
        area = self.pi*self.radius*self.radius
        return area


circle_1 = Circle()
circle_1.get_circumference()
print(circle_1.get_circumference())

circle_1 = Circle()
circle_1.get_area()
print(circle_1.get_area())      
        