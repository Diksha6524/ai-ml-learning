import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


#in this we will be learing about eda and feature engg on black friday dataset
#cleaining and preparing the data for model training

#import dataset
df_train=pd.read_csv('blackfriday_train.csv')
print(df_train.head())
print(df_train.columns)


#problem statemnt->Problem Statement
# A retail company “ABC Private Limited” wants to understand the customer purchase behaviour (specifically, purchase amount) against various products of different categories. They have shared purchase summary of various customers for selected high volume products from last month. The data set also contains customer demographics (age, gender, marital status, city_type, stay_in_current_city), product details (product_id and product category) and Total purchase_amount from last month.
# Now, they want to build a model to predict the purchase amount of customer against various products which will help them to create personalized offer for customers against different products.




# we need to combine train and test dataset,so that we so preprocessing on both

#import test data
df_test=pd.read_csv('blackfriday_test.csv')
print(df_test.head())
print(df_test.columns)  #intest data we wot be able to see output variable ie ->Purchase


#merge both dataset
df=pd.concat([df_train,df_test])
print(df.head(15))
print(df.info())
#age in it is categorical vairable cuz its in range
print(df.describe())

#we can drop column user_id
df.drop(['User_ID'],axis=1,inplace=True) #axis =0 rowwise,axis=1 columnwise
print(df.columns)

#number of categorical variables are Gender,Age,Occupation,city_category
#we fix categorical variables
# Fixing categorical variables helps in:
# Correct value counts
# Clean bar charts
# Meaningful groupby analysis
# Reliable model input later


# Numerical variables → we check range, min, max, outliers
# Categorical variables → we check consistency, spelling, categories count




#gender->
#lets check m and f
#using dummies->numerical representation of categorical variables
print(pd.get_dummies(df['Gender'],dtype=int))  #it shows in true and false  without dtype=int it shows in bool
#now we will convet f /m into 0/1 s
#we use map method it will take conditions given and map it to the data accordingly
df['Gender']=df['Gender'].map({'F':0,'M':1})
print(df['Gender'].head())  
#this can be also done as
#df['Gender ']=df['Gender '].replace({'F':0,'M':1}) or df['Gender']=pd.get_dummies(df['Gender'],dtype=int,drop_first=1)
#why drop_first used-> to avoid dummy variable trap
#Drop one dummy category per feature to avoid multicollinearity
#example->if we have 3 categories A,B,C then if we create dummies for all 3 then if we know values of A and B we can easily find C
#so we drop one category to avoid this trap
#Pandas drops the first category in sorted order
# For ['Female', 'Male'] → Female is dropped
#drop_first=True removes one dummy variable per categorical feature to prevent multicollinearity.


#  age -> categorical variable to numerical
print(df['Age'].unique())  #it will give unique valuse in age column
df['Age']=df['Age'].map({'0-17':1,'18-25':2,'26-35':3,'36-45':4,'46-50':5,'51-55':6,'55+':7})
#here we gave rank,for target guiding encoding,that is ml will understand that 26-35 age group buys more than 18-25 age group
# Label Encoding means:(in the abve example we can use label encoding)
# Converting categorical (text) values into numbers by assigning a unique number to each category.
#it is mostly used when category ORDER matters

#example-
# from sklearn import preprocessing
# le=preprocessing.LabelEncoder() #creation of bject

# df['Age']=le.fit_transform(df['Age']) #fitting and transforming in one step
# print(df['Age'].unique())
#outpu['0-17' '55+' '26-35' '46-50' '51-55' '36-45' '18-25']
# [0 6 2 4 5 3 1]   
#for test we hv to do transfrm

#City_category
df_City=(pd.get_dummies(df['City_Category'],drop_first=True,dtype=int))
print(df_City.head())
#here we will concat it with aour og dataset
df=pd.concat([df,df_City],axis=1)  #it will concat the two dataset columnwise
print(df.head())
#now we can drop city category column
df.drop(['City_Category'], axis=1, inplace=True)#inplace=True means it will make changes in original dataset


# We didn’t map because mapping creates a fake order.
# We dropped the original column because one-hot columns already carry the city information correctly.


# print(df['City_Category'].unique())
#we can see that city category has 3 categories A,B,C
#we will use label encoding for this
# df['City_Category']=df['City_Category'].map({'A':1,'B':2,'C':3})
# print(df['City_Category'].head())







#missing values
print(df.isnull().sum())
#we can see that product category 2 and 3 have missing values even Purchase column has missing values in test dataset
#purchase should hv null values cuz Purchase is what we are trying to predict.


# Training data = questions with answers # u learn from it
# Test data = questions without answers #u have to predict the answers
# Train.csv → Purchase column filled
# Test.csv → Purchase column empty

#comapny doesnt kow future purchase amount so its missing in test data
#so we will only deal with missing values in product category 2 and 3

print(df['Purchase'].info())


