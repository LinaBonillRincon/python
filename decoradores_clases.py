"""Igual que en funciones solo 
que con una ligera modificación
"""

def decorador_clase(cls):
    class ClaseDecoradora(cls):
        def metodo_decorado(self):
            print("Estamos en el metodo decorado ")
            return self.metodooriginal()
    return ClaseDecoradora

@decorador_clase
class MiClase:
    def metodooriginal(self):
        print("Estamos en el metodo original")

#mi_objeto=MiClase()
#mi_objeto.metodo_decorado()


#Anidados

def decorador1(func):
    def funcion_interna():
        print("Decorador 1")
        func()
    return funcion_interna

def decorador2(func):
    def funcion_interna():
        print("Decorador 2")
        func()
    return funcion_interna

@decorador1
@decorador2
def mi_funcion():
    print("Funcion original")

mi_funcion()