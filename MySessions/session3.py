print("""
------ SESSION 3: --------
------ + Conjuntos -------
------ + Diccionarios ----""")

conjunto = {1, 2, 3, "arroz", "arroz"}
print(len(conjunto))

for x in conjunto:
    print(x)

print("arroz" in conjunto)
conjunto.add("olla")

print(conjunto)
