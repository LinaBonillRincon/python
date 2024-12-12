#Mecanismo que permite crear clases a partir de clases existentes 
""" Reutilización de código
Clase original - Clase padre
Clase herdera - Clase Hijo

Se puede heredar atributos y métodos 

"""
class Clasebase:
    def __init__(self):
        print("Constructor de ClaseBase")
    def metodo_clase(self):
        print("Metodo de clase base")

class Clasederivada(Clasebase): #Herencia
    def __init__(self):
        #Super().__init__()
        print("Contructor de clase derivada")

#obj = Clasederivada()
#obj.metodo_clase()  


#Clase constructor
#Clase derivada super().__init__() #Conserva contructor original


#Polimorfismo
"""
Permite reducir el código a la hora de crear funciones que proporciona 
resultados similares o diferentes

"""


