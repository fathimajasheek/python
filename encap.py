class bank:
    def __init__(self,name,balance):
        self.name=name #public
        self.__balance=balance #private
    def about(self):
        print(f"{self.name} has {self.__balance} in their account")
    def balance(self):
        print(self.__balance)
a=bank("fathima",2000)
print(a.name)
a.about()
a.balance()
    