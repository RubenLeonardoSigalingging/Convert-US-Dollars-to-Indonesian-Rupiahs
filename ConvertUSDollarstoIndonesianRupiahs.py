#!/usr/bin/env python3


def Convert_US_Dollars_to_Indonesian_Rupiahs(created_by="Ruben Leonardo Sigalingging."):
	from os import system
	system("pip install tk")
	system("pip install pyfiglet")
	system("clear")


	def USD_to_IDR(created_by="Ruben Leonardo Sigalingging."):
		ubah_angka=dollars.get()
		ubah_ke_dollar=float(ubah_angka)*14871.91
		text_string_program.set(str(ubah_ke_dollar))
		label_program_ke_2.config(font=("Helvetica",18,"bold","italic"),fg="green")
		# label_program_ke_2.save("Hasil.txt")

	# IMPORT MODULE TKINTER
	import tkinter as tk
	jendela=tk.Tk()


	# UBAH JUDUL PROGRAM
	jendela.title("US Dollars to Indonesian Rupiahs")


	# UBAH UKURAN
	jendela.geometry("800x300")


	# UBAH LABEL PROGRAM ATAU TOOLS
	label_program=tk.Label(jendela,text="US Dollars",font=("Helvetica",18,"bold","italic"),fg="chocolate")
	label_program.pack()


	# BUAT TOMBOL UNTUK USER MENGINPUT USD
	dollars=tk.Entry(jendela,font=("Helvetica",18,"bold","italic"),width=8,justify=tk.CENTER)
	dollars.pack()


	# BUAT TOMBOL PROGRAM NYA
	tombol_program=tk.Button(jendela,text="to",command=USD_to_IDR)
	tombol_program.pack()


	# BUAT STRING VARIABEL
	text_string_program=tk.StringVar()
	text_string_program.set("IDR")


	label_program_ke_2=tk.Label(jendela,text="IDR",font=("Helvetica",18,"bold","italic"),textvariable=text_string_program,fg="chocolate")
	label_program_ke_2.pack()
	# label_program_ke_2=tk.Label(jendela,font=("Helvetica",18,"bold","italic"),textvariable=text_string)

	jendela.mainloop()
Convert_US_Dollars_to_Indonesian_Rupiahs()