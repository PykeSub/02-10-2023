class Rectangulo:
    def __init__(self, largo: float, ancho: float):
        self.largo = largo
        self.ancho = ancho
        
    def perimetro(self):
        return 2 * (self.largo + self.ancho)
    
    def area(self):
        return self.largo * self.ancho
    
    def ver(self):
        print (f'Longitud: {self.largo}')
        print (f'Ancho: {self.ancho}')
        print (f'Perimetro: {self.perimetro()}')
        print(f'Area: {self.area()}')
        
    def __str__(self):
        return f'Rectangulo de largo {self.largo} y ancho {self.ancho}'
    
    