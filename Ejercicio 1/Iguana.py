from Reptil import Reptil

class Iguana(Reptil):
    def __init__(self, nombre: str, edad: int, patas: int, piel: str):
        super().__init__(nombre, edad, patas, piel)