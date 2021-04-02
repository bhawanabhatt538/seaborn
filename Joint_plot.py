import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

print(tips.head())

iris = sns.load_dataset('iris')
print(iris.head())

sns.jointplot(x='total_bill' , y='tip', data = tips)
plt.show()

sns.jointplot(x='sepal_length', y='sepal_width',data = iris)
plt.show()

sns.jointplot(x='total_bill' , y='tip', data = tips , kind ='reg')
plt.show()

sns.jointplot(x='total_bill' , y='tip' , data = tips , kind='hex')
plt.show()

sns.jointplot(x='total_bill' , y='tip' , data = tips , kind='kde')
plt.show()


sns.jointplot(x='sepal_length', y='sepal_width', data=iris, kind='kde' )
plt.show()

#STAT_FUNC
# from scipy.stats import spearmanr
# sns.jointplot(x='total_bill', y='tip', data=tips, stat_func=spearmanr)
# plt.show()

# sns.jointplot(x='size', y='total_bill', data=tips, stat_func=spearmanr)
# plt.show()

sns.jointplot(x='total_bill' , y='tip', data = tips , ratio=1, size=4)
plt.show()
