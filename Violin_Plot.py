import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

tips=sns.load_dataset('tips')

sns.violinplot(x=tips['tip'],color='skyblue')
plt.show()
print(tips)

#for total bill
sns.violinplot(x=tips['total_bill'])
plt.show()

# #for two variable violin plot
sns.violinplot(x='size' , y='total_bill',data=tips)
plt.show()

sns.violinplot(x='day', y = 'total_bill', data=tips)
plt.show()

sns.violinplot(x='day', y = 'total_bill',data=tips,hue='sex' ,palette='husl')
plt.show()

# sns.violinplot(x='day',y='total_bill',data=tips,hue='smoker',palette='winter_r')
# plt.show()

sns.violinplot(x='day',y='total_bill',hue='smoker',data=tips,split=True,palette='coolwarm')
plt.show()

sns.violinplot(x='day', y='total_bill', data=tips, palette='coolwarm', order=['Sat','Thur','Sun','Fri'])
plt.show()

sns.violinplot(x='day',y='total_bill',data=tips,hue='smoker',palette='husl',inner='stick',scale='count')
plt.show()

sns.violinplot(x='day',y='total_bill',data=tips,hue='smoker',palette='husl',inner='stick')
plt.show()

sns.violinplot(x='day',y='total_bill',data=tips,hue='sex',palette='husl',inner='stick',scale='count')
plt.show()

sns.violinplot(x='day',y='total_bill',data=tips,hue='sex',palette='husl',split=True,inner='stick',scale='count')
plt.show()


sns.violinplot(x='day',y='total_bill',data=tips,hue='smoker',palette='husl',inner='stick',scale='count',scale_hue=False,split=True)
plt.show()

sns.violinplot(x='day',y='total_bill',data=tips,hue='sex',palette='husl',inner='stick',scale='count',scale_hue=False,split=True)
plt.show()

sns.violinplot(x='day',y='total_bill',data=tips,hue='sex',palette='husl',inner='stick',scale='count',scale_hue=False,split=True,bw=0.1)
plt.show()
