print("""
------ SESSION 2: --------
------ + Listas ----------
------ + Tuplas ----------""")

print("---------------------- Listas --------------------------")

mylist = ["Lopez", 32, 3.3, -1, True, "Lopez", "moshito"]
print(f"Tamaño de la lista: {len(mylist)}")
print(mylist)
print(f"Primer dato : {mylist[0]}")
print(f"Primer dato : {mylist[-2]}")
print(f"Primer dato [1:4] : {mylist[1:4]}")
print(f"Primer dato [:3] : {mylist[:3]}")

if "moshito" in mylist:
    print("si está")

mylist[2] = "Sheila"
mylist.append("orange")
print(mylist)

print("----- FUNCIONES ------")
print(f"1. len(mi lista)= tamaño de mi lista : {len(mylist)}")

print("------ METODOS -------")
a = "arroz"
mylist.append(a)
print(f"1. list.append(dato)= Añadir dato a mi lista : {mylist}")
print(f"2. list.count(dato)=Buscar dato de mi lista : {mylist.count('Lopez')}")
print(
    f"3. list.index(dato)= Saber posicion de dato de mi lista : {mylist.index(True)}")

a = "pelotas"
mylist.insert(1, a)
print(
    f"4. list.insert(index,dato)= Ingresar dato en cualquier posicion de lista : {mylist}")

mylist.remove('pelotas')
print(
    f"5. list.remove(dato)= Sacar dato de mi lista : {mylist}")

print("------ USO DE FOR -------")

for n in mylist:
    print(n)

print("---------------------- Tuplas --------------------------")

mytuple = ("orange", 2, "orange")

print("----- FUNCIONES ------")
print(f"1. len(mi lista)= tamaño de mi lista : {len(mytuple)}")
a = "rice"
print(f"1. dato.add(mi tupla)= Agregar dato : {mytuple}")

print("------ METODOS -------")
print(
    f"1. mitupla.count(dato)= Contar datos repetidos : {mytuple.count('orange')}")
