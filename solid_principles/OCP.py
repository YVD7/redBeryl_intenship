"""
open/closed principle--->open for extension but close for modification

this principle is used in oops for extend the funcationlity of the code and it should only used for modification not for close the code


"""
# here in this example we are extend the funcationlity of area funcation means we are  using  same funcation for differnt purposes  but we can not modify the funcationlity of parent class
from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def area(self):
        pass

class rectangle(shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
class square(shape):
    def __init__(self, length):
        self.length = length     

    def area(self):
        return self.length * self.length

class circle(shape):
    def __init__(self, radius):
        self.radius = radius        

    def area(self):
        return 3.14 * self.radius * self.radius

# Creating instances of different shapes
rect = rectangle(5, 10)
sq = square(7)
cir = circle(4)

# Calculating areas of the shapes
print("Area of Rectangle:", rect.area())  # Output: 50
print("Area of Square:", sq.area())      # Output: 49
print("Area of Circle:", cir.area())     # Output: 50.24 (approximately)
