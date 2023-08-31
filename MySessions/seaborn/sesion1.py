import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random

"""sns.distplot([0, 1, 2, 3, 4, 5, 6, 7, 8], hist=False)
plt.show()"""

# sns.distplot(random.normal(size=100), hist=False)
sns.displot(random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.5, 0.1], size=100))
plt.show()
