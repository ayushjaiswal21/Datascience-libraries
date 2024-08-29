import pandas as pd 
import numpy as np 
import statistics 
import scipy.stats as stats
df=pd.read_csv('book.csv')
print(df.head())
print(df.info())
print(df.shape)
print(df.describe())
print(df['auther'=='jk'])
print(df['authe'.unique()])
print(df['auther_rating'].mean())
print(df['auther_rating'].median())
print(df['auther_rating'].mode())
print(statistics.stdev(df['price'])) #standard deviation
print(statistics.variance(df['average_rating'])) #varience
q3,q1=np.percentile(df['average_rating'],[75,25])
print(q3,q1)
iqr=q3-q1
print(stats.zscore(df['average_rating']))
print(df.corr(method='person')) #cofficient of corelation
a=df['sold'].mean()
df['sold'].fillna(a,inplace=True)