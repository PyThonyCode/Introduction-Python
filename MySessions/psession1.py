from datetime import datetime

print("""
PRACTICA N°1""")

nombre = input("Ingresar nombre: ")
apellido = input("Ingresar apellido: ")
year_nacimiento = int(input("Ingresar año que nacistes: "))
frase_habitual = input("Frase más común: ")
presupuesto = int(input("Ingresar presupuesto: "))


def calcular_edad(year_nacimiento):
    date_now = datetime.now()
    edad = date_now.year - year_nacimiento
    return edad


edad = calcular_edad(year_nacimiento)


def contar_vocales(frase):
    count = 0
    for n in frase:
        print(n)
        if n == "u":
            count += 1
        if n == "a":
            count += 1
    print(f"Conteo: {count}")


def Imprimir():
    print(f"Nombre: {nombre}")
    print(f"Apellido: {apellido}")
    print(f"Año que naciste: {year_nacimiento}")
    print(f"Edad: {edad}")
    print(f"Frase que usas seguido: {frase_habitual}")
    print(f"Conteo de palabra: {len(frase_habitual)}")
    print(
        f"Presupuesto: S/. {presupuesto} al día cuando puede agarrar de su padre xd")

    contar_vocales(frase_habitual)


Imprimir()
