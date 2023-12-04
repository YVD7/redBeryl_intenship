"""
what is Polymorphis: The word polymorphism means having many forms. In programming, polymorphism means the same function name (but different signatures) being used for different types. The key difference is the data types and number of arguments used in function.
"""

class Animal:
    def speak(self):
        pass  # Placeholder method

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Duck(Animal):
    def speak(self):
        return "Quack!"

# Function that interacts with Animal objects
def make_animal_speak(animal):
    return animal.speak()

# Creating instances of different classes
dog = Dog()
cat = Cat()
duck = Duck()

# Calling the function with different instances
print(make_animal_speak(dog))   # Outputs: Woof!
print(make_animal_speak(cat))   # Outputs: Meow!
print(make_animal_speak(duck))  # Outputs: Quack!
