"""class Producto:
    def __init__(self, color):
        self.color = color
        print(self.color)


ob1 = Producto("azul")


class Persona:
    nombre = ""
    edad = 0

    def mostrar_info(self, nombre, edad):
        print(self.nombre)
        print(self.edad)


jorge = Persona()
jorge.edad = 22
jorge.nombre = "Jorge"

jorge.mostrar_info(jorge.nombre, jorge.edad)"""

print("""
*********************************
* SISTEMA DE VENTA REST. PEPITO *
*********************************""")
print("Hola mi nombre es SOFIA soy tu asistente")
nombre = input("Cual es su nombre? ")

print("Muy bien", nombre, "esta es la lista de nuestro menu")

print("""
*******************************
************ MENU *************
*-----------------------------*
* 1-Arroz chaufa - 13 soles   *
* 2-arroz con pollo - 10 soles*
* 3-chicharron - 15 soles     *
* 4-cabrito    -    20 soles  *
* 5-Lomo saltado -  18 soles  *
* 6-salir del sistema         *
*******************************""")

op = input("Ingrese el numero del plato, por favor ")
while op > "0" and op < "6":
    if op == "1":
        precio = 13
        plato = "Arroz chaufa"
    elif op == "2":
        precio = 10
        plato = "arroz con pollo"
    elif op == "3":
        precio = 15
        plato = "chicharron"
    elif op == "4":
        precio = 20
        plato = "cabrito"
    elif op == "5":
        precio = 18
        plato = "Lomo saltado"
    else:
        print("Muchas gracias ", nombre, "espero haber sido de ayuda")
        break

    cant = int(input("Ingresar la cantidad de platos"))

    print("*******BOLETA DE VENTA ********")
    print("Descripcion del plato:  ", plato)
    print("Costo del plato:  ", precio)
    print("Cantidad: ", cant)
    print("Total: ", precio*cant)

    op = input("Ingrese el numero del plato, por favor ")
