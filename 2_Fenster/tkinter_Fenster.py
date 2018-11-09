#!/usr/bin/python3

# Einfaches Fenster mit Tkinter

import tkinter

# Das Fenster wird in die Variable root geschrieben
root = tkinter.Tk()

# Nun dem Fenster root einen Namen verpassen
root.title("VHS Esslingen - raspikurs")

# Jetzt wird die Größe des Fensters root angepasst
root.geometry('600x300')

# Anschließend noch ein Paar Labels (Schriftfelder) einfügen
tkinter.Label(root, text="Grafikfenster mit TKinter", fg="#0A116B").pack()
tkinter.Label(root, text="\n      Viel Erfolg\n      mit TKinter\n").pack()

# Und das Foto nicht vergessen!
foto = tkinter.PhotoImage(file="logo.png")
tkinter.Label(root, image=foto).pack()


#Nun das Fenster starten
root.mainloop()
