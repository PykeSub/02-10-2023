class Rectangulo:
    def __init__(self, largo: float, ancho: float):
        self.__largo = largo
        self.__ancho = ancho
        
    def perimetro(self):
        p = 2 * (self.__largo) + 2 * (self.__ancho)
        return p
    
    def area(self):
        a = self.__largo * self.__ancho
        return a
    
    def ver(self):
        print (f'Longitud: {self.__largo}')
        print (f'Ancho: {self.__ancho}')
        print (f'Perimetro: {self.perimetro()}')
        print(f'Area: {self.area()}')
        

    
    
