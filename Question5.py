import math
class Shape:
    def __init__(self,name):
        self.name=name

    def cal_area(self):
        raise ValueError("This function cannot be implemented here")

    def cal_perimeter(self):
          raise ValueError("this function can not be called")
    def __str__(self):
        '''string representation of shape'''
        return f'{self.name}' 
         
class Circle(Shape):
    '''circle shape'''
    def __init__(self,radius,name='circle'):
        super().__init__(name)
        self.radius=radius  
        
    def cal_area(self):
        return math.pi * self.radius**2
    
    def cal_perimeter(self):
        return 2 * math.pi * self.radius
    
    def __str__(self):
        return f"This is {super().__str__()} whose Radius: {self.radius}m \n Area: {self.cal_area():.1f} meter square"


class Rectangle(Shape):
    '''Rectangle shape'''

    def __init__(self,width,length,name="rectangle"):
        
        super().__init__(name)
        self.width=width
        self.length=length
               
        
    def cal_area(self):   
        return self.length *self.width

    def cal_perimeter(self):
        return 2 * (self.length +self.width)
    
    def __str__(self):
        return f"This is {super().__str__()} whose Width: {self.width} and length: {self.length}\n Area: {self.cal_area()} meter square"

class Triangle(Shape):
    '''Triangle shape'''

    def __init__(self,s1,s2,s3,name="triangle"):
        super().__init__(name)  
        self.s1=s1
        self.s2=s2
        self.s3=s3
         

    def cal_area(self):
       # Using Heron's formula
        sum = self.cal_perimeter() / 2
        return math.sqrt(sum * (sum - self.s1) * (sum - self.s2) * (sum - self.s3))
    
    def cal_perimeter(self):
        return self.s1 + self.s2 + self.s3
    
    def __str__(self):
        return f"This is{ super().__str__()}\n whose Sides are: {self.s1}m, {self.s2}m, {self.s3}m\n Area: {self.cal_area():.1f} meter square"


'''TLet's take example'''
if __name__ == "__main__":
    shapes = [
        Circle(5),
        Rectangle(4, 6),
        Triangle(3, 4, 5)
    ]
    
    for shape in shapes:
        print(shape)
        print(f"Perimeter: {shape.cal_perimeter():.1f}m\n")