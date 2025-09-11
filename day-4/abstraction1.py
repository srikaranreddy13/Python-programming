from abc import ABC, abstractmethod
 
# Abstract class
class Shape(ABC):
 
    @abstractmethod           # Abstract method
    def area(self):
        pass 
class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius
r=Rectangle(3,4)
c=Circle(10)
print(f"Area of rectangle is:{r.area()}")
print(f"Area of circle is:{c.area()}")


