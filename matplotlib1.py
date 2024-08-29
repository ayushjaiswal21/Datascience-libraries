import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
x=np.array([0,8])
y=np.array([0,100])
plt.plot(x,y)
plt.show()

#marker
ymark = np.array([2,3,8,1])
plt.plot(ymark,market='0')

#color and linestyle
plt.plot(x,y,'r--*') #for increasing size of marker we use 'ms=size'
plt.plot(x,y,'r--*',ms=5)
#mfc=marker face color 
#mec=marker edge color
year=(2015,2016,2017,2018,2019,2020)
inc=(20.4,39.8,21.9,44.9,68.3,79.3)
wo=(19.4,43.5,56.9,78.4,100.4,111.3)

#1 is a number to a figure and act like a attribute of figure
fig = plt.figure(1,figsize=(6,4))
chart = fig.add_subplot(121)
chart2=fig.add_subplot(122)
chart.plot(year,inc)
chart2.plot(year,wo)
plt.show()

fig_2,axes=plt.subplots(2,2,figsize=(20,5))
axes[0,1].scatter(year,wo)
axes[1,0].plot(year,inc)

#pie chart 
y = np.array([30,20,30,20])
lblcity=['delhi','pune','chennai','hyd']
plt.pir(y,labels=lblcity)
plt.legend(title='cities : ')

#bar charts
a=np.array(["p",'q','r','s'])
b=np.array([2,6,2,11])
plt.bar(a,b)

#for horizontal bar chart
plt.barh(a,b)

#histogram
x=np.random.normal(170,10,250)
plt.hist(x)
fig,ax=plt.subplots(1,1)
a=np.array([22,33,44,5,63,76,75,56,84,87,2,93])
ax.hist(a,bins=[0,25,50,75,100])
ax.set_title("histogram charts")
ax.set_xticks([0,25,50,75,100])
ax.set_xlabel('marks')
ax.set_ylabel('no. of student')
plt.show()
