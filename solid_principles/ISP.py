#With ISP
from abc import ABC, abstractmethod 
class Workable(ABC):    #workable interface contains a single work method repesenting the ability to work .
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):      #Eatable interface contains a single eat method repesenting the ability to eat
    @abstractmethod
    def eat(self):
        pass

class Worker(Workable, Eatable):       # worker class implements both workable and Eatable interfaces.
    def work(self):         # implementation of work class
        print("Worker is working.")

    def eat(self):          # implemantation of eat class
        print("Worker is eating.")
        
w1 = Worker() 
w1.work()
w1.eat()       