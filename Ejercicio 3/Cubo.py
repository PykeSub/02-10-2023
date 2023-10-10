from Rectangulo import Rectangulo

class Cubo(Rectangulo):
    def __init__(self, largo: float, ancho: float, lado3: float):
        super().__init__(largo, ancho)
        self.lado3 = lado3
        
    def volumen(self):
        return self.largo * self.ancho * self.lado3
    
    def ver(self):
        super().ver()
        print(f'Lado 3: {self.lado3}')
        print(f'Volumen: {self.volumen()}')
        
    def __str__(self):
        return f'Cubo con lados {self.largo}, {self.ancho}, {self.lado3}'
    
    