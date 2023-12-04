# ***DATA ABSTRACTION***
# -It hides unnecessary code details from the user. Also,  when we do not want to give out sensitive parts of our code implementation and this is where data abstraction came.
# DATA HIDING - In Python, we use double underscore (Or __) before the attributes name and those attributes will not be directly visible outside. 

# class MyClass:
#     # Hidden member of MyClass
#     __hiddenVariable = 0

#     # A member method that changes 
#     # __hiddenVariable
#     def add(self, increment):
#         self.__hiddenVariable += increment
#         print(self.__hiddenVariable)

# # Driver Code
# myObject =  MyClass()
# myObject.add(2)
# myObject.add(5)

# # This line causes error
# print(myObject.__hiddenVariable)

# In the above program we tried to access a hidden variable the class using an object and it threw exception \
# We can access the value of hidden attribute by tricky syntax:

# A Python program to demonstrate that hidden 
# members can be accessed outside a class
class MyClass:

    # Hidden member of MyClass
    __hiddenVariable = 10

# Driver Code
myObject = MyClass()
print(myObject._MyClass__hiddenVariable)


