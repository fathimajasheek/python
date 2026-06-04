class animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print(f"{self.name} woofed")
class dog(animal):
    def speak(self):
        print(f"{self.name} barked")
class cat(animal):
    def speak(self):
        print(f"{self.name} meowed")
x=dog("rocky")
y=cat("lily")
x.speak()
y.speak()
