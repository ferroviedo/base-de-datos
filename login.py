import tkinter
import tkinter as tk
import sqlite3
from tkinter import *
from tkinter import ttk

def escribir():  
    nombre = caja1.get()
    apellido = caja2.get()
    dni = caja3.get()
    print(nombre,apellido,dni)
    
def leer():
    respuesta.get(*)
    
ventana = tkinter.Tk()
ventana.title ("Login")
ventana.geometry ("450x250+500+250")
ventana.config(bg = "skyblue3")
boton = ttk.Button(text="Guardar", command = escribir)
boton.place(x=245, y=150)
boton = ttk.Button(text="Buscar")
boton.place(x=110, y=150)
ventana.resizable(0, 0)
Label(ventana, text = "Nombre:", bg = "skyblue3").pack()
caja1 = Entry(ventana, bg = "lightblue")
caja1.pack()
Label(ventana, text = "Apellido:", bg ="skyblue3").pack()
caja2 = Entry(ventana,  bg = "lightblue")
caja2.pack()
Label(ventana, text = "Dni:", bg = "skyblue3").pack()
caja3 = Entry(ventana, bg = "lightblue")
caja3.pack()

lista=["0", "1", "2",]
combo = ttk.Combobox(values=lista)
combo.place(x=130, y=190)

    

    
ventana.mainloop()