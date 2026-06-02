#function without parameter
def greet():
    print ("hello")
greet()
#function with parameters
def add(a,b):
    print(a+b)
add(5,3)
#return statement
def mul(a,b):
    return(a*b)
print(mul(3,5))
a=mul(3,5)
print(5+a)
#arguments
def add(a,*b,**c):
    print(a)
    print(b)
    print(c)
add(1,2,3,4,5,name="fathima",age=20)
#scope
x=10
def scope():
    x=34
    print(x)
scope()
print(x)