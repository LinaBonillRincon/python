# with open("nombre del archivo.txt","a") as archivo
#nombredecarpeta/nombre del archivo, motivo de abrir a, w , r ,r+, w+
archivo=open("nombre del archivo.txt","a") #modo escritura
#"r" leer archivo
# "a" añadir contenido sin borrar
# "r+ w+" leer y escribir
archivo.write("\n Bienvenido")
#writelines (permite escribir varias lineas)
archivo.close() #Siempre ponerlo al final de las acciones con el archivo
#interación poner open "r"
#for linea in archivo: print(linea)  
# nueva variable= archivo.read() completo
#nueva variable= archivo.readline() una linea
