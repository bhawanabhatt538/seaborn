import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

iris = sns.load_dataset('iris')
print(iris)

# x=sns.PairGrid(iris)
# x=x.map(plt.scatter)
# plt.show()

# x=sns.PairGrid(iris)
# x=x.map_diag(plt.hist)
# x=x.map_offdiag(plt.scatter)
# plt.show()

# x=sns.PairGrid(iris, hue='species')
# x=x.map_diag(plt.hist)
# x=x.map_offdiag(plt.scatter)

# plt.show()

# #how to add legend
# x=sns.PairGrid(iris,hue='species')
# x=x.map_diag(plt.hist)
# x=x.map_offdiag(plt.scatter)
# x=x.add_legend()
# plt.show()

# #add palette

# x=sns.PairGrid(iris,hue='species',palette='coolwarm')
# x=x.map_diag(plt.hist)
# x=x.map_offdiag(plt.scatter)
# x=x.add_legend()

# plt.show()



# x=sns.PairGrid(iris,hue='species',palette='coolwarm')
# x=x.map_diag(plt.hist,histtype='step',linewidth=4)
# x=x.map_offdiag(plt.scatter)
# x=x.add_legend()
# plt.show()


x = sns.PairGrid(iris)
x = x.map(plt.scatter)
plt.show()

# ok so in pair grid we also draw the subsets of the variables

x = sns.PairGrid(iris, hue='species',vars= ['petal_length' ,'petal_width' ])
x=x.map_diag(plt.hist )
x=x.map_offdiag(plt.scatter)
x=x.add_legend()
plt.show()


#apply edgecolor
x = sns.PairGrid(iris, hue='species',vars= ['petal_length' ,'petal_width' ])
x=x.map_diag(plt.hist , edgecolor = 'black' )
x=x.map_offdiag(plt.scatter ,edgecolor='blue')
x=x.add_legend()
plt.show()

#we can change the varibles

x=sns.PairGrid(iris , x_vars= ['petal_length' ,'petal_width' ] , y_vars=['sepal_length' , 'sepal_width'])
x=x.map(plt.scatter)
plt.show()

# different graph above and below the diagonal

x = sns.PairGrid(iris ,hue= 'species' , hue_kws={'marker':['D','s','+']})
x = x.map_diag(plt.hist)
x = x.map_upper(plt.scatter)
x = x.map_lower(sns.kdeplot)
x = x.add_legend()
plt.show()


x = sns.PairGrid(iris ,hue= 'species' , hue_kws={'marker':['D','s','+']})
x = x.map(plt.scatter, s=30 ,edgecolor='black')#s=size
x = x.add_legend()
plt.show()

