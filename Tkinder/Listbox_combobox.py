import tkinter as tk
from tkinter import ttk
ventana=tk.Tk()
ventana.title("Ejemplo Listbox y Combobox")
"""listbox=tk.Listbox(ventana, width=30, height=10, font=("Arial",12), fg="blue", bg="white") # selectmode=tk.MULTIPLESelectmode es para seleccionar más de una opción
listbox.insert(tk.END, "Elemento 1")
listbox.insert(tk.END, "Elemento 2")
#listbox.insert(posicion, "Elemento ")
#listbox.delete(posición)



#Definición de eventos
def on_select(event):
    indice=listbox.curselection()
    elemento=listbox.get(indice)
    print(f"Selecciono: {elemento}")

def on_clic(event):
    print("Click en el listbox")
def on_doble_clic(event):
    print("Doble Click en el listbox")

listbox.bind("<Button-1>", on_clic)
listbox.bind("<Double-Button-1>", on_doble_clic)
listbox.pack()"""


#COMBOBOX

combobox= ttk.Combobox(ventana, width=30, font=("Arial", 12), foreground="blue", background="white")
combobox.pack()

elementos=["Elemento1", "Elemento2", "Elemento3"]
combobox["values"]=elementos


#Modificar elemento
"""indice=1
nuevo_valor="Elemento modificado"
elementos[indice]=nuevo_valor
combobox["values"]=elementos
"""
def on_select(event):
    valor_seleccionado=combobox.get()
    print(f"Seleccionado: {valor_seleccionado}")

combobox.bind("<<ComboboxSelected>>",on_select)
ventana.mainloop()