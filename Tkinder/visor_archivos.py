import tkinter as tk
from tkinter import filedialog
ventana=tk.Tk()
ventana.title("Visor de archivos")
text_widget=tk.Text(ventana, wrap="word")
text_widget.pack(expand=True, fill='both')

def abrir_archivo():
    file_path=filedialog.askopenfilename(filetypes=[('Archivos de texto', '*.txt'), ('Todos los archivos', '*-*')])
    if file_path:
        with open(file_path, 'r') as file_obj:
            contenido=file_obj.read()
            text_widget.delete(1.0, tk.END)
            text_widget.insert(tk.INSERT,contenido)




abrir_boton=tk.Button(ventana, text="Abrir archivo", command=abrir_archivo)
abrir_boton.pack()
ventana.mainloop()