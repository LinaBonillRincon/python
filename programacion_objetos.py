#CONCEPTOS BASICOS
#Objeto Entidad que tiene atributos (características) y métodos (comportamiento)
#Clase es el molde que define los atributos y métodos comunes a todos los objetos
#class nombre: pass
#especio = 'bulldog ingles' (Atributo)
# def ladrar (self) : print("guau")
#constructor __init__(self, nombre, edad): #automatico
# self.nombre=nombre


class Perro:
    especie= 'Bulldog Inglés'
    def __init__(self, nombre,edad):
        self.nombre=nombre
        self.edad=edad
        #print('Hola '+nombre)
    def ladrar(self):
        print("Guauuu!")

#Crear objeto
mi_perro=Perro("Lorenzo",3)
#Llamar a los atributos
print(mi_perro.edad)
#Acceder a la función (comportamiento)
mi_perro.ladrar()
#modificar valor
mi_perro.edad=4
#Eliminar objeto es del mi_perro