import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

tips= sns.load_dataset('tips')

#box plot for single variable
print(tips.head())

#let's looking at a single horizontal box plot for let's say size
sns.boxplot(tips['size'])
plt.show()

#single horizontal box plot for some other variable
sns.boxplot(x=tips['total_bill'])
plt.show()


#drow boxplot for two variable
sns.boxplot(x='sex',y='total_bill',data=tips)
plt.show()
#box plot for day versus total bill
sns.boxplot(x='day',y='total_bill',data=tips)
plt.show()

sns.boxplot(x='day',y='total_bill',data=tips,hue='sex',palette='husl')
plt.show()

sns.boxplot(x='day',y='total_bill',data=tips,hue='time')
plt.show()








