#Pandas-- It is used to data manipulation: 1. Data Cleaning  2. Data Analysis
#Data structure-- 1. Series - One dimensional   2. Data Frame - Two Dimensional  3. Panel - Three Dimensional
#Pandas library

import pandas as pd
'''my_series = pd.Series(["Apple", "Banana" , "Mango" , "Watermelon"], name = "Fruit")
print(my_series)'''

'''list_of_list = [["Amar", 15], ["Akbar",14], ["Anthony",13]]
df = pd.DataFrame(list_of_list, columns = ["Name", "Age"])
print(df)'''

df = pd.read_csv("imdb_data.csv")
'''print(df)

#find the number of rows and columns
print(df.shape)

#fetch the data from top 
(print(df.head(2))) #by default it fetch 5 rows

#fetch the data from bottom
print(df.tail(2))

#fetch data randomnly
print(df.sample(10))
'''
#find the information of the data
#print(df.info())

#How does the data look like mathematically
#print(df.describe())

#find the number of columns
#print(df.columns)

#find the duplicate values
#print(df.duplicated().sum())                   #duplicate values means no similar rows

#find the null values
#print(df.isnull().sum())

#Indexing and Slicing
#print(df["title"])
#print(df[0:4])
#print(df.iloc[0:4,0:3])

#print multiple columns
#print(df[["title","budget","revenue","original_language"]])

#print(df.loc[0:4,["title","budget","revenue","original_language"]])

#in iloc ending index is not included but in loc ending index is included

#unique values in a column
#print(df["original_language"].unique())
#print(df[df["original_language"]=="en"])

#if you want to write the data in a csv file
hindi_movies = df[df["original_language"]=="hi"]
print(hindi_movies.to_csv("hindi_movies.csv"))


