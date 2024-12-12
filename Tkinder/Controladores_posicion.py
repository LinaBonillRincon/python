"""
GRID, PACK, PLACE

Administradores de geometría
Permiten organizar y posicionar los widgets en la interfaz gráfica

GRID Estructura en fila y columnas, control preciso de posición y tamaño

PACK Ubicación por bloques, horizontal o verticalmente 

PLACE: Control de posición en coordenadas específicas 

"""


import tkinter as tk
ventana=tk.Tk()
ventana.title("Ejemplo Controladores de posición")

#Ejemplo de GRID
"""label1=tk.Label(ventana, text="Label 1")
label1.grid(row=0, column=0,padx=10, pady=10)
label2=tk.Label(ventana, text="Label 2")
label2.grid(row=1, column=1, padx=10, pady=10)
"""
"""
EJEMPLO CON PACK

frame_botones=tk.Frame(ventana)
frame_botones.pack(pady=10)

boton1=tk.Button(frame_botones, text="Boton1")
boton1.pack(side="left", padx=5)
boton2=tk.Button(frame_botones, text="Boton2")
boton2.pack(side="left", padx=5)
boton3=tk.Button(frame_botones, text="Boton3")
boton3.pack(side="left", padx=5)
"""

label1=tk.Label(ventana, text="Label 1")
label1.place(x=50, y=50)

label2=tk.Label(ventana, text="Label 2")
label2.place(x=100, y=100)

ventana.mainloop()