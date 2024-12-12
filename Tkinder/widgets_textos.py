import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import askopenfilename, askopenfilenames
from tkinter import filedialog

def abrir_archivo():
    archivo= askopenfilename()
    if archivo:
        texto_desplegable.delete(1.0,"end")
        with open(archivo,"r") as file:
            texto_desplegable.insert(1.0, file.read())



def guardar_archivo():
    archivo=filedialog.asksaveasfile(mode="w",defaultextension="*.txt", filetypes=[('Archivos de texto', '*.txt'),('Todos los archivos','*.*')])
    if archivo:
        archivo.write(texto_desplegable.get(1.0, "end"))
        archivo.close()


ventana=tk.Tk()
ventana.title("Widgets textos")

texto_desplegable=ScrolledText(ventana, wrap="word")
texto_desplegable.pack(expand=True, fill="both")

boton_abrir=tk.Button(ventana,text="Abrir", command=abrir_archivo)
boton_guardar=tk.Button(ventana, text="Guardar", command=guardar_archivo)
boton_abrir.pack(side="left")
boton_guardar.pack(side="right")

"""
def copiar():
    texto.event_generate("<<Copy>>")

def pegar():
    texto.event_generate("<<Paste>>")

def cortar():
    texto.event_generate("<<Cut>>")



texto=tk.Text(ventana)
texto.pack()
boton_copiar=tk.Button(ventana,text="Copiar", command=copiar)
boton_pegar=tk.Button(ventana,text="Pegar", command=pegar)
boton_cortar=tk.Button(ventana,text="Cortar", command=cortar)
boton_copiar.pack()
boton_pegar.pack()
boton_cortar.pack()



texto=tk.Text(ventana, width=40, height=10, wrap="word", bg="lightgray", fg="black", padx=10, pady=10, font=("Helvetica", 12))

texto.insert("1.0", "Bienvenido")
texto.insert("end", "\n\n Adios", "resaltado")
texto.tag_config("resaltado", background="yellow", foreground="black")
contenido=texto.get("1.0", "end") #Extrae el contenido 
print(contenido)
#texto.delete("1.0", "end")
texto.pack()

texto_desplazable=ScrolledText(ventana)
texto_desplazable.pack()
"""
ventana.mainloop()