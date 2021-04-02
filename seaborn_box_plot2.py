import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

tips= sns.load_dataset('tips')
print(tips)

sns.boxplot(x='day',y='total_bill',hue='time',data=tips,order=['Sun','Fri', 'Thur' , 'Sat'],palette='husl' )
plt.show()

sns.boxplot(x='sex',y='tip',data=tips,order=['Female','Male'])
plt.show()

iris=pd.read_csv('../datafile/IRIS.csv')
print(iris)

#box plot for iris dataset

sns.boxplot(data=iris,palette='husl',orient='horizontal')#horizontal or just h
plt.show()
sns.boxplot(data=iris,palette='husl',orient='verticaly')
plt.show()


#each of our data points in box plot(mathod is swarn plot)
sns.boxplot(x='day',y='total_bill',data=tips,palette='husl')
sns.swarmplot(x='day',y='total_bill',data=tips,color='black')
plt.show()









