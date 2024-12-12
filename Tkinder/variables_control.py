"""
StringVar Cadenas de texto
IntVar  Enteros
DoubleVar Flotantes
BooleanVar Booleanos

Mantener y gestionar valores en campos de texto y botones
"""

import tkinter as tk
ventana=tk.Tk()
ventana.title("Ejemplo variables de control")

booleano=tk.BooleanVar(value=True)
check2=tk.Checkbutton(ventana,text="Opcion 2", font=("Arial",14),fg="blue", bg="lightgray", variable=booleano)
check2.pack()

def actualizar(*args):
    print(booleano.get())

booleano.trace("w", actualizar)


"""
decimal=tk.DoubleVar(value=3.14)

control_delizante=tk.Scale(ventana, variable=decimal, from_=0, to=10, resolution=0.01, orient=tk.HORIZONTAL)
control_delizante.pack() 
"""

"""
entero=tk.IntVar(value=42)
opcion1= tk.Radiobutton(ventana,text="1", font=("Arial",14),fg="blue", bg="lightgray", variable=entero, value=1 )
#Cuando se ponen valores y se ejerce un control, ya se selecciona solo única respuesta
opcion2= tk.Radiobutton(ventana,text="2", font=("Arial",14),fg="blue", bg="lightgray", variable=entero, value=2)

opcion1.pack()
opcion2.pack()

def actualizar(*args):
    print(entero.get())
entero.trace("w",actualizar)
"""

"""
texto=tk.StringVar(value="Hola mundo")
print(texto.get())
entrada=tk.Entry(ventana, textvariable=texto)
entrada.pack()

etiqueta=tk.Label(ventana)
etiqueta.pack()

def actualizar_etiqueta(*args):
    etiqueta.config(text=texto.get())

texto.trace("w", actualizar_etiqueta) #Modo escritura y actualización
"""

ventana.mainloop()