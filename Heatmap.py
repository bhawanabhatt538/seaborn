import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

normal = np.random.rand(12,15)
print(normal)

# # sns.heatmap(normal)
# # plt.show()

# # sns.heatmap(normal ,annot = True)
# # plt.show()

# # sns.heatmap(normal, vmin = 0, vmax=2)
# # plt.show()

# # sns.heatmap(normal, vmin = 0, vmax=3)
# # plt.show()


# flights = sns.load_dataset('flights')
# print(flights)

# # print(flights.head())
# # print(flights.tail())

flights = flights.pivot('month','year','passengers')
sns.heatmap(flights)
plt.show()

sns.heatmap(flights, linewidths = 0.9,annot = True, fmt ='d', vmin=100, vmax=650)
plt.show()

sns.heatmap(flights, cmap='summer', annot=True, fmt='d')
plt.show()

sns.heatmap(flights , center=flights.loc['Jun',1954], annot=True)
plt.show()


sns.heatmap(flights , center=flights.loc['Jun',1954], annot=True,fmt='d')
plt.show()


sns.heatmap(flights , center=flights.loc['Jun',1954], annot=True,fmt='d',cbar=False)
plt.show()



