# class creation
class Circle:
    
    shape_object ="circle"
    
    def __init__(self,radius=1.0):
        self.radius = radius
        
    def __str__(self):
        return 'This is a circle with radius of {:.2f}'.format(self.radius)
    
    def get_area(self) :
        return self.radius * self.radius * 3.14  
    
# object creation    
c1 = Circle(5)    
print(c1)
print('The area of the circle is: {:.2f}'.format(c1.get_area()))