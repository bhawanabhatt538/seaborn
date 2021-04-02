import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tips=sns.load_dataset('tips')
print(tips)

print(tips.head())

#let's looking at a single horizontal box plot for let's  say size
sns.boxplot(x=tips['size'])
plt.show()

sns.boxplot(x=tips['total_bill'])
plt.show()

#box plot for two variables
sns.boxplot(x='sex',y='total_bill',data=tips)
plt.show()

#box plot for day versus total bill
sns.boxplot(x='day',y='total_bill',data=tips)
plt.show()

#we can also combine these two box by passing hue
sns.boxplot(x='day',y='total_bill',data=tips,hue='sex')
plt.show()

#now we have data for each day ,for each day we have male and female and can change the color of this by passing palette attribute
sns.boxplot(x='day',y='total_bill',data=tips,hue='sex',palette='husl')
plt.show()

sns.boxplot(x='day',y='total_bill',data=tips,hue='time')
plt.show()


#use attribute order and pass the day in such an order that we want
sns.boxplot(x='day',y='total_bill',data=tips,order=['Sun','Fri','Thur','Sat'])
plt.show()


#use palette  attribute to  change the color
sns.boxplot(x='day',y='total_bill',data=tips,order=['Sun','Fri','Thur','Sat'],palette='husl')
plt.show()



iris=pd.read_csv("../datafile/IRIS.csv")
print(iris)

sns.boxplot(data=iris,palette='coolwarm')
plt.show()

sns.boxplot(x='day',y='total_bill',palette='husl')
sns.swarmplot(x='day',y='total_bill',data=tips)
plt.show()











