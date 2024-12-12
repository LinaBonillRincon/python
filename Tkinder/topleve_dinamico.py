from tkinter import  *
ventana=Tk()
ventana.title("Ejemplo ventana dinámica")


ventana.geometry("600x400")


ventana_toplevel= Toplevel(ventana)
ventana_toplevel.title("Ventana Toplevel")
ventana_toplevel.geometry("300x200+50+50")
label=Label(ventana_toplevel, text="Ventana_Toplavel")
label.pack()



def cerrar_ventana(ventana):
    ventana.destroy()

"""boton=Button(ventana, text="Abrir Ventana Toplevel", command=abrir_ventana_toplevel)
boton.pack()"""
boton2=Button(ventana, text="Cerrar Ventana Toplevel", command= lambda:cerrar_ventana(ventana_toplevel))
boton2.pack()
"""


"""
ventana.mainloop()