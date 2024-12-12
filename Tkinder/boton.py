import tkinter as tk
ventana=tk.Tk()
ventana.title("Ejemplo Boton")

boton=tk.Button(ventana,text="Presiona aqui")
boton.config(fg="white", bg="green", font=("Arial",12))
boton.pack()

etiqueta=tk.Label(ventana,text="Hola")
etiqueta.pack()



def cambiar_texto():
    etiqueta.config(text="Botón presionado")
boton.config(command=cambiar_texto)
ventana.mainloop()