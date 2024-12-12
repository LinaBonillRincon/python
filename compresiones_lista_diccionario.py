"""Crar listas, diccionarios y conjuntos 
de manera consistente

Forma breve de crear listas a partir de listas  u/o objetos iterables 

nueva_lista= [expresion for elemento in iterable if condicion]
 
nuevo_diccionario = {clave: valor for elemento in iterable if condicion}

"""

numeros=[1,2,3,4,5]
cuadrados_pares=[ n ** 2 for n in numeros if n % 2 == 0]
#print(cuadrados_pares)

#Diccionario
personas={'Ana': 22, 'Carlos': 17, 'Maria': 28, 'Pedro': 15}
mayores_de_edad= {nombre:edad for nombre,edad in personas.items() if edad>=18}

#print(mayores_de_edad)

