from tkinter import *

def escribir():
    lista = [var_name.get(), var_preis.get(), '\n']  # import values from entries
    archivo = open("csv_ziel.csv", 'a')
    archivo.write("\t".join(lista))                  # write lista in archivo

def ende(): #esta funcion terminatodo con el boton "Exit"
    master.destroy()


master = Tk()

var_name = StringVar()
entry_name = Entry(master, textvariable=var_name).place(x=10, y=10,  width=100, height=30)

var_preis = StringVar()
entry_preis = Entry(master, textvariable=var_preis).place(x=10, y=40,  width=100, height=30)

Button(master, text='Schreiben', command=escribir).place(x=10,  y=70,   width=100, height=30)
Button(master, text='Ende',      command=ende).    place(x=10, y=100,   width=100, height=30)

master.mainloop()
