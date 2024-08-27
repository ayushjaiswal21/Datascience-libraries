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
#replace null values
data_test = pd.read_excel("data_test.xlsx")
data_test.Fillna(s,inplace=True) # to fill null values
data_test["column_name"].Fillna(10,inplace=True) #tp filling specific file
data_test["column_name"].mean() # print mean 

# deal with duplicate values in data
data_test.duplicated() #for priting duplicate values 
data_test.drop_duplicated() #for removing duplicated values
data_test.corr() #check the corealtionship (always get in zero and one )

#for concatenate 2 files
data_con = pd.read_excel(data_con.xlsx)
pd.concat([data_test,data_con])

#for concatinating column wise we have to give axis =1
concat_df =pd.concat([data_test,data_con],axis=1)
concat_df.to_excel('data_write.xlsx',sheet_name='sheet1') #for exporting concatinated file into working directory.

#indexing
df2=pd.DataFrame({'sports':['cricket','football','valleyball'],
                  'city':['delhi','mumbai','pune'],
                  'amazon':['books','clothes','battery','charger']},
                index=[0,1,2])
df2.loc[2]
df2[['city','sports']]

#iloc - get the combination of row and columns
df2.iloc[::]
#if df2.iloc[0:,0:3] then we get 0 row and column 0 to 2

#merging
left = pd.DataFram({'a':['hello','sir'],'b':[1,2]})
right = pd.DataFram({'a':['hello','mam'],'c':[3,4]})

#for merging
left.mearge(right,how='left',on='a')
