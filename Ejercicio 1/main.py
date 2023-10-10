from Animal import Animal
from Reptil import Reptil
from Mamifero import Mamifero
from Iguana import Iguana
from Hormiga import Hormiga
from Perro import Perro
from Ballena import Ballena
from Gato import Gato

a1 = Animal('Juanito', 20, 2)
print(a1)
a1.comer()
r1 = Reptil('Maxial Juanito', 7, 3, 'Dura')
print(r1)
r1.comer()
m1 = Mamifero('Leon Juanito', 5, 4, 'Felino', 2)
print(m1)
m1.comer()
i1 = Iguana('Julio Juanito', 10, 4, 'Aspera')
print(i1)
i1.comer()
h1 = Hormiga('Alberto Juanito', 7, 4, 'Fuego')
print(h1)
h1.comer()
p1 = Perro('Maximus Juanito', 9, 4, 'Pitbull', 15, 'Pureza Racial')
print(p1)
p1.comer()
b1 = Ballena('Leonidas', 11, 0, 'Franca', 22, 'Azul')
print(b1)
b1.comer()
g1 = Gato('Tom', 2, 4, 'Asiático', 8)
print(g1)
g1.comer()