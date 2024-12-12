#IMPORTACIÓN DE IMÁGENES
import tkinter as tk
ventana=tk.Tk()
ventana.title("Ejemplo imagenes")
imagen=tk.PhotoImage(file='c://Users//Pc//Documents//python//Tkinder//Arturia1.png')
etiqueta=tk.Label(ventana,image=imagen)
etiqueta.pack()


ventana.mainloop()
#PIL redimensionar, tamaño, rotación
"""
from PIL import Image, ImageTK
image_pil=image.open()
image_pil.resize
image_pil.rotate
"""