import tkinter as tk
ventana=tk.Tk()
ventana.title("Ejemplo Radiobutton")

#Opciones para elegir
#Variable control

variable_control=tk.IntVar()




#Mostrar selección

def mostrar_seleccion():
    print("Opcion seleccionada: ", variable_control.get())


def color_selecionado():
    color_selecionado= variable_control.get()
    if color_selecionado ==1:
        ventana.config(bg="red")
    elif color_selecionado ==2:
        ventana.config(bg="blue")

#OTRA OPCIÓN ES DIRECTAMENTE EN LOS RADIOBUTTON
opcion1= tk.Radiobutton(ventana,text="Rojo", font=("Arial",14),fg="blue", bg="lightgray", variable=variable_control, value=1, command=color_selecionado)
#Cuando se ponen valores y se ejerce un control, ya se selecciona solo única respuesta
opcion2= tk.Radiobutton(ventana,text="Azul", font=("Arial",14),fg="blue", bg="lightgray", variable=variable_control, value=2,command=color_selecionado)
opcion1.pack()
opcion2.pack()
#boton=tk.Button(ventana, text="Mostrar selección", command=color_selecionado)
#boton.pack() UNA OPCIÓN
ventana.mainloop()



