#With ISP
from abc import ABC, abstractmethod
class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class Worker(Workable, Eatable):
    def work(self):
        print("Worker is working.")

    def eat(self):
        print("Worker is eating.")
        
w1 = Worker() 
w1.work()
w1.eat()       