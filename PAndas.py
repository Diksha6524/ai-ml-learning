import pandas as pd
##### for accessing data from csv file using pandas
dt=pd.read_csv("people_data.csv")
print(dt.columns)
print(dt.head())
# how many elements  present in dataframe
print(dt.info())
print(dt.describe())
print(dt.shape) 
 
# # what is the index of word micros
print(dt[dt['First Name']=='Lori'])
print(dt.loc[1])  # loc is used to access a row by its index label
# if we hv to find highestsalary or max value from any column
# print(dt['Salary'].max())  HERE WE DONT ANY COLUMN WITH VALUED LIKE THAT
print(dt.max()) # gives max value from all columns present
# print(dt.loc[dt['Age'].idxmax()]) # gives row with max age
print(dt.min()) # min value from all columns 


df=pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],columns=["a","b","c"]) #if we want to give index or row names then we can specify with the help of index parameter ie index=["x","y","z"]
print(df)
print(df.head())
print(df.head(1))
print(df.tail(2)) 
print(df.describe())
print(df.max())
print(df.min())
print(df.info())
print(df.nunique())
# for finding specific value
print(df[df['b']==5])
print(df.shape) #output of format(rows,columns)


#if i hv to load csv file from url
url="https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv"
D=pd.read_csv(url)
print(D.head())

#csv files takes up more memory so we can use other file formats like parquet or feather
results=pd.read_parquet("results.parquet")
print(results.head())
print(results.sample(5))  # Sample 5 rows from the results Data(gives random 5 rows)

#loc and iloc
#Loc= alows us to filter or access data by rows and columns
print(results.loc[0:2,["year","type"]]) #[[rows],[columns]]
#iloc= access data by index value
print(results.iloc[0:3,0:4]) #[[rows],[columns]]
#iloc-upper index isnt inclusive,loc its inclusive
print(results.type) #accessing column named type
print(results['type']) #accessing column named type
results.index=results['discipline'] #changing index to discipline column if we want want more columns ['discipline':'place']
print(results.head())





