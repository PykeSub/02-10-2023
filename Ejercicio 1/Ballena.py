from Mamifero import Mamifero

class Ballena(Mamifero):
    def __init__(self, nombre: str, edad: int, patas: int, raza: str, tamanio: int, color:str):
        super().__init__(nombre, edad, patas, raza, tamanio)
        self.__color = color
        
    def __str__(self):
        txt = super().__str__()
        txt += f'\nColor: {self.__color}'
        return txt
    
    def comer(self):
        print('Estoy comiendo Crustáceos')