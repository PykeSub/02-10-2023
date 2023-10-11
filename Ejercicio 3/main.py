from Rectangulo import Rectangulo
from Cubo import Cubo

r = Rectangulo(7, 9)
print(r.Perimetro())
print(r.Area())
r.ver()
lado3 = input('Ingrese lado3 : ')
c = Cubo(4, 4, 4)
#c = Cubo(4)
print(c.Volumen())
c.ver()
