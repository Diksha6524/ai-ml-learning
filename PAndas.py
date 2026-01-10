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
coffee=pd.read_csv("coffee.csv")
print(coffee.head())
#to make changes in og data of coffee
coffee.loc[1,"Units Sold"]=10 #we can also use slice for the same ie for rows
print(coffee.head())
#at and iat
print(coffee.at[1,"Day"])#accessing single value
print(coffee.iat[4,1])#accessing single value by index
#iloc and loc are used for multiple values,iat and at are used for single value
print(coffee.Day)#or print(coffee['Day']),but u cant do coffee.Units Sold bcoz of space in the word
print(coffee.Day.unique()) #gives unique values in day column
print(coffee.nunique()) #gives number of unique values in each column
print(coffee.sort_values("Units Sold")) #sorts data in ascending order
print(coffee.sort_values("Units Sold",ascending=False)) #sorts data in descending order
print(coffee.sort_values(["Units Sold","Coffee Type"],ascending=[0,1])) #sorts by Units sold in descending(decreasing order) and coffee type in ascending(by aplhabetical order)
#for - itrating  through rows, loose performance
for index,row in coffee.iterrows():
    print(index)
    print(row)# also add single row ie row['column name']
    print("\n")
    #or u can write like this
# for index,row in coffee.iterrows():
#    print(f"Index: {index}, Day: {row['Day']}, Coffee Type: {row['Coffee Type']}, Units Sold: {row['Units Sold']}")
###filtering data
bios=pd.read_csv("bios.csv")
print(bios.head())
print(bios.tail())
#condition
print(bios['height_cm']>180) #gives true or false for each row
print(bios.loc[bios['height_cm']>180]) #gives rows where height>180
#or
print(bios[bios['height_cm']>180])#gives rows with height>180 
#for getting specific colums with the same 
print(bios[bios['height_cm']>180][["name","height_cm"]])#no in between ,( ie in between condn and columns)
#for getting specific columns only 
tA=bios.loc[bios['height_cm']>180,["name","height_cm"]]
print(tA)
#multiple conditions
Mul_Cond=bios[(bios['height_cm']>180)&( bios['weight_kg']>80)]
cond=Mul_Cond[['name','height_cm','weight_kg']]
print(cond)
#string operations
Diksha=bios[bios['name'].str.contains("Diksha")]#case senisitive
#If it shoulnd be case sensitive then
diksha=bios[bios['name'].str.contains("diksha",case=False)]
print(Diksha)
print(diksha)
#we can add conitions too
D_iksha=bios[bios['name'].str.contains('diksha|sara',case=False)]
print(D_iksha)
#startswith
start=bios[bios['name'].str.startswith('D')]
print(start)
#endswith
end=bios[bios['name'].str.endswith('a')]
print(end)
#string length
length=bios[bios['name'].str.len()>5]
print(length)
#missing values
miss=bios[bios['height_cm'].isnull()]
print(miss)
#athletexs born in cities that starts wuth a vowel
vowel_C=bios[bios['born_city'].str.contains(r'^[AEIOUaeiou]',na=False)]
#r-> raw string ,aviods escape char
#^ ->startswith  ie example if apple then a is the beggining of the word therfore its true or it will show the name cuz it starts with a vowel
#but for banana it will be false as letter b is at the beggining of the word 
# [AEIOUaeiou] -> any od these letters should be prsent at the beggining
#na=False -> to avoid NaN values
#or u can write it like this
vowel_c=bios[bios['born_city'].str.contains(r'^[aeiou]',case=False,na=False)]
#pandas cant filter rows with NaN values directly so we hv to use na parameterie if borncity has nan value then it will be considered as false
#case=False -> to avoid case sensitivity

print(vowel_C)
print(vowel_c)
#find athletes with names containing exactly two vowels
two_vowels=bios[bios['name'].str.contains(r'^[^AEIOUaeiou]*[AEIOUaeiou][^AEIOUaeiou]*[AEIOUaeiou][^AEIOUaeiou]*$',na=False)]
# ^ -> at the start is for start of the word
# $ -> at the end is for end of the word
# ^ inside []-> negation ie any letter except these
# *-> zero or more occurences of the preceding element
# [AEIOUaeiou]-> any one of these vowels
# [^AEIOUaeiou]*-> any number of non vowels

# exapmle
# R-nonvowel
# o-first vowel
# h-nonvowel
# i-second vowel
# t-nonvowel
# ^ → start

# $ → end

# [^vowels]* → any non-vowels

# [vowels] → one vowel


#athletes with nmes ending with son or sen
end_n=bios[bios['name'].str.contains(r'son$|sen$',na=False,case=False)]
print(end_n)

#find athlestes  with born year starting with 19
year_19=bios[bios['born_date'].str.contains(r'^19',na=False,)]
year_19_2=year_19[['name','born_date']]
print(year_19_2)
#find athletes born in cities containing double letters
double_l=bios[bios['born_city'].str.contains(r'(.)\1',na=False)]
# (.) -> any character
# \1 -> backreference to the first captured group
double_l_2=double_l[['name','born_city']]
#name containg 3 or more vowels
three_v=bios[bios['name'].str.contains(r'([AEIOUaeiou].*){3,}',na=False)]
#* -> zero or more occurences of the preceding element

#regular expressions
# Symbol	Meaning	Example
# ^	start of string	^A
# $	end of string	n$
# .	any one character	c.t
# *	0 or more	ab*
# +	1 or more	ab+
# []	choose one	[abc]
# [^ ]	NOT these	[^aeiou]

_is_in=bios[bios['born_country'].isin(['USA','FRA'])]
print(_is_in)
_is_in_=bios[bios['born_country'].isin(['USA','FRA']) &(bios['name'].str.startswith('A',na=False))]
print(_is_in_)
#instead of using bios again and again we can use query function
bios_query=bios.query('born_country=="USA" & name.str.startswith("Al")')
print(bios_query)
#####ADDING AND REMOVING COLUMNS FROM DATAFRAME
print(coffee.head())
#adding new column "pricez"
coffee['Price']=5.0
print(coffee.head())
#to be specific  we can use numpy function ie where
import numpy as np
coffee['new_Price']=np.where(coffee['Coffee Type']=='Espresso',4.0,5.0)
print(coffee.head())
#using loc 
coffee.loc[coffee['Coffee Type']=='Latte','new_Price']=4.5
print(coffee.head())
#i tried using query method for the same  just to realise im SToPiD, cuz query fun only fo filtering  not for assigning vals
#np.where() / .loc -> assigning vals


# #map is also used
# price_map = {
#     'Espresso': 4.0,
#     'Latte': 5.0
# }
# coffee['new_Price'] = coffee['Coffee Type'].map(price_map)

#removing index
print(coffee.drop(0)) #it doesnt alter the og data
#removing column
print(coffee.drop('new_Price',axis=1)) #axis=1 for column,axis=0 for row
#0r
print(coffee.drop(columns=['new_Price','Units Sold']))
#to make changes in og data
coffee.drop(columns=['new_Price','Day','Price'],inplace=True)
print(coffee.head())

#if i want new dataframe without modifying og data
new_coffee=coffee
new_coffee['Discounted Price']=4.0
print(new_coffee.head())
print(coffee.head())# same output as new coffee bcoz both r pointing to same data in memory
#to avoid this we use copy function
new_coffee_copy=coffee.copy()









 










