import pandas as pd, numpy as np, csv
pd.set_option("mode.chained_assignment", None)

#Read in CSV file and build pd DataFrame
df = pd.read_csv("SalesData.csv")
#Sets the store names as the df index
stores = df["Unnamed: 0"]
df.index = stores
#Removes store names from df values
df.index.name=None
df.drop("Unnamed: 0", axis=1, inplace=True)

print("Sales for P2 and B8 in Nov, Feb and Mar:")
#Extract data into a seperate DataFrame using the loc indexing operation
sales1 = df.loc[["P2", "B8"], ["Nov-18", "Feb-19", "Mar-19"]]
print(sales1)

print("\nThird quarter sales for London stores, with monthly percentage increase:")
#This time using the iloc function for slice indexing by integer
sales_london = df.iloc[:2, 6:9]
#Calculate percentage change between columns, storing results in seperate DataFrame "pct"
pct = sales_london.pct_change(axis="columns", periods=1)
pct = pct * 100
#Insert percentage change figures as columns
sales_london.insert(2, "Nov Change", pct["Nov-18"])
sales_london.insert(4, "Dec Change", pct["Dec-18"])
print(sales_london)

print("\nTop 3 months for New York and corresponding stores:")
sales = df.copy()
#First extract all data for New York stores into new DataFrame
sales_ny = sales.iloc[3:5, :]
#Extract the max value in NY dataframe and then remove it
first = sales_ny.stack().index[np.argmax(sales_ny.values)]
sales_ny.replace(sales_ny.max().max(), 0, inplace=True)
#Extract the new max value in NY dataframe (second highest) and then remove it
second = sales_ny.stack().index[np.argmax(sales_ny.values)]
sales_ny.replace(sales_ny.max().max(), 0, inplace=True)
#Extract the new max value in NY dataframe (third highest) and then remove it
third = sales_ny.stack().index[np.argmax(sales_ny.values)]
sales_ny.replace(sales_ny.max().max(), 0, inplace=True)
print(f"Top monthly sales was {first[1]} at the {first[0]} store.")
print(f"Second highest monthly sales was {second[1]} at the {second[0]} store.")
print(f"Third highest monthly sales was {third[1]} at the {third[0]} store.")

print("\nThe overall lowest sales figure:")
print(df)
lowest = df.stack().index[np.argmin(df.values)]
print(f"The lowest figure came in {lowest[1]} at the {lowest[0]} store.")