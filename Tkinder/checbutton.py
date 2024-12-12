import tkinter as tk
ventana=tk.Tk()
ventana.title("Ejemplo Checkbutton")

variable_check1=tk.BooleanVar() #True o false acorde a la selección
variable_check2=tk.BooleanVar() #Mas de una variable de control

def checkbutton_selec():
    if variable_check1.get():
        boton.config(state="normal") #Acceder al botón
    else:
         boton.config(state="disabled") #No se puede acceder al botón




check1=tk.Checkbutton(ventana,text="Opcion 1", font=("Arial",14),fg="blue", bg="lightgray", variable=variable_check1, command=checkbutton_selec)
check2=tk.Checkbutton(ventana,text="Opcion 2", font=("Arial",14),fg="blue", bg="lightgray", variable=variable_check2)
boton=tk.Button(ventana, text="Botón", state="disabled")
check1.pack()
check2.pack()
boton.pack()
ventana.mainloop()