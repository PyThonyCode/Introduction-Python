print("""
------ SESSION 1: --------
---- + Variables ---------
---- + Tipo de Datos -----
---- + Cadenas -----------
---- + Booleanos ---------
---- + Operadores --------""")

print("+ Variables")
nombre = "Anthony"
a = "Hola " + nombre
edad = 23
b = a + " y tengo " + str(edad) + " años"
print(b)
print(type(b))
print(type(edad))
print("+ Tipos de datos")
x = "Hola"
print(type(x))
x = ["Hola", "eo"]
print(type(x))
x = 32
print(type(x))
x = 32.1
print(type(x))

print("+ Cadenas")
cadena = "Hola mundo"
print(cadena[1])
for i in cadena:
    print(i)

print(len(cadena))
