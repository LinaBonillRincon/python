import tkinter as tk
ventana=tk.Tk()
ventana.title("Mi primera ventana")
ventana.geometry("600x400")
ventana.configure(bg="lightblue")

labelframe=tk.LabelFrame(ventana, text="Grupo", bg="yellow", padx=10,pady=10)
labelframe.configure(width=300,height=200)
labelframe.pack()
'''
#FRAMES
frame1=tk.Frame(ventana)
frame1.configure(width=300,height=200,bg="red",bd=5)
#Frame debtro de otro frame
frame2=tk.Frame(frame1)
frame2.configure(width=100,height=100,bg="blue",bd=5)
#Botones

boton=tk.Button(frame1,text="Hola")
boton.pack()
#Ejecución de los frame
frame1.pack()
frame2.pack()

'''
ventana.mainloop()