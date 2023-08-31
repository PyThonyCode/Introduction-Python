""""DISTRIBUCION NORMAL"""

import seaborn as sns
import matplotlib.pyplot as plt
from numpy import random
# dato aleatorio
"""data = random.normal(size=100)"""
# distribucion normal estandar media = 0 y desviacion standar = 1

data = random.normal(loc=0, scale=1, size=20)
print(data)
