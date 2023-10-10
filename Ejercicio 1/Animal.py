class Animal:
    def __init__(self, nombre: str, edad: int, patas: int):
        # Asignar cada parametro como atributo
        self.__nombre = nombre
        self.__edad = edad
        self.__patas = patas
        
    def get_nombre(self):
        return self.__nombre
    
    def set__nombre(self, nombre):
        self.__nombre = nombre
        
    def get_edad(self):
        return self.__edad
    
    def set__edad(self, edad):
        self.__edad = edad
        
    def get_patas(self):
        return self.__patas
    
    def set_patas(self, patas):
        self.__patas = patas
        
    def __str__(self):
        txt = f'Nombre: {self.__nombre}'
        txt += f'\nEdad: {self.__edad}'
        txt += f'\nPatas: {self.__patas}'
        return txt
    
    def comer(self):
        print('Estoy comiendo algo')