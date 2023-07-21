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

print("+ Booleanos")
print(10 == 9)
print(10 > 3)
print("+ Operadores")
a = 10
b = 6
suma = a + b
resta = a - b
mult = a * b
div = a/b
mod = a % b
a -= 3
b -= 2
exp = b ** a
flord = a//b
print(suma)
print(resta)
print(mult)
print(div)
print(mod)
print(f"a:{a}, b:{b}")
print(exp)
print(flord)

palabra = "hola mundo"
print("hola" in palabra)
print("hola mundo" is palabra)
