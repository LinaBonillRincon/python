import tkinter as tk
ventana=tk.Tk()
ventana.title("Ejemplo Canvas arrastrar")


def iniciar_arrastrar(event):
    global objeto_seleccionado
    objeto_seleccionado=canvas.find_closest(event.x, event.y)

def terminar_arrastre(event):
    global objeto_seleccionado
    if objeto_seleccionado:
        x,y=event.x,event.y
        canvas.move(objeto_seleccionado, x- canvas.coords(objeto_seleccionado)[0], y - canvas.coords(objeto_seleccionado)[1] )


canvas=tk.Canvas(ventana, width=500, height=300, bg="lightblue")



canvas.pack(fill='both',expand=True)
objeto_seleccionado=None
rectangulo=canvas.create_rectangle(100,100,200,200, fill="blue",tags="rectangulo")

canvas.tag_bind('rectangulo', '<ButtonPress-1>', iniciar_arrastrar)
canvas.tag_bind('rectangulo', '<ButtonRelease-1>', terminar_arrastre)
ventana.mainloop()