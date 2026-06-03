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
    
    