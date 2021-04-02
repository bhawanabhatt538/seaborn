import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
sns.FacetGrid(tips, row='smoker', col='time')
plt.show()
print(tips.head())
# x = sns.FacetGrid(tips, row='smoker', col='time')
# x = x.map(plt.hist, 'total_bill')
# plt.show(x)

# x = sns.FacetGrid(tips, row='smoker', col='time')
# x = x.map(plt.hist, 'total_bill',color='green')
# plt.show(x)

# x = sns.FacetGrid(tips, row='smoker', col='time')
# x = x.map(plt.hist, 'total_bill',color='blue',bins=15)
# plt.show(x)

# LET'S TAKE ANOTHER FUNCTION
# x = sns.FacetGrid(tips, row='smoker', col='time')
# x = x.map(plt.scatter, 'total_bill', 'tip')
# plt.show(x)

# x = sns.FacetGrid(tips, row='smoker', col='time')
# x = x.map(sns.regplot, 'total_bill', 'tip')
# plt.show(x)

#ADD HUE FUNCTION
# x = sns.FacetGrid(tips, hue='smoker', col='time')
# x = x.map(plt.scatter, 'total_bill', 'tip')
# plt.show(x)

# x = sns.FacetGrid(tips, hue='smoker', col='time')
# x =( x.map(plt.scatter, 'total_bill', 'tip').add_legend())
# plt.show(x)

# x = sns.FacetGrid(tips, col='day')
# x = x.map(sns.boxplot, 'time','total_bill')
# plt.show()

# # #USE OF SIZE AND ASPECT
# x = sns.FacetGrid(tips, col='day',size=6,aspect=.4)
# x = x.map(sns.boxplot, 'time','total_bill')
# plt.show()
# x = sns.FacetGrid(tips, col='day',size=6,aspect=.4,col_order=['Sat','Thur','Sun','Fri'])
# x = x.map(sns.boxplot, 'time','total_bill')
# plt.show()



