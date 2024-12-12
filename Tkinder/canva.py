import tkinter as tk
ventana=tk.Tk()
ventana.title("Ejemplo Canvas")

canvas=tk.Canvas(ventana, width=500, height=300, bg="lightblue")
rectangulo=canvas.create_rectangle(50,50,150,100, fill="green", outline="black", width=2)
ovalo=canvas.create_oval(200,50,300,150, fill="blue",width=2)
poligono=canvas.create_polygon(350,50,400,100,350,150, fill="purple", outline="black", width=2)
canvas.create_line(10,200,100,250)
imagen=tk.PhotoImage(file='c://Users//Pc//Documents//python//Tkinder//Arturia1.png')
canvas.create_image(150,200, image=imagen, anchor='nw')


canvas.pack(fill='both',expand=True)


ventana.mainloop()