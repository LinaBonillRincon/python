"""
Permite modificacion de comportamiento de funciones o métodos

función que toma otra función como argumento y devuelve otra función que conlleva funcionalidades adicionales

Función de orden superior 

"""
def decorador(func):
    def nueva_funcion():
        print("Funcionalidad antes de llamar a 'func' ")
        func()
        print("Funcionalidad adicional despues de llamar 'func'")
    return nueva_funcion
@decorador
def funcion_decorador():
    print("Soy la funcion original")

funcion_decorador()







def saludar(func):
    print("Esto se imprime antes")
    func()

def hola():
    print("Hola")

# Retornossaludar(hola)