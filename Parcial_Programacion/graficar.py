from ast import Import
from msilib.schema import Font
from pydoc import plain
import tkinter as tk
from tkinter import messagebox, Canvas, Frame,BOTH, CENTER
import random
from tkinter import Tk, Label, StringVar




#---------------------------
# Funciones Finales
# --------------------------



# -----------------------------
# VENTANA PRINCIPAL
# -----------------------------
# creacion objeto Tk (ventana principal)
ventana_principal = tk.Tk()
# Titulo ventana principal
ventana_principal.title("Graficar")
# dimensiones de la ventana
ventana_principal.geometry("800x580")
# deshabilitar boton maximizar
ventana_principal.resizable(0,0)
# color de fondo ventana principal
ventana_principal.config(bg="Red")



#-----------------------------
# Definir y dar Instrucciones a variables
#-----------------------------
base = 460
altura = 380
x1= StringVar()
y1= StringVar()
x2= StringVar()
y2= StringVar()

def suma ():
    xuno= float(x1.get())
    yuno= float(y1.get())
    xdos= float(x2.get())
    ydos= float(y2.get())
    p= (yuno-xuno)/(ydos-xdos)
    Label(frame_operaciones,text="La pendiente es: "+ str(p), bg='Grey', fg= 'Black', font= ('Chiller', 20,'bold')).place(x=540, y=310)



# Se supone que ubico el punto con un * y luego creo otra funcion que una los dos puntos que marque con una linia
def graficar():
    xuno= float(x1.get())
    yuno= float(y1.get())
    p1= linea2/xuno
    p2= linea1/yuno
    Label(frame_operaciones,text="*"+ str(p1)+str(p2), fg= 'Black', font= ('Chiller', 20,'bold')).place(x=linea2, y=linea1)


# -----------------------------
# FRAME ENTRADA DATOS
# -----------------------------
frame_entrada = tk.Frame(ventana_principal)
frame_entrada.config(bg="black", width=780, height=85)
frame_entrada.place(x=10,y=10)

# Variable Titulo movimiento
incremento = 1
periodo = 60
tamanio_max = 50
tamanio = tamanio_min = 47
def modifica_tamanio():
    global tamanio, incremento
    if tamanio > tamanio_max or tamanio < tamanio_min:
        incremento = -incremento
    tamanio += incremento
    titulo.configure(bg="black", fg="White", font=("Chiller",str(tamanio)))
    titulo.after(periodo, modifica_tamanio)
titulo = tk.Label(frame_entrada,text="Plano Cartesiano")
titulo.pack(expand=True)

# Titulo Lugar
titulo.place(x=230, y=1)

# -----------------------------
# FRAME OPERACIONES
# -----------------------------
frame_operaciones = tk.Frame(ventana_principal)
frame_operaciones.config(bg="Grey", width=780, height=470)
frame_operaciones.place(x=10,y=100)


c = Canvas(frame_operaciones, width = base, height = altura)
c.place(x = 10,y = 10)



# Líneas rectas

linea1 = c.create_line(base/2, 0, base/2, altura/2, fill = "black")
linea2 = c.create_line(base, altura/2, base/2, altura/2, fill = "black")
linea3 = c.create_line(base/2, altura, base/2, altura/2, fill = "black")
linea4 = c.create_line(0,altura/2, base/2, altura/2, fill = "black")

Label(frame_operaciones,text="Ingrese el valor de X1:", bg='black', fg= 'WHITE', font= ('Chiller', 15, 'bold')).place(x=550, y=20)
X1 = tk.Entry(frame_operaciones, font=("arial",10,"bold"), width=10, textvariable= x1, justify= CENTER)
X1.place(x=550, y=50)

Label(frame_operaciones,text="Ingrese el valor de Y1:", bg='black', fg= 'WHITE', font= ('Chiller', 15, 'bold')).place(x=550, y=80)
y1 = tk.Entry(frame_operaciones, font=("arial",10,"bold"), width=10, textvariable= y1, justify= CENTER)
y1.place(x=550, y=110)

Label(frame_operaciones,text="Ingrese el valor de X2:", bg='black', fg= 'WHITE', font= ('Chiller', 15, 'bold')).place(x=550, y=140)
X2 = tk.Entry(frame_operaciones, font=("arial",10,"bold"), width=10, textvariable= x2, justify= CENTER)
X2.place(x=550, y=172)

Label(frame_operaciones,text="Ingrese el valor de Yy:", bg='black', fg= 'WHITE', font= ('Chiller', 15, 'bold')).place(x=550, y=200)
y2 = tk.Entry(frame_operaciones, font=("arial",10,"bold"), width=10, textvariable= y2, justify= CENTER)
y2.place(x=550, y=230)





boton1 = tk.Button(frame_operaciones, text="Calcular Pendiente", command= suma)
boton1.config(bg="black", fg="cyan", font=("Chiller", 20))
boton1.place(x= 80, y=410)

boton2 = tk.Button(frame_operaciones, text="Graficar", command= graficar)
boton2.config(bg="black", fg="cyan", font=("Chiller", 20))
boton2.place(x= 250, y=410)

# -----------------------------
# FRAME RESULTADOS
# -----------------------------




modifica_tamanio()

# desplegar ventana principal y queda a la espera de eventos del usuario
ventana_principal.mainloop()