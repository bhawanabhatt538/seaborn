import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#loading tips dataset

tips = sns.load_dataset('tips')
#let's called two variable form our dataset through a bar plot for we called seaborn's barllet method

#sns.barplot(x="day",y="tip",data=tips)
#plt.show()

#let's plot bar plot day versus total bill
#sns.barplot(x='day',y='total_bill',data=tips)
#plt.show()
#this time pass hue attribute for sex
#sns.barplot(x='day',y='tip',data=tips,hue='sex')
#plt.show()

#for change color of bars add_legend
#sns.barplot(x='day',y='tip',data=tips,hue='sex',palette='winter_r')
plt.show()

#now we want to pass plot for smoker

#sns.barplot(x='day',y='total_bill',data='tips',hue='smoker')
plt.show()


#if we want to see days in differnt order
#sns.barplot(x='day',y='tip',data=tips,hue='sex',order=['Sat','Fri','Sun','Thur'])
plt.show()


#to pass meuian
from numpy import median

sns.barplot(x='smoker',y='tip',data=tips,estimator= median)
plt.show()
