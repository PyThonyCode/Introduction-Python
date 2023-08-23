print("""
------ SESSION 3: --------
------ + Conjuntos -------
------ + Diccionarios ----""")

conjunto = {1, 2, 3, "arroz", "arroz"}
a = ["a", 3.2]
print(len(conjunto))

for x in conjunto:
    print(x)

print("arroz" in conjunto)
conjunto.add("olla")
print(conjunto)

conjunto.update(a)
print(conjunto)

set3 = conjunto.union(a)
print(set3)


thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(thisdict["brand"])
# x = thisdict.get("model")
x = thisdict.keys()
print(x)

print(x)  # before the change

thisdict["color"] = "white"

print(x)  # after the change

x = thisdict.values()

print(x)

x = thisdict.items()

print(x)

if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")


myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}

print(myfamily)
print(myfamily["child2"]["name"])

child4 = {
    "name": "Pedro",
    "year": 2021
}

myfamily["child4"] = child4
print(myfamily)
# actualizar
myfamily["child4"]["year"] = 2030
print(myfamily["child4"]["year"])
