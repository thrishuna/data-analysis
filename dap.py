# -*- coding: utf-8 -*-
"""DAP.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zPB6cMmXMBz5CGk6HWf5cKHMsnKRLwbQ
"""

import numpy as np
#creating array
arr=np.array([1,2,3,4,5])
print(arr)
a=np.zeros((3,3),dtype=int)
print(a)
b=np.ones((2,2),dtype=int)
print(b)
c=np.arange(10)
print(c)
#array manipulation
d=arr.reshape(5,1)
print(d)
e=arr[2:4]
print(e)

import numpy as np
#mathematical operations
#addition of arrays
arr1=np.array([1,2,3,4])
arr2=np.array([5,6,7,8])
arr3=(arr1+arr2)
print(arr3)
#broad casting
a=arr+3
print(a)
#vstack
a=np.array([2,4,7,9])
b=np.array([1,5,3,8])
c=np.vstack(a+b)
print(c)
#stack
a=np.array([2,4,7,9])
b=np.array([1,5,3,8])
c=np.stack(a+b)
print(c)
#split
a=np.array([1,2,4,6,3,7,5,8])
split=np.split(a,4)
print(split)
#transpose
ar=np.array([1,2,3,4,5,6])
trans=ar.T
print(trans)

import numpy as np
#linear algebra
a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
c=np.dot(a,b)
print(c)
d=np.linalg.eig(c)
print(d)
#1
a=np.array([[1,2,3],[5,6,4]])
b=np.sum(a)
print(b)
#2
a=np.array([[1,2,3],[4,6,7]])
c=np.sum(a,axis=0)
d=np.sum(a,axis=1)
print(c)
print(d)
#3
a=np.array([1,2,3,4,5])
b=np.mean(a)
c=np.median(a)
d=np.var(a)
stand=np.std(a)
print(b)
print(c)
print(d)
print(stand)

import numpy as np
#creating data set,loading,saving the data set
data=np.loadtxt("/content/note.txt",dtype=int)
data=np.savetxt("/content/date.txt",data)
print(data)

import matplotlib.pyplot as plt
a=np.array([1,2,3,4])
plt.plot(a)

#importing pandas
import pandas as pd
a=["jwalitha","lahari","sunny","dhanush","durga","jahnavi","ramya"]
r=pd.Series(a,index=[67,43,44,89,34,45,23])
print(r)

df=pd.read_csv("/content/disasters data.csv")
print(df)
print(df.loc[1])
df.head(5)
df.tail(10)
df.shape
dfn=df.tail(10)
d=df.head(10)
dfn=pd.concat([d,dfn],axis=0)
e=df.to_csv("manual.csv")
print(dfn.groupby(['Year'])['Seq'].count())



df=pd.read_csv("/content/floods.txt", sep=" ")
print(df)

df=pd.read_excel("/content/excel.xlsx",sheet_name=1)
print(df)

from google.colab import drive
drive.mount('/content/drive')

import numpy as np
import matplotlib.pyplot as plt
runs=np.array([100,50,91,78,89,25,34,19,9,10])
w=np.array([1,0,2,0,3,7,8,9,7,5])
plt.scatter(runs,w,color='orange')
plt.title('IndvsAus_score')
plt.show()

import numpy as np
import matplotlib.pyplot as plt
#generate array of 200 elements
tigar=np.linspace(-2*np.pi,2*np.pi,50)
print(tigar)
plt.plot(tigar,np.sin(tigar),color='black')
plt.title("sin(x)")
plt.show()

import numpy as np
import matplotlib.pyplot as plt
#creating x
overs=np.arange(5,50,5)
overs_a=np.arange(5,30,5)
#creating y
runs_i=np.array([25,51,84,131,160,189,220,250,267])
runs_a=np.array([15,41,94,110,151])
wickets=np.array([12,32,96])
#plotting
plt.subplot(2,1,2)
plt.plot(overs,runs_i,color='blue',label='India')
plt.legend(loc='best')
plt.subplot(2,1,1)
plt.plot(overs_a,runs_a,color='yellow',label='Aus')
#combining two graphs
plt.legend(loc='best')
#displaying final graph
plt.show()

import matplotlib.pyplot as plt
a=[230,560,780,127,128]
b=[200,160,270,127,400]
years=[1,2,3,4]
profit_a=[(a[i]-a[i-1]) for i in range(1,len(a))]
profit_b=[(b[i]-b[i-1]) for i in range(1,len(b))]
plt.subplot(2,1,2)
plt.plot(years,profit_a,color='hotpink',linewidth='3',label='companyA',marker='.',ms='15',mec='k')
plt.subplot(2,1,1)
plt.plot(years,profit_b,color='black',linestyle='dotted',label='companyB',marker='H')

a=np.array([25,60,5,10])
labe=["AIML","Python","Pandas","Numpy"]
explo=[0.2,0,0,0]
colo=["red","blue","yellow","black"]
plt.pie(a,labels=labe,explode=explo,colors=colo,startangle=180)
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("/content/daily temperature - Sheet1.csv")
print(df)
average_temperature=df['temperature( celsius)'].mean()
highest_temperature=df['temperature( celsius)'].max()
lowest_temperature=df['temperature( celsius)'].min()
threshold=50
days_above_threshold=df[df['temperature( celsius)']>threshold].shape[0]
plt.plot(Date,temperature( celsius),color='hotpink',linewidth='3',label='companyA',marker='.',ms='15',mec='k')
print("average temperature of month:",average_temperature)
print("highest temperature of month:",highest_temperature)
print("lowest temperature of month:",lowest_temperature)
print("number of days where temperature exceeded",threshold,"degrees celsius:",days_above_threshold)
plt.show()

"""training data
testing data
types
1 superwised
2 unsuperwised
3 semisuperwised

"""

pip install seaborn

import seaborn as sns
import matplotlib.pyplot as plt
#load example dataset
tips=sns.load_dataset("dots")
print(tips)
#create a scatter plot
sns.scatterplot(x="coherence",y="firing_rate",data=tips)
plt.title("scatter plot of coherence vs.firing_date")
plt.xlabel("coherence($)")
plt.ylabel("firing_date($)")
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
iris=sns.load_dataset("iris")
print(iris)
correlation_matrix=iris.corr()
sns.heatmap(correlation_matrix,annot=True,cmap="coolwarm")
plt.title("correlation heatmap of iris dataset")
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
flights=sns.load_dataset("flights")
print(flights)
correlation_matrix=flights.corr()
sns.heatmap(correlation_matrix,annot=True,cmap="coolwarm")
plt.title("correlation heatmap of flights dataset")
plt.show()

"""training data-training the machine
testing data-tes
1 superwised
2 unsuperwised
3 semisuperwised
"""