#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Datei: vorwiderstand.py



from time import sleep

print("raspi Kurs Esslingen")

sleep(3)
weiter="j"
while weiter=="j":
	print()
	print("Vorwiderstandsberechnung")

	#Eingabe
	eingabe = input("Eingabe Batteriespannung (x.x): ")
	u_batt = float(eingabe)

	eingabe = input("Eingabe LED Spannung (x.x): ")
	u_led = float(eingabe)

	eingabe = input("Eingabe LED Strom in mA (x.x): ")
	i_led = float(eingabe)

	#Kontrollausgabe
	print()
	print("Batteriespannung U_Batt: {}V".format(u_batt))
	print("Vorwärtsspannung LED: {}V".format(u_led))
	print("Vorwärtsstrom I_F: {}mA".format(i_led))

	#Ergebnisausgabe
	print()
	print("--> benötigter Vorwiderstand: {0:5.0f} OHM".format((u_batt - u_led)/i_led*1000))
	print("                              {0:1.3f} Watt".format((u_batt - u_led)*i_led/1000))

	print()
	weiter = input("Weiter j/n: ")

print("Tschüß")