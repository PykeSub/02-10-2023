from Animal import Animal

class Reptil(Animal):
    def __init__(self, nombre: str, edad: int, patas: int, piel: str):
        super().__init__(nombre, edad, patas)
        self.__piel = piel
        
    def __str__(self):
        txt = super().__str__()
        txt += f'\nPiel: {self.__piel}'
        return txt
    
    def comer(self):
        print('Estoy comiendo carne')