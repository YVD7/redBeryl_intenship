"""
Encapsulation 

Encapsulation is one of the fundamental concepts in object-oriented programming (OOP). 

It refers to the practice of bundling the data (attributes or properties) and methods (functions or procedures) that operate on that data into a single unit, often called a class. 

In encapsulation, the internal representation of an object is hidden from the outside, and access to the object's data is typically controlled through well-defined interfaces, which are the class's methods.

data hiding--->
 Encapsulation allows you to hide the internal state (data) of an object from the external world. This is typically achieved by marking the object's attributes as private and providing controlled access to them through methods.


"""
class Car:
    def __init__(self, make, model, mileage):
        self._make = make  # Protected attribute
        self.__model = model  # Private attribute
        self.mileage = mileage  # Public attribute

    # Getter method for protected attribute _make
    def get_make(self):
        return self._make

    # Setter method for private attribute __model
    def set_model(self, new_model):
        self.__model = new_model

    # Method to display car information
    def display_info(self):
        print(f"Make: {self._make}")
        print(f"Model: {self.__model}")
        print(f"Mileage: {self.mileage}")


# Creating an instance of the Car class
my_car = Car('Toyota', 'Corolla', 50000)

# Accessing attributes using methods
print("Using Getter Method - Make:", my_car.get_make())  # Accessing protected attribute
my_car.set_model('Camry')  # Modifying private attribute using a setter method

# Accessing attributes directly (not recommended, but possible)
print("Directly accessing public attribute - Mileage:", my_car.mileage)
# print("Directly accessing protected attribute - Make:", my_car._make)  # Avoid direct access
# print("Directly accessing private attribute - Model:", my_car.__model)  # Raises AttributeError

# Displaying car information using a method
my_car.display_info()
