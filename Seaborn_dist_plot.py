import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#loading a tips data set
tips=sns.load_dataset('tips')
print(tips)
#using numpy to generatinng a list of random number
Num=np.random.random(150) #150 list of normaly distributed random Number
print(Num)

#seaborn has method display then we will pass the randomly generated number ,displot by default have histogramand kernel density estimate.
#we will pass the color attribue to change the color of graph
sns.displot(Num,color='red')
#plt.show()

#we can label our x axis
label_dist = pd.Series(Num,name='variable x')
#pass label_dist object
sns.distplot(label_dist)
plt.show()

#we can also ake our plots appers an the y axis by passing the vertical attribute

sns.distplot(label_dist,vertical=True)
plt.show()

#if we want to change the default color of blue we can pass the color attribute and set it to let's say red
sns.distplot(label_dist,vertical=True,color='red')
plt.show()

#if we don't want to see histogram we can pass another attribute known as hist and set it to be equal to false
sns.distplot(label_dist, hist=False)
plt.show()
#again instead of histogram we ccan pas rug attribute now we will see rug plot for each of oyr data set for each of oyr data point

sns.distplot(label_dist,rug= True,hist=False,color='green')
plt.show()


