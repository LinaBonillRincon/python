import tkinter as tk

def mostrar_mensaje():
    mensaje="Hola mundo!!"
    etiqueta.config(text=mensaje)


ventana=tk.Tk()
ventana.title("Mi Aplicación")
ventana.geometry("300x200")
etiqueta=tk.Label(ventana, text="Presiona el botón para mostrar el mensaje")
etiqueta.pack(pady=20)
boton=tk.Button(ventana, text="Mostrar mensaje", command=mostrar_mensaje )
boton.pack()
ventana.mainloop()