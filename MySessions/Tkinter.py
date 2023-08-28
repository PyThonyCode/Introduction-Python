import tkinter as tk

# VENTANA
"""ventana = tkinter.Tk()
# metodo gemetry para dimension de la interfaz
ventana.geometry("500x300")
ventana.title("SUMATORIA")"""

# EIQUETA
# etiqueta = tkinter.Label(ventana, text="Hola mundo", bg="blue")
# metodo pack
# posiicion con side
# etiqueta.pack(side=tkinter.RIGHT)

# fill es para estirar
# expandir bg en eje x
# etiqueta.pack(fill=tkinter.X)

# expandir bg en eje y
# etiqueta.pack(fill=tkinter.Y, expand=True)

# expandir bg en eje x e y cyubriendo todo
# etiqueta.pack(fill=tkinter.BOTH, expand=True)

# BOTONES
# btn1 = tkinter.Button(ventana, text="Presionar", padx=40, pady=50)
# btn1.pack()

# FUNCIONES Y USO DE BOTON


"""def saludo():
    print("Hola mundo")


btn1 = tkinter.Button(ventana, text="PRESIONAR", command=saludo)"""

# Con parametros


"""def saludo(nombre):
    print("Hola mundo "+nombre)


btn1 = tkinter.Button(ventana, text="PRESIONAR",
                      command=lambda: saludo("Thony"))"""


# Con caja de texto y botones

"""txtinput = tkinter.Entry(ventana, font="Normal 26")
txtinput.pack()
txtlabel = tkinter.Label(ventana)
txtlabel.pack()


def saludo():
    texto = txtinput.get()
    txtlabel["text"] = texto


btn1 = tkinter.Button(ventana, text="PRESIONAR", command=saludo)
btn1.pack()"""

# metodo grid para dividir la ventana en columna y filas, y poder posicionr un widget

"""btn1 = tkinter.Button(ventana, text="Boton1", padx=50, pady=50)
btn2 = tkinter.Button(ventana, text="Boton2", padx=40, pady=50)
btn3 = tkinter.Button(ventana, text="Boton3", padx=30, pady=50)

btn1.grid(row=0, column=0)
btn2.grid(row=1, column=1)
btn3.grid(row=1, column=2)"""


# LO QUE SABEMOS
# DATO 1
"""
txtlabel1 = tkinter.Label(ventana, text="Número 1  =  ")
txtinput1 = tkinter.Entry(ventana, font="Normal 16", width=8)
txtlabel1.grid(row=0, column=0)
txtinput1.grid(row=0, column=1)
# DATO 2
txtlabel2 = tkinter.Label(ventana, text="Número 2  =  ")
txtinput2 = tkinter.Entry(ventana, width=8, font="Normal 16")
txtlabel2.grid(row=1, column=0)
txtinput2.grid(row=1, column=1)

txtsalida = tkinter.Label(ventana)


def sumar():
    dato1 = float(txtinput1.get())
    dato2 = float(txtinput2.get())
    suma = dato1 + dato2
    txtsalida["text"] = f"La suma es {str(suma)}"
    txtsalida.grid(row=0, column=2)


btn1 = tkinter.Button(text="SUMAR", width=12,
                      command=lambda: sumar())
btn1.grid(row=2, column=0)

ventana.mainloop()"""


def sumar():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    resultado = num1 + num2
    label_resultado.config(text=f"Resultado: {resultado}")


# Crear la ventana
ventana = tk.Tk()
ventana.title("Sumadora")

# Etiquetas y campos de entrada
label_num1 = tk.Label(ventana, text="Número 1:")
label_num1.pack()

entry_num1 = tk.Entry(ventana)
entry_num1.pack()

label_num2 = tk.Label(ventana, text="Número 2:")
label_num2.pack()

entry_num2 = tk.Entry(ventana)
entry_num2.pack()

# Botón para sumar
boton_sumar = tk.Button(ventana, text="Sumar", command=sumar)
boton_sumar.pack()

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(ventana, text="Resultado:")
label_resultado.pack()

# Iniciar la interfaz gráfica
ventana.mainloop()
