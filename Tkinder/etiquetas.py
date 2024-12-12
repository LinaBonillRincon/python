import tkinter as tk
import time
ventana=tk.Tk()
ventana.title("Ejemplo Reloj")

etiqueta=tk.Label(ventana,text="Hola")
etiqueta.pack()

def actualizar_hora():
    etiqueta.config(text=time.strftime("%H:%M:%S"))
    ventana.after(1000,actualizar_hora)

actualizar_hora()

ventana.mainloop()