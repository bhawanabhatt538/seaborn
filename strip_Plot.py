import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot  as plt

tips=sns.load_dataset('tips')
print(tips)

sns.stripplot(x=tips['tip'],jitter=False )
plt.show()

sns.stripplot(x='total_bill',data=tips,jitter=False)
plt.show()

sns.stripplot(x='day',y='total_bill',data=tips)
plt.show()

sns.stripplot(x='day',y='total_bill',data=tips,jitter=False)
sns.stripplot(x='day',y='total_bill',data=tips,jitter=0.2)
plt.show()

sns.stripplot(x='total_bill',y='day',data=tips,jitter=False)
plt.show()
#draw some outline outside our  datapoints

sns.stripplot(x='total_bill',y='day',data=tips,jitter=False,linewidth=1.2)#we can any line for linewidth
plt.show()

sns.stripplot(x='day',y='total_bill',data=tips,hue='sex',jitter=False)
plt.show()

sns.stripplot(x='day',y='total_bill',data=tips,hue='sex')
plt.show()

sns.stripplot(x='day',y='total_bill',data=tips,hue='smoker',jitter=True,split=True,palette='winter_r')
plt.show()

sns.stripplot(x='day',y='total_bill',data=tips,hue='smoker',jitter=True,split=True,palette='winter_r',order=['Fri','Sun','Sat','Thur'])
plt.show()

sns.stripplot(x='sex',y='tip',data=tips,jitter=False,order=['Female','Male'],palette='husl')
plt.show()

sns.stripplot(x='sex',y='tip',data=tips,jitter=False,order=['Female','Male'],marker='D',palette='husl')
plt.show()

sns.stripplot(x='day',y='total_bill',data=tips,marker='D',size=9,hue='sex',edgecolor='grey')
plt.show()

sns.stripplot(x='day',y='total_bill',data=tips,marker='D',size=9,hue='sex',edgecolor='grey',palette='husl',alpha=0.50,jitter=True)
plt.show()

#draw strip plot on the top of box plot
sns.stripplot(x='tip',y='day',data=tips,jitter=True,palette='winter_r',color='0.5')
sns.boxplot(x='tip',y='day',data=tips)
plt.show()

#ddraw strip plot and violin plot on the same graph
sns.stripplot(x='tip',y='day',data=tips,jitter=True,color='0.6')
sns.violinplot(x='tip',y='day',data=tips,jitter=True)
plt.show()




























































