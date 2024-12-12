from tkinter import  *


"""
Menubutton
Menu
Menus contextuales
"""
ventana=Tk()
ventana.title("Ejemplo ventana dinámica")
"""
Menu en boton
menubutton=Menubutton(ventana, text="Archivo")
menubutton.pack()

menu=Menu(menubutton)
menubutton.config(menu=menu)
def abrir_archivo():
    print("Abierto")



menu.add_command(label="Abrir", command=abrir_archivo)



Menu 
barramenu=Menu(ventana)
ventana.config(menu=barramenu)
archivo_menu=Menu(barramenu)
barramenu.add_cascade(label="Archivo",menu=archivo_menu)
archivo_menu.add_command(label="Nuevo")
archivo_menu.add_command(label="Abrir")
archivo_menu.add_separator()
archivo_menu.add_command(label="Salir")

"""
def mostrar_menu_contextual(event):
    menu_contextual.tk_popup(event.x_root, event.y_root)


menu_contextual=Menu(ventana, tearoff=0)
menu_contextual.add_command(label="Cortar")
menu_contextual.add_command(label="Copiar")
menu_contextual.add_command(label="Pegar")

entrada=Entry(ventana)
entrada.pack()

entrada.bind("<Button-3>", mostrar_menu_contextual)#El menu solo aparece en la entrada de texto
#ventana.bind("<Button-3>", mostrar_menu_contextual)#El menu aparece en toda la ventanas
ventana.mainloop()