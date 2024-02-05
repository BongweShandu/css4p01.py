# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 21:40:30 2024

@author: bongw
"""

import pandas as pd
df = pd.read_csv("movie_dataset.csv")
print(df)

#indexing a column
df = pd.read_csv("movie_dataset.csv", index_col = 0)
print(df)

# replacing empty values with mean() using the fillna function
x = df["Revenue (Millions)"].mean()
df["Revenue (Millions)"].fillna(x, inplace = True)

x = df["Metascore"].mean()
df["Metascore"].fillna(x, inplace = True)
print(df)

# Question 1
# sort the "Rating"column in descending order
pd = df.sort_values(by=['Rating'], ascending=False)
print(pd)
"""The Dark Knight"""

#Question 2
#  calculating average revenue for all the movies
pd = df["Revenue (Millions)"].mean()
print(pd)
"""82.95637614678898 million"""

# Question 3
# filter out revenue data for 2015 and 2017
Revenue_2015_2017 = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]

# Calculate the average revenue
pd = Revenue_2015_2017['Revenue (Millions)'].mean()
print(pd)
"""68.06 million"""

# Question 4
# count how many times 2016 appears on the year column
pd = df['Year'].value_counts()[2016]
print(pd)
"""297"""

# Question 5
# count how many times Nolan appears on the director column
pd = df['Director'].value_counts()['Christopher Nolan']
print(pd)
"""5"""

# Question 6
# filtering data
print(df[df['Rating'] >= 8.0])
"""78 (from number of rows)"""

# Question 7
# filter movies directed by nolan
films_by_nolan = df[df['Director'] == 'Christopher Nolan']

# Calculate the median rating
pd = films_by_nolan['Rating'].median()
print(pd)
"""8.6"""

# Question 8
# calculate the average rating for each year
pd = df.groupby('Year')['Rating'].mean()

# filter and find the year with the highest average rating
highest_year = pd.idxmax()
print(highest_year)
"""2007"""

# Question 9
# count films released between 2006 and 2016

year_counts = df['Year'].value_counts()
count_2006 = year_counts.get(2006, 0)
print(count_2006)

count_2016 = year_counts.get(2016, 0)
print(count_2016)

# (new-old)/old*100
pd = (count_2016 - count_2006) / count_2006 *100
print(pd)
"""575"""

# Question 10
pd = df[['Actors']].copy()
print(df)

pd['Actors'] = pd['Actors'].str.split(',')

# convert list into multiple rows
pd = pd.explode('Actors')
print(pd)

# lets get count by actor
pd['count'] = 1 
print(pd)

grouped = pd.groupby('Actors')

Actors_feat_count = grouped['count'].count()
print(Actors_feat_count.info())


# Question 11
Genres = df[['Genre']].copy()
print(Genres)

# Split text into a list
# Then sum of unique genres...
Genres['Genre'] = Genres['Genre'].str.split(',')

# Convert list into multiple rows
Genres = Genres.explode('Genre')
print(Genres)

Genres_unique = Genres.drop_duplicates()
print(len(Genres_unique))
"""20"""

# Question 12
# assuming 'df' is your DataFrame and you want to analyze numerical columns.TPM
numerical_features = df.select_dtypes(include=['float64', 'int64'])

# calculate the correlation matrix.T
correlation_matrix = numerical_features.corr()

# print the correlation matrix.
print("Correlation Matrix:")
print(correlation_matrix)





