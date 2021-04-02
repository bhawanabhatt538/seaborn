import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

flights = sns.load_dataset('flights')

print(flights.head())



#standardize across col or rows
sns.clustermap(data=flights, standard_scale = 1)
plt.show()

sns.clustermap(data=flights, standard_scale = 0)
plt.show()

#normalizing our dataset= z score
sns.clustermap(flights, z_score=0)
plt.show()

sns.clustermap(flights, z_score=1)
plt.show()

