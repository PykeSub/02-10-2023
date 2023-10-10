from Animal import Animal

class Hormiga(Animal):
    def __init__(self, nombre: str, edad: int, patas: int, tipo: str):
        super().__init__(nombre, edad, patas)
        self.__tipo = tipo
        
    def __str__(self):
        txt = super().__str__()
        txt += f'\nTipo: {self.__tipo}'
        return txt