#!/usr/bin/python3
# einfaches Fenster mit tkinter

from tkinter import *

root = Tk()

root.title("VHS Esslingen - raspikurs")
root.geometry('1024x768')

Label(root, text="Grafikfenster mit TKinter", fg="#0A116B").pack()
Label(root, text="\n      Viel Erfolg\n      mit TKinter\n").pack()

foto = PhotoImage(file="VHSTechnikSchule.gif")
Label(root, image=foto).pack()

root.mainloop()