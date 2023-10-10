from Animal import Animal

class Mamifero(Animal):
    def __init__(self, nombre: str, edad: int, patas: int, raza: str, tamanio: int):
        super().__init__(nombre, edad, patas)
        self.__raza = raza
        self.__tamanio = tamanio
        
    def __str__(self):
        txt = super().__str__()
        txt += f'\nRaza: {self.__raza}'
        txt += f'\nTamanio: {self.__tamanio}'
        return txt
    
    def comer(self):
        print('Estoy tomando leche')