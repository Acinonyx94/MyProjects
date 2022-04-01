import csv, numpy as np, pandas as pd, random

df = pd.read_csv("PeoplesFavourites-1.csv")

#Drops any duplicate rows
df = df.drop_duplicates()

#Replaces NA symbols with np's NaN value
df = df.replace([0, "0", "none", " ", ""], np.nan)

#Drops any rows with NaN values in First Name, Last Name or Email columns
df = df.dropna(how="any", subset=["First Name", "Last Name", "Email"])

#Drops First Name and Last Name columns to add anonymity
df = df.drop(["First Name", "Last Name"], axis=1)

#Creates set of unique random 4-digit numbers with length of the df rows
id_gen = random.sample(range(1001, 9999), len(df.index))

#Inserts these random values into "ID" column as the first of the df.
df.insert(0, "ID", id_gen)

print(df)

#Writes the dataframe to a new CSV
df.to_csv("PeoplesFavouritesCleaned.csv")