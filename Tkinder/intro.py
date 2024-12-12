"""
Libreria grafica que permite la creación de interfaz de usuario

"""
import tkinter as tk
#Crear la ventana
ventana=tk.Tk()
ventana.title("Mi primera ventana")

#Configuración 
#Tamaño
ventana.geometry("600x400") # mas coordenadas en que aparezca en la ventana
#Minimo de ventana
ventana.minsize(400,200)
ventana.maxsize(800,600)
#Icono de ventana: ventana.iconbitmap(imagen en mismo archivo. ico)
ventana.configure(bg="lightblue")
#bloquear el incremento o reducción de la ventana con ventana.resizable(false,false)

#ventana semi transparente ventana.atributes("-alpha",1)

#Etiqueta 
"""
etiqueta =tk.label(ventana, text= Hola)
etiqueta.config(fg=blue, bg= front=(Arial, 14,))
etiqueta.pack()

"""

ventana.mainloop()
