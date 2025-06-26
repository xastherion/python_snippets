import sys
from tkinter import *

mi_gui= Tk()
mi_gui.geometry('300x100+30+30') # Opcional para definir tamano-x y posicion+ de la ventan
mi_gui.title('Nombre de Ventana')

mi_entrada=Entry(mi_gui)
mi_entrada.insert(END, 'Texto por defecto')
mi_entrada.place(x=50,y=30)

# pack is a easy version, another posibilities are grid and place
# place use coordenates and grid positions

mi_gui.mainloop() # this is only a contruction if sometimes dont fuction