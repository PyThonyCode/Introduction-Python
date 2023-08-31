# from numpy import random

"""x = random.randint(40)
print(x)

x = random.randint(40, size=3)
print(x)

x = random.randint(40, size=(2, 3))
print(x)

# valores de 0 a 1

x = random.rand()
print(x)

x = random.rand(3)
print(x)

x = random.rand(2, 3)
print(x)

# Elegir aleatoriamente en un array con choice
x = random.choice([3, 1, 6, 7, 2, 0, 10])
print(x)"""

# DISTRIBUCION ALEATORIA DE DATOS
"""from numpy import random
data = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.5, 0.1], size=100)
print(data)"""

# PERMUTACION DE DATOS CON metodos shufle y permutation


"""arr = np.array([1, 2, 3, 4])
random.shuffle(arr)
print(arr)
arr = np.array([1, 2, 3, 4])
per = random.permutation(arr)
print(per)"""


# DISTRIBUCION NORMAL
from numpy import random
import numpy as np
x = random.normal(size=(2, 4))
print(x)

# con media y desviacion standar

x = random.normal(loc=1, scale=2, size=(2, 3))
print(x)
