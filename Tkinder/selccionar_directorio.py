import tkinter as tk
from tkinter import filedialog
import os

def seleccionar_directorio():
    dir_path=filedialog.askdirectory() #Carpeta
    if dir_path:
        listabox.delete(0,tk.END)
        for file in os.listdir(dir_path):
            listabox.insert(tk.END, file)

ventana=tk.Tk()
ventana.title("Seleccionar directorios")
listabox=tk.Listbox(ventana)
listabox.pack(expand=True, fill="both")
seleccionar_boton=tk.Button(ventana, text="Seleccionar directorio", command=seleccionar_directorio)
seleccionar_boton.pack()
ventana.mainloop()