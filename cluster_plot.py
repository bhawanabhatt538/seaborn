import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

flights = sns.load_dataset('flights')

print(flights.head())

# flights = flights.pivot('month','year','passengers')
# sns.heatmap(flights)
# plt.show()

# sns.clustermap(flights)
# plt.show()

# sns.clustermap(flights,col_cluster=False)
# plt.show()

# sns.clustermap(flights, row_cluster=False)
# plt.show()

# sns.clustermap(flights ,cmap='coolwarm')
# plt.show()

# #line width

# sns.clustermap(flights ,cmap='coolwarm',linewidth=1)
# plt.show()

# #size
# print(sns.clustermap(flights, cmap='coolwarm', linewidths=1.2, figsize=(6,4)))

#standardize across col or rows
sns.clustermap(data=flights, standard_scale = 1)
plt.show()

sns.clustermap(data=flights, standard_scale = 0)
plt.show()

#normalizing our dataset= z score
sns.clustermap(flights, z_score=0)
plt.show()








