from abc import ABC, abstractmethod
class food(ABC):
    @abstractmethod
    def eat(self):
        pass
class pizza(food):
    def eat(self):
        print("i am eating pizza")
class burger(food):
    def eat(self):
        print("i am eating burger")
x=pizza()
y=burger()
x.eat()
y.eat()