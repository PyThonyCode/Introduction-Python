import tkinter as tk


def salida():
    print(txt_input.get())


interfaz = tk.Tk()
txt_input = tk.Entry(interfaz)
txt_input.pack()
boton = tk.Button(interfaz, text="INGRESAR", command=salida)
boton.pack()
interfaz.mainloop()
