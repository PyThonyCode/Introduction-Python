# MOSTRANDO DATOS CON CHOICE Y LUEGO TRAZARLO CON SEABORN AL FINAL MOSTRARLO
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

data = random.choice([1, 2, 3, 4, 5, 6], p=[
                     0.2, 0.1, 0.2, 0.1, 0.1, 0.3], size=40)
print(data)
sns.displot(data)
plt.show()
