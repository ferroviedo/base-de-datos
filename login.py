import tkinter
import tkinter as tk
import sqlite3
from tkinter import *
from tkinter import ttk
ventana = tkinter.Tk()
ventana.title ("Login")
ventana.geometry ("450x250+500+250")
ventana.config(bg = "skyblue3")
boton = ttk.Button(text="Registrarte")
boton.place(x=185, y=175)
ventana.resizable(0, 0)
Label(ventana, text = "Usuario:").pack()
caja1 = Entry(ventana, bg = "lightblue")
caja1.pack()
Label(ventana, text = "Contraseña:").pack()
caja2 = Entry(ventana,  bg = "lightblue",show = "*")
caja2.pack()
Label(ventana, text = "Telefono:").pack()
caja3 = Entry(ventana, bg = "lightblue")
caja3.pack()
Label(ventana, text = "Dni:").pack()
caja4 = Entry(ventana, bg = "lightblue")
caja4.pack()

bd = sqlite3.connect("login.py")
cursor =  bd.cursor()
cursor.execute("SELECT * FROM Datos")
print(cursor)
datos = fetchone()
print(datos)
bd.commit()

cursor.execute("INSERT INTO Datos VALUES " \
            "('fer',12345,'1122334455','9090909')")

    
ventana.mainloop()