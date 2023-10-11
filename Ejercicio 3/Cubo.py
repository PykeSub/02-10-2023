from Rectangulo import Rectangulo

class Cubo(Rectangulo):
    def __init__(self, largo: float, ancho: float, lado3: float):
        super().__init__(largo, ancho)
    #def __init__(self, lado3: float):
        #super().__init__(lado3)
        self.__lado3 = lado3
        
    def volumen(self):
        v = self.lado3 ** 3
        #v = super().area() * self.__lado3
        #v = super().get__ancho() * super().get__largo() * self.__lado3
    
    def ver(self):
        print(f'Lado 3: {self.__lado3}')
        print(f'Volumen: {self.volumen()}')
        print(f'Perimetro: {self.Perimetro()}')
        print(f'Area: {self.Area()}')

    
