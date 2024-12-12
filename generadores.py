"""Funciones que permiten crear iteradores de manera sencilla y eficiente

La diferencia entre un generador y una funcion regular es que los generadores no retornan  un valor unico, sino que producen una serie de valores, uno  por vez, cada vez que lo solicitan

palabra clave: yield (pausar ejecución)

Cuando se llama de nuevo a un generador, este continúa su ejecución desde donde se dejo, en lugar desde cereo como una función regular.


"""

def numeros_pares(limite):
    numero=0
    while numero <= limite:
        yield numero
        numero+=2

#iteración
"""for par in iter(numeros_pares(10)):
    print(par)"""

#También se puede en lista
pares_lista=list(numeros_pares(10))
#print(pares_lista)


def fibonacci(limite):
    a,b=0,1
    while a< limite:
        yield a
        a,b =b,a +b

for num in iter(fibonacci(10)):
    print(num)


    

