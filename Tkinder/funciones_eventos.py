import tkinter as tk

def on_click(event): #Función que ejecuta evento
    print("Boton presionado")

ventana=tk.Tk()

button=tk.Button(ventana,text="Haz click aqui")
button.pack()

button.bind("<Button-1>",on_click) #Evento click con e izquierdo

"""
Evento con tecla 

def on_key_press(evento):
 if evento.char == "a"
    print("Tecla 'a' presionado")

ventana.bind("<KeyPress>", on_key_press)

#Redimensionar la ventana

def on_resize(event):
print (f" La ventana ha sido redimensionada a {event.wight} x {event.height}")

ventana.bind("<Configure>", on_resize)

def  on_mouse_move(event):
print(f" Ratón movido = {event.x}, {event.y}")

ventana.bind("<Motion>", on_mouse_move)



def on_click(event):
 print(f"Boton {event.widget['text']} presionado")

botones=[tk.Button(ventana,text="Button {i}") for i in range(3)]


for button in botones:
   button.pack()
   button.bind("<Button-1>", on_click)
"""
ventana.mainloop()