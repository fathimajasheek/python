#ysing init
class dress:
    def __init__(self,size,type,colour):
        self.size=size
        self.type=type
        self.colour=colour
    def displayinfo(self):
        print(f"{self.type} in {self.colour} colour in size {self.size}")
dress1=dress("medium","frock","blue")
print(dress1.size)
print(dress1.type)
print(dress1.colour)
dress1.displayinfo()

#without init
class food:
    def attr(self,portion,cuisine):
        self.portion=portion
        self.cuisine=cuisine
    def about(self):
        print(f"the food is from {self.cuisine} cuisine and in {self.portion} portion")
food1=food()
food1.attr("quarter","asian")
food1.about()

