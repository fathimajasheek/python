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
x=dog("jacky")
x.sound()
x.speak()
x.sound1()