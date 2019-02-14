from tkinter import *

def ende(): 
    master.destroy()

master = Tk()
Button(master, text='Ende', command=ende).place(x=10, y=10,   width=50, height=30)
mainloop()
