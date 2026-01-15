import pandas as pd

bios=pd.read_csv('bios (1).csv')
print(bios.head())


# #what we actually want to see in this dataset
# #ie what should we clean up?
# # |
# # --->
# #get rid of bullet points used in names column
# #removing unnecessary columns
# #split height/weight
# #parse out dates from born and died column
# #parse out city,region and country from 'born' column

df=bios.copy()
print(df.info())

#removing bullet points
print(df[df['Used name'].str.contains('•')])

#lets chnage this bullet point to space
df['name_contains_bulletpoints']=df['Used name'].str.replace('•',' ')
print(df.head())


#spliting height and weight 
df[['height','weight']]=df['Measurements'].str.split('/',expand=True)#we used expand=true cux we want two columns
print(df[['height','weight']])
print(df)