import tkinter as tk
ventana=tk.Tk()
ventana.title("Ejemplo Entry")

etiqueta=tk.Label(ventana,text="Digite algo")


entrada=tk.Entry(ventana) #Escribir  datos

entrada.config(fg="blue",bg="lightgray", font=("Arial",12))
entrada.insert(0,"Nombre")


def aplicar_texto():
    texto=entrada.get() #Guardar el contenido
    etiqueta.config(text=texto)
 

boton=tk.Button(ventana,text="Aplicar texto")
boton.config(fg="white", bg="green", font=("Arial",12))
boton.config(command=aplicar_texto)





entrada.pack()

boton.pack()
etiqueta.pack()
ventana.mainloop()

