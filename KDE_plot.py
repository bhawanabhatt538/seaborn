import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

mean = [0,0]
cov = [[0.2,0],[0,3]]

x_axis, y_axis = np.random.multivariate_normal(mean, cov, size = 40).T
# sns.kdeplot(x_axis)
# plt.show()

# sns.kdeplot(y_axis)
# plt.show()

# #for color

# sns.kdeplot(x_axis, shade=True, color='green')
# plt.show()

# sns.kdeplot(y_axis, shade=True, color='purple')
# plt.show()

# #KDE plot of both variables
# sns.kdeplot(x_axis, y_axis)
# plt.show()

# sns.kdeplot(x_axis, y_axis, shade= True)
# plt.show()

# #color map for kde plot
# sns.kdeplot(x_axis, y_axis, cmap='RdBu')
# plt.show()

# sns.kdeplot(x_axis, y_axis, cmap='coolwarm')
# plt.show()

# #change the number of contour line by passing the
# sns.kdeplot(x_axis, y_axis, n_levels=35)
# plt.show()

# sns.kdeplot(x_axis, bw=1.5)
# plt.show()

# sns.kdeplot(x_axis, bw=0.1)
# plt.show()

iris = sns.load_dataset('iris')
setosa = iris.loc[iris.species == 'setosa']
versicolor = iris.loc[iris.species == 'versicolor']

sns.kdeplot(setosa.petal_length, setosa.petal_width)
sns.kdeplot(versicolor.petal_length, versicolor.petal_width)
plt.show()

#pass color map

sns.kdeplot(setosa.petal_length, setosa.petal_width, cmap = 'coolwarm')
sns.kdeplot(versicolor.petal_length, versicolor.petal_width, cmap='RdBu',shade=True)
plt.show()


#e




