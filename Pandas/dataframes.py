# DataFrame Creation and Basic Operations
#
#     Create a pandas DataFrame with the following data:
#         Name: ["Alice", "Bob", "Charlie"]
#         Age: [25, 30, 35]
#         City: ["New York", "Paris", "London"]
#
#     Load a CSV file into a pandas DataFrame and display the first 5 rows.
#
# Create a DataFrame with random numbers (5 rows and 3 columns) and add a new column that contains the row-wise sum of all values.
#
#Filter rows from a DataFrame where the value in the Age column is greater than 30.
#
#     Sort a DataFrame by a specific column, both in ascending and descending order.

import pandas as pd
import numpy as np
from pandas.conftest import index

my_df = pd.DataFrame([["Alice", "Bob", "Charlie"],[25, 30, 35],["New York", "Paris", "London"]],index=['Name','Age','City'])
print(my_df)

my_csv= pd.read_csv('/Users/prse/Downloads/tips.csv')
print(my_csv.head())

new_df= pd.DataFrame(np.random.randint(1,100,size=(5,3)),columns=['0','1','2'] )
new_df['Total']= new_df.sum(axis=1) # axis =1 , if sum is done row wise and axis =0 if sum is done col wise
print(new_df)

# Convert index to numeric type (integer) to fix the comparison issue
# my_df.index = pd.to_numeric(my_df.index,errors='coerce')
# my_df.index.name='Age' # pointing to the index we want to evaluate
# filter_df =my_df.loc[my_df.index>30]
# print(filter_df)
df = pd.DataFrame(

    {

        "one": pd.Series(np.random.randn(3), index=["a", "b", "c"]),

        "two": pd.Series(np.random.randn(4), index=["a", "b", "c", "d"]),

        "three": pd.Series(np.random.randn(3), index=["b", "c", "d"]),

    }

)
print(df)

row = df.iloc[1]
print(row)
column = df["two"]
print(column)
df.sub(row, axis="columns")
print(df)
df.sub(row, axis=1)
print(df)
df.sub(column, axis="index")
print(df)
df.sub(column, axis=0)
print(df)

dfmi = df.copy()
dfmi.index = pd.MultiIndex.from_tuples(

    [(1, "a"), (1, "b"), (1, "c"), (2, "a")], names=["first", "second"]

)
print(dfmi)
print(dfmi.sub(column, axis=0, level="second"))
s = pd.Series(np.arange(10))
div, rem = divmod(s, 3)
print(div)
print(rem)
idx = pd.Index(np.arange(10))
print(idx)
div, rem = divmod(idx, 3)
print(div,rem)
#Missing data / operations with fill values
df2 = df.copy()
df2.loc["a","three"] = 1.0
print(df2)
print(df + df2)
print(df.add(df2,fill_value=0))
