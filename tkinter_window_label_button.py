# Windows, Labels, Buttons

import sys
from tkinter import *

migui = Tk()
migui.geometry('450x450+800+200')    # geom. 450x450 tamano y 800 +200 ubicacion
migui.title('mi Ventana de Tkinter') #nombre de la ventana

# migui es el nombre de la ventana, se puede poner cualquier cosa

mietiqueta = Label(text='Etiqueta01',fg='red',bg='blue').grid(row=0,column=0,sticky=W)
mietiqueta2 = Label(text='Etiqueta02',fg='red',bg='blue').grid(row=1,column=0,sticky=W)
mietiqueta3 = Label(text='Etiqueta03',fg='red',bg='blue').grid(row=2,column=0,sticky=W)

miboton1=Button(text='OK').grid(row=3,column=0)
miboton2=Button(text='Cancelar').grid(row=3,column=10)

# sticky W para izquierda y E para derecha (West-East)
# place(x=225,y=225) en lugar de grid
#.pack() 
# puede cambiarse .pack() por mietiquet.pack() en otra linea

migui.mainloop() # solo para windows, mac, pycharm

