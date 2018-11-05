#!/usr/bin/python3

# Einfaches Fenster mit Tkinter

import Tkinter

# Das Fenster wird in die Variable root geschrieben
root = Tkinter.Tk()

# Nun dem Fenster root einen Namen verpassen
root.title("VHS Esslingen - raspikurs")

# Jetzt wird die Größe des Fensters root angepasst
root.geometry('600x300')

# Anschließend noch ein Paar Labels (Schriftfelder) einfügen
Tkinter.Label(root, text="Grafikfenster mit TKinter", fg="#0A116B").pack()
Tkinter.Label(root, text="\n      Viel Erfolg\n      mit TKinter\n").pack()

# Und das Foto nicht vergessen!
foto = Tkinter.PhotoImage(file="logo.png")
Tkinter.Label(root, image=foto).pack()


#Nun das Fenster starten
root.mainloop()
