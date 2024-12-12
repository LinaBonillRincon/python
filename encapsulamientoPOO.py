#permite ocultar detalles internos de una clase y exponer solo lo necesario
#codigo mas facil de entender 
#Evita manipulaciones no deseadas
#en la clase constructor 
# self.__marca(marca)
#def __nombrefuncion(self):

class Auto:
    def __init__(self,marca, modelo, año):
        self.__marca=marca #privado
        self.__modelo=modelo
        self.año= año #publico
    def get_marca(self):
        return self.__marca
    def set_marca(self,marca):
       self.__marca=marca
    def get_modelo(self):#Extraer datos privados
        return self.__modelo
    def set_modelo(self,modelo):#Crear o modificar dato privado
        self.__modelo=modelo
    def __acelerar(self):
        print("Acelerar")


mi_auto=Auto("Chevrolet","C4",2016)
print(mi_auto.año)
print(mi_auto.get_marca())
#Acceder a una función privada
mi_auto._Auto__acelerar()