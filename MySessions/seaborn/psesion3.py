import matplotlib.pyplot as plt
from numpy import random
import seaborn as sns
# Parámetros de la distribución binomial
n = 10  # Número de ensayos
p = 0.5  # Probabilidad de éxito en cada ensayo
tamanio_muestra = 1000
datos_binomiales = random.binomial(n, p, tamanio_muestra)
# Visualizar la distribución utilizando Seaborn
sns.set(style="whitegrid")
sns.histplot(datos_binomiales, bins=range(0, n+2), kde=False)
plt.title("Distribución Binomial")
plt.xlabel("Número de Éxitos")
plt.ylabel("Frecuencia")
plt.show()
