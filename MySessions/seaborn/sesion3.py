# DISTRIBUCION BINOMIAL
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
"""
Describe el resultado de escenarios binarios, por ejemplo, lanzamiento de una moneda, ya sea cara o cruz.

Tiene tres parámetros:

n - número de ensayos.

p - probabilidad de ocurrencia de cada ensayo (por ejemplo, para el lanzamiento de una moneda de 0,5 cada uno).

size - La forma de la matriz devuelta."""

"""x = random.binomial(n=10, p=0.5, size=10)
print(x)"""
"""sns.distplot(random.binomial(n=10, p=0.5, size=1000), hist=True, kde=False)
plt.show()"""

# Distribución normal y binomial
"""La principal diferencia es que la distribución normal es continua mientras que el binomio es discreto, Pero si hay suficientes puntos de datos, será bastante similar a la distribución normal con cierta loc y escala."""

sns.distplot(random.normal(loc=50, scale=5, size=1000),
             hist=False, label="normal")
sns.distplot(random.binomial(n=100, p=0.5, size=1000),
             hist=False, label="binominal")
plt.show()
