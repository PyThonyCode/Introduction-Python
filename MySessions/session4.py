"""Nivel Básico
1. Escribir un programa que pida al usuario una palabra y la cantidad de veces que desea que se
muestre."""

# palabra = input("Ingresar palabra: ")
# repetir = int(input("Cuanto quieres repetirlo: "))
# for x in range(repetir):
#   print(palabra)

"""
2. Preguntar al usuario su edad, luego imprimir todos los años que ha cumplido (desde 1 hasta su
edad)."""

# usuario = int(input("Ingresar tu edad: "))
# print("Pasastes estos años: ")
# for x in range(1, usuario+1):
#    print(x)

""" 3. Ingresar número entero positivo, luego imprimir todos los números impares desde 1 hasta ese
número separados por “;”."""

# num = int(input("Ingresar numero: "))
# impares = []
# for x in range(1, num+1):
#    if x % 2 == 1:
#        impares.append(str(x))

# print(" ; ".join(impares))

""" 
4. Ingresar un número entero positivo, luego imprimir la cuenta atrás desde ese número hasta
cero separados por comas."""

# num = int(input("Ingresar numero: "))
# datos = []

# while num > 0:

#    datos.append(str(num))
#    num -= 1

# print(" ; ".join(datos))

"""
5. Ingresar una cantidad a invertir, el interés anual y el número de años, luego imprima el capital
obtenido por cada año """
# Pedir al usuario que ingrese la cantidad a invertir, el interés anual y el número de años
# cantidad_invertir = float(input("Ingrese la cantidad a invertir: "))
# interes_anual = float(input("Ingrese el interés anual (%): "))
# num_anios = int(input("Ingrese el número de años: "))

# Convertir el interés anual a decimales
# interes_decimal = interes_anual / 100

# Imprimir encabezado
# print("Año\tCapital")

# Calcular y mostrar el capital obtenido por cada año
# for anio in range(1, num_anios + 1):
#    capital_obtenido = cantidad_invertir * (1 + interes_decimal) ** anio
#    print(f"{anio}\t{capital_obtenido:.2f}")

"""
6. Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de
ciclos """


"""
7. Mostrar todas las palabras que introduzca el usuario hasta que el usuario escriba “salir” """

# palabra = input("Ingresar una palabra: ")

# while palabra != "salir":
#    print(palabra)
#    palabra = input("Ingresar una palabra: ")

"""
8. Crear una variable contraseña en el cual almacene lo siguiente “SENATI”, luego preguntar al
usuario por la contraseña hasta que introduzca la contraseña correcta"""

# password = "SENATI"

# while True:
#    pass_ingresado = input("Ingresar la contraseña: ")

#    if pass_ingresado == password:
#        print("Ingresaste a tu cuenta")
#        break
#    else:
#         print("No es correcto la contraseña")


"""Nivel Intermedio
1. Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar"""

# for x in range(1, 20):
#    if x % 2 == 0:
#        print(f"{x} es par")
#    else:
#        print(f"{x} es impar")

"""
2. Modificar el ejercicio 1 para poder ingresar el último número y luego imprimir por pantalla si
es par o impar
3. En un ciclo for mostrar los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3"""
# print("Número\tPotencia")
# for x in range(1, 6):
#    print(f"{x}\t{x**3}")

"""
4. Imprimir la tabla de multiplicar del 1 al 10"""

# print("""
# ******************************
# **** TABLA DE MULTIPLICAR ****
# ******************************""")

# for x in range(1, 11):
#    for y in range(0, 13):
#        print(f"{x}*{y} = {x*y}")

"""
5. Utilizar un ciclo while para realizar la factorial de un número guardado en una variable, sólo si
la variable es mayor a 0"""

# num = 5
# factorial = 1
# while num > 0:
#    factorial *= num
#    num -= 1
# print(factorial)

"""
6. Crear una lista1 con n elementos y luego ingresar los números enteros del 10 al 50, luego crear
otra lista2 para invertir los elementos de la lista1
7. Imprimir los números primos existentes entre 1 y n, recuerda que n es el último número.
8. ¿Se puede mejorar el proceso del ejercicio7? Utilizar las sentencias break
9. Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro
del rango de números de 100 a 300
10. Crear un ciclo while que encuentre"""

print("""
++++++++++    CALCULADORA   +++++++++
++++++++++ DE 4 OPERACIONES +++++++++
+ 1 - SUMA                          +
+ 2 - RESTA                         +
+ 3 - MULTPLICACION                 +
+ 4 - DIVISION                      +""")

op = input("Ingresar el número de operación: ")

if op == "4":
    print("""
    ++++ DIVISION DE 2 NUMEROS +++++""")
    num1 = int(input("Ingresar primer número: "))
    num2 = int(input("Ingresar primer número: "))

    if num1 != 0 and num2 != 0:
        print(f"La division es {num1/num2}")
    else:
        print("Los números no deben ser 0")
        pass
else:
    print("salida")
