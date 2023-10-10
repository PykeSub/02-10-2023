# Metodo 1
class Calculadora:
    def __init__(self, num1: float, num2: float):
        self.__num1 = num1
        self.__num2 = num2
        
    def suma(self):
        return self.__num1 + self.__num2
    
    def resta(self):
        return self.__num1 - self.__num2
    
    def multiplicacion(self):
        return self.__num1 * self.__num2
    
    def division(self):
        if self.__num2 != 0:
            return self.__num1 / self.__num2
        else:
            return 'No se puede dividir por 0'
        
    def mostrar_resultados(self):
        txt = f'Numero1: {self.__num1}'
        txt = f'Numero2: {self.__num2}'
        txt += f'\nSuma: {self.suma()}'
        txt += f'\nResta: {self.resta()}'
        txt += f'\nMultiplicacion: {self.multiplicacion()}'
        txt += f'\nDivision: {self.division()}'
        return txt