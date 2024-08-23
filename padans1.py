import pandas as pd

# create series
data = pd.series([1,2,3,4])
data1=pd.series([1,2,3,4],index=(["a","b","c","d"]))

# for reading data from excel
df =pd.read_excel("data.xlsx")

#analyse the data 
df.head() #print only first five rows
df.tail() # print last 5 values
df['colume_name']
df.shape #shows no. of rows and column
df.info() # give information
df.describe() 
df['wifi'].nunique() # find no. of unique values in a column 
df["column_name"].sum() # give sum in column
df.index #provide index
df1 = pd.read_excel('data.xlsr',usecols=['blue','pc']) # for reading specific columne
freom numpy.randome import randn
sample = pd.DataFrame(randn(8,4),index = None,columns=['A','B','C','D'])
print(df.loc[3]) #locate rows in the data

# data cleaning
data_test = pd.read('data_test.xlsx')
pd.isnull(data_test) #use to see which column has null value.
pd.isnull(data_test).sum() # to see which column has how many null values
data_test.sort_values(by='colume_name') #to sort column
data_test.dropna() # we want to drop missing values
data_test.dropna(axis=1)
data_test.dropna(thresh=2)
