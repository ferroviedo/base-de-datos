import tkinter
import tkinter as tk
import sqlite3
from tkinter import *
from tkinter import ttk

def escribir():  
    nombre = caja1.get()
    apellido = caja2.get()
    telefono = caja3.get()
    dni = caja4.get()
    print(nombre,apellido,telefono,dni)
    bd = sqlite3.connect('login.bd')
    cur = bd.cursor()
    sql = 'INSERT OR IGNORE INTO login (Nombre, Apellido, Telefono, Dni) VALUES ("{}", "{}", {}, {});'
    cur.execute(sql.format(nombre,apellido,telefono,dni))
    bd.commit()
    bd.close()
    
#def leer():
 #   respuesta.get(*)
    
ventana = tkinter.Tk()
ventana.title ("Login")
ventana.geometry ("450x250+500+250")
ventana.config(bg = "skyblue3")
boton = ttk.Button(text="Guardar", command = escribir)
boton.place(x=245, y=175)
boton = ttk.Button(text="Buscar")
boton.place(x=110, y=175)
ventana.resizable(0, 0)
Label(ventana, text = "Nombre:", bg = "skyblue3").pack()
caja1 = Entry(ventana, bg = "lightblue")
caja1.pack()
Label(ventana, text = "Apellido:", bg ="skyblue3").pack()
caja2 = Entry(ventana,  bg = "lightblue")
caja2.pack()
Label(ventana, text = "Telefono:", bg = "skyblue3").pack()
caja3 = Entry(ventana, bg = "lightblue")
caja3.pack()
Label(ventana, text = "Dni:", bg = "skyblue3").pack()
caja4 = Entry(ventana, bg = "light blue")
caja4.pack()

lista=["46502154", "47171797",]
combo = ttk.Combobox(values=lista)
combo.place(x=130, y=210)

ventana.mainloop()