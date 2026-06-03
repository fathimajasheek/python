#single inheritance
class animal:
    def __init__(self,name):
        self.name=name
    def sound(self):
        print(f"{self.name} woofed")
class dog(animal):
    def speak(self):
        print(f"{self.name} cried")
x=dog("jacky")
x.sound()
x.speak()
    
#multiple inheritance   
class animal:
    def __init__(self,name):
        self.name=name
    def sound(self):
        print(f"{self.name} woofed")
class human:
    def __init__(self,name):
        self.name=name
    def sound1(self):
        print(f"{self.name} smiled")
class dog(animal,human):
    def speak(self):
        print(f"{self.name} cried")
x=dog("sandra")
x.sound()
x.speak()
x.sound1()

#multilevel inheritance
class animal:
    def __init__(self,name):
        self.name=name
    def sound(self):
        print(f"{self.name} woofed")
class dog(animal):
    def speak(self):
        print(f"{self.name} cried")
class puppy(dog):
    def speak1(self):
        print(f"{self.name} barked")
x=puppy("willow")
x.sound()
x.speak()
x.speak1()

#hierarchical inheritance
class animal:
    def __init__(self,name):
        self.name=name
    def sound(self):
        print(f"{self.name} woofed")
class dog(animal):
    def speak(self):
        print(f"{self.name} cried")
class cat(animal):
    def speak1(self):
        print(f"{self.name} meowed")
x=dog("rocky")
y=cat("lily")   
x.sound()
x.speak()
y.sound()
y.speak1()

#hybrid inheritance
class animal:
    def __init__(self,name):
        self.name=name
    def sound(self):
        print(f"{self.name} woofed")
class dog(animal):
    def speak(self):
        print(f"{self.name} cried")
class cat(animal):
    def speak1(self):
        print(f"{self.name} meowed")
class puppy(dog):
    def speak2(self):
        print(f"{self.name} barked")
x=puppy("rocky")
y=cat("lily")
x.sound()
x.speak()
x.speak2()
y.sound()
y.speak1()
