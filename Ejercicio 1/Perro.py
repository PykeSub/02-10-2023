from Mamifero import Mamifero

class Perro(Mamifero):
    def __init__(self, nombre: str, edad: int, patas: int, raza: str, tamanio: int, pedigree: str):
        super().__init__(nombre, edad, patas, raza, tamanio)
        self.__pedigree = pedigree
        
    def __str__(self):
        txt = super().__str__()
        txt += f'\nPedigree: {self.__pedigree}'
        return txt
    
    def comer(self):
        print('Estoy comiendo Champion Dog')