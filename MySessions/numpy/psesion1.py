# Ejercicio 1.1: Suma y Promedio
"""import numpy as np

arr = np.array([3, 5, 6, 1, 4, 11, 2])
suma = np.sum(arr)
promedio = np.mean(arr)
print("Arreglo de números:", arr)
print(f"La suma es {suma}, y el promedio es {promedio}")"""

# Ejercicio 1.2: Suma y Promedio con valores random
"""import numpy as np
from numpy import random
arr = random.randint(20, size=4)
suma = np.sum(arr)
promedio = np.mean(arr)
print(f"Mi areglo es: {arr}")
print(f"La suma es: {suma}")
print(f"Promedio es: {promedio}")"""

# Ejercicio 2: Operaciones Elementales

import numpy as np
arr1 = np.array([[1, 2, 3], [4, 5, 1]])
arr2 = np.array([[5, 2, 1], [2, 1, 3]])

suma_elemento = arr1 + arr2
print(type(suma_elemento))
print(f"La suma es: {suma_elemento}")
numeros_aleatorios = np.random.rand(5)
print(numeros_aleatorios)
