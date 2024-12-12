import tkinter as tk
from tkinter import filedialog

def nuevo_archivo():
    texto.delete(1.0,tk.END)

def guardar_archivo():
    global nombre_archivo
    if nombre_archivo:
        try:
            with open(nombre_archivo,"w", encoding="utf-8") as file:
                file.write(texto.get(1.0,tk.END))
        except:
            print("no se puede guardar")

    
def guardarcomo_archivo():
    nueva_ruta=filedialog.asksaveasfilename(defaultextension="*.txt", filetypes=[('Archivos de texto', '*.txt'),('Archivos de python', '*.py'),('Todos los archivos','*.*')])
    if nueva_ruta:
        with open(nueva_ruta,"a", encoding="utf-8") as file:
            file.write(texto.get(1.0,tk.END))


def abrir_archivo():
    
    global nombre_archivo
    nombre_archivo=filedialog.askopenfilename(defaultextension="*.txt", filetypes=[('Archivos de texto', '*.txt'),('Archivos de python', '*.py'),('Todos los archivos','*.*')])
    texto.delete(1.0,tk.END)
    with open(nombre_archivo,"r", encoding="utf-8") as file:
        texto.insert(tk.INSERT,file.read())

def copiar():
    texto.event_generate("<<Copy>>")

def pegar():
    texto.event_generate("<<Paste>>")

def cortar():
    texto.event_generate("<<Cut>>")

ventana=tk.Tk()
ventana.title("Bloc de notas")
ventana.geometry("800x600")
menu=tk.Menu(ventana)
ventana.config(menu=menu)
archivo=tk.Menu(menu)
menu.add_cascade(label="Archivo", menu=archivo)
nombre_archivo=""
edicion=tk.Menu(menu)
menu.add_cascade(label="Edición", menu=edicion)

texto=tk.Text(ventana)
texto.pack(fill=tk.BOTH, expand=True)
archivo.add_command(label='Abrir', command=abrir_archivo)
archivo.add_command(label='Nuevo', command=nuevo_archivo)
archivo.add_command(label='Guardar', command=guardar_archivo)
archivo.add_command(label='Guardar como', command=guardarcomo_archivo)

edicion.add_command(label='Copiar', command=copiar)
edicion.add_command(label='Pegar', command=pegar)
edicion.add_command(label='Cortar', command=cortar)

ventana.mainloop()