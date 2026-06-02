#importing whole module
import module
print(module.eng("fathima"))
print(module.hindi("fathima"))
#importing function from moduls
from module import eng
print(eng("fathima"))
#importing usimg alias
import module as m
print(m.eng("fathima"))
print(m.hindi("fathima"))