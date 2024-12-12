import tkinter as tk


#Variables
valor_1=0
valor_2=0
operacion="suma"
resultado=0

#Funciones interfaz grafica

def sumar():
    global valor_1
    global valor_2
    return valor_1+valor_2
def restar():
    global valor_1
    global valor_2
    return valor_1-valor_2
def multiplicar():
    global valor_1
    global valor_2
    return valor_1*valor_2
def dividir():
    global valor_1
    global valor_2
    return valor_1/valor_2
def borrar():
    global entrada
    entrada.delete(0, tk.END)

def agregar_en_pantalla(valor):
    global entrada
    entrada.insert(tk.END,valor)
    
def operar(simbolo):
   global entrada
   global valor_1
   global operacion
   valor_1=float(entrada.get())
   entrada.delete(0,tk.END)
   if simbolo=="/":
       operacion="dividir"
   elif simbolo=="*":
       operacion="multiplicar"
   elif simbolo=="-":
       operacion="restar"
   elif simbolo=="+":
       operacion="sumar"
   print(valor_1)
   print(operacion)

 

def resultado_igual():
    global entrada
    global valor_1
    global operacion
    global resultado
    global valor_2
    valor_2=float(entrada.get())
    entrada.delete(0,tk.END)
    evaluacion= eval(operacion)
    resultado=evaluacion()
    entrada.insert(tk.END, resultado)





#Interfaz
ventana=tk.Tk()
ventana.title("Calculadora grafica")
ventana.configure(bg="lightblue", bd=5)
#Texto
entrada=tk.Entry(ventana,width=30,bd=5, justify="right")
entrada.grid(row=0,column=0, columnspan=4)

#Botones
boton_7=tk.Button(ventana,text="7", width=5, command=lambda:agregar_en_pantalla(7))
boton_7.grid(row=1, column=0)
boton_8=tk.Button(ventana,text="8", width=5,command=lambda:agregar_en_pantalla(8))
boton_8.grid(row=1, column=1)
boton_9=tk.Button(ventana,text="9", width=5,command=lambda:agregar_en_pantalla(9))
boton_9.grid(row=1, column=2)
boton_=tk.Button(ventana,text="/", width=5,command=lambda:operar("/"))
boton_.grid(row=1, column=3)

boton_4=tk.Button(ventana,text="4", width=5,command=lambda:agregar_en_pantalla(4))
boton_4.grid(row=2, column=0)
boton_5=tk.Button(ventana,text="5", width=5,command=lambda:agregar_en_pantalla(5))
boton_5.grid(row=2, column=1)
boton_6=tk.Button(ventana,text="6", width=5,command=lambda:agregar_en_pantalla(6))
boton_6.grid(row=2, column=2)
boton_m=tk.Button(ventana,text="*", width=5,command=lambda:operar("*"))
boton_m.grid(row=2, column=3)

boton_1=tk.Button(ventana,text="1", width=5,command=lambda:agregar_en_pantalla(1))
boton_1.grid(row=3, column=0)
boton_2=tk.Button(ventana,text="2", width=5,command=lambda:agregar_en_pantalla(2))
boton_2.grid(row=3, column=1)
boton_3=tk.Button(ventana,text="3", width=5,command=lambda:agregar_en_pantalla(3))
boton_3.grid(row=3, column=2)
boton_r=tk.Button(ventana,text="-", width=5,command=lambda:operar("-"))
boton_r.grid(row=3, column=3)

boton_punto=tk.Button(ventana,text=".", width=5)
boton_punto.grid(row=4, column=0)
boton_0=tk.Button(ventana,text="0", width=5,command=lambda:agregar_en_pantalla(0))
boton_0.grid(row=4, column=1)
boton_igual=tk.Button(ventana,text="=", width=5,command=resultado_igual)
boton_igual.grid(row=4, column=2)
boton_sum=tk.Button(ventana,text="+", width=5,command=lambda:operar("+"))
boton_sum.grid(row=4, column=3)


boton_borrar=tk.Button(ventana,text="Borrar",width=20, command=borrar)
boton_borrar.grid(row=5, columnspan=4)

ventana.mainloop()
