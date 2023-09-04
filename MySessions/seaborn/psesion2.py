import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
"""EJERCICIOS DE DISTRIBUCION NORMAL"""
# ejercicio 1
"""

media = 0
desv_standar = 1
muestra = 1000

datos = random.normal(media, desv_standar, muestra)
print(datos)
sns.set(style="whitegrid")
sns.histplot(datos)
plt.title("Distribución Normal")
plt.xlabel("Valor")
plt.ylabel("Frecuencia")
plt.show()"""

# ejercicio 2

muestra = 1000
""""dato 1"""
media1 = 0
desv_standar1 = 1
datos1 = random.normal(media1, desv_standar1, muestra)

""""dato 2"""
media2 = 2
desv_standar2 = 1.5
datos2 = random.normal(media2, desv_standar2, muestra)

""""etiquetas"""
etiquetas = ["Distribucion 1", "Distribucion 2"]

datos_combinados = np.concatenate([datos1, datos2])
etiqueta_combinada = np.concatenate(
    [[etiquetas[0]]*muestra, [etiquetas[1]]*muestra])

# Crear un gráfico de violin plot utilizando Seaborn
sns.set(style="whitegrid")
# sns.violinplot(x=etiqueta_combinada, y=datos_combinados)
# sns.histplot(datos_combinados, kde=True)
# sns.boxplot(x=etiqueta_combinada, y=datos_combinados)

# usando el violintplot con valores

ax = sns.violinplot(x=etiqueta_combinada, y=datos_combinados)


for i, label in enumerate(etiquetas):
    datos_etiqueta = datos_combinados[etiqueta_combinada == label]
    plt.annotate(f"Media {label}: {np.mean(datos_etiqueta):.2f}",
                 xy=(i, np.mean(datos_etiqueta)), xytext=(5, 5),
                 textcoords='offset points', ha='center', va='bottom')

plt.title("Comparación de Distribuciones Normales")
plt.xlabel("Distribuciones")
plt.ylabel("Valores")
plt.show()
