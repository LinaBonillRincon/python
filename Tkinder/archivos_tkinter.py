import tkinter as tk
from tkinter import filedialog
ventana=tk.Tk()
ventana.title("Archivos con tkinter")
ventana.withdraw()
file_path=tk.filedialog.askopenfilenames() #Mas de un archivo seleccionado
print(file_path)
file_obj=filedialog.askopenfile(mode='r')
if file_obj:
    print(file_obj.read())
    file_obj.close()

ventana.mainloop()