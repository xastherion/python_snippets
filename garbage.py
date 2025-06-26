import sys
from tkinter import *


root = Tk()
frame1 = Frame(root)
frame2 = Frame(root)
frame3 = Frame(root)
frame4 = Frame(root)

Label (frame1, text='Demostracion').pack()

Entry(frame1, text='AAA').pack(side=LEFT)
Button(frame1, text='BBB').pack(side=RIGHT)

Entry(frame2, text='DDD').pack(side=LEFT, fill=Y)
Button(frame2, text='EEE').pack(side=RIGHT, fill=Y)

Entry(frame3, text='AAA').pack(side=LEFT, fill=Y)
Button(frame3, text='BBB').pack(side=RIGHT, fill=Y)

Entry(frame4, text='DDD').pack(side=LEFT, fill=Y)
Button(frame4, text='EEE').pack(side=RIGHT, fill=Y)

frame1.pack()
frame2.pack()
frame3.pack()
frame4.pack()
# ---------------------------------------------------
mainloop() # this is only a contruction if sometimes dont fuction