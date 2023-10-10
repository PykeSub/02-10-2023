from Mamifero import Mamifero

class Gato(Mamifero):
    def __init__(self, nombre: str, edad: int, patas: int, raza: str, tamanio: int):
        super().__init__(nombre, edad, patas, raza, tamanio)