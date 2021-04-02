import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


tips = sns.load_dataset('tips')
print(tips)

# sns.regplot(x='total_bill' , y='tip' , data=tips)
# plt.show()

# sns.regplot(x='total_bill' , y='tip' , data=tips , color='green')
# plt.show()

mean = [2,5]
cov = [[1.1, 0.4],[2.2, 3]]

x_value, y_value = np.random.multivariate_normal(mean, cov, 100).T

# sns.regplot(x=x_value, y=y_value)
# plt.show()


# sns.regplot(x=x_value, y=y_value, color = 'red')
# plt.show()



# seriesx_values = pd.Series(x_value , name='Var-X')
# seriesy_values = pd.Series(y_value , name='Var-Y')
# print(seriesy_values)
# sns.regplot(x=seriesx_values, y=seriesy_values)
# plt.show()

# seriesx_values = pd.Series(x_value , name='Var-X')
# seriesy_values = pd.Series(y_value , name='Var-Y')

# sns.regplot(x=seriesx_values, y=seriesy_values, marker='d', color=gray)
# plt.show()

# sns.regplot(x='total_bill', y='tip', data=tips, marker='+',\
#             scatter_kws={'color':'blue','marker'='D'},\
#             line_kws={'color':'black','linewidth':2.5})
# plt.show()


# sns.regplot(x='total_bill', y='tip', data=tips, marker='+',\
#             scatter_kws={'color':'grey'},\
#             line_kws={'color':'black','linewidth':2.5})
# plt.show()


sns.regplot(x=x_value, y=y_value, color = 'red', ci=40)
plt.show()

sns.regplot(x='size',y='total_bill',data=tips)
plt.show()

#to find more information about size feature
sns.regplot(x='size',y='total_bill',data=tips,x_jitter=0.08)
plt.show()


sns.regplot(x='size',y='total_bill',data=tips,x_jitter=0.08,scatter_kws={'color':'red'})
plt.show()

sns.regplot(x='size',y='total_bill',data=tips,x_estimator=np.mean)
plt.show()
