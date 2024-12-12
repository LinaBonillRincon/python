"""
*args y **kwargs

*args converción de Python para para una lista de varibales de argumentos

**kwargs pasar discionario de atributos

"""

def sumar_numeros(*args): #*numeros (lista indefinida de valores)
    suma=0
    for numeros in args:
        suma+=numeros
    return suma

#resultado=sumar_numeros(1,2,3,4,5)
#print(resultado)

def mostrar_informacion(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

#mostrar_informacion(nombre="Ana",edad=25,ciudad="Madrid")
        
#Desempaquetado
        
def multiplicar_numeros(a,b,c):
    return a* b*c
numeros=(2,3,4)
resultado=multiplicar_numeros(*numeros)
print(resultado)

def mostrar_informacion(nombre,edad,ciudad):
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Ciudad: {ciudad}")

info= {"nombre": "Carlos","edad": 30, "ciudad": "Barcelona"}
mostrar_informacion(**info)


