class Rectangle:
#constructor
    def __init__(self,height,width):
        self.height=height
        self.width=width
    def set_dimensions(self,height,width):
        self.height=height
        self.width=width
    def area(self):
        return self.height*self.width
    def perimeter(self):
        return 4*(self.height+self.width)
rect1=Rectangle(4,3)
#rect1.set_dimensions(4,3)
print("the height and width are",rect1.height,rect1.width)
print(rect1.area())
print(rect1.perimeter())

""" height_input = float(input("Enter the height of the rectangle: "))
width_input = float(input("Enter the width of the rectangle: "))

# Set the dimensions using the input values
rect1.set_dimensions(height_input, width_input) """