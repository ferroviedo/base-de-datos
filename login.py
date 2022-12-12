import tkinter
import tkinter as tk
import sqlite3
from tkinter import *
from tkinter import ttk
#cursor = conexion.cursor()
#cursor.execute
ventana = tkinter.Tk()
ventana.title ("Login")
ventana.geometry ("450x250+500+250")
ventana.config(bg = "skyblue3")
boton = ttk.Button(text="Registrarte")
boton.place(x=185, y=195)
ventana.resizable(0, 0)
Label(ventana, text = "Nombre de Usuario:").pack()
caja1 = Entry(ventana)
caja1.pack()
Label(ventana, text = "Contraseña:").pack()
caja2 = Entry(ventana, show = "*")
caja2.pack()
Label(ventana, text = "Numero de telefono:").pack()
caja3 = Entry(ventana)
caja3.pack()
Label(ventana, text = "Dni:").pack()
caja4 = Entry(ventana)
caja4.pack()


def Login(self):
    bd = sqlite3.connect("/Carpeta Personal/Documentos/Login.bd")
    c = db.cursor()
    
    
ventana.mainloop()