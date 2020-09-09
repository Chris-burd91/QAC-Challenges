

class Rectangle:

    def __init__(self,h,l):
        self.height = h
        self.length = l

    def rectangle_area(self):
        return self.length*self.height

    
create_Rectangle = Rectangle(3, 6)

print(create_Rectangle.rectangle_area())