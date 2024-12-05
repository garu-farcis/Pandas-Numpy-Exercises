import pandas as pd

df_empty = pd.DataFrame()
df_non_empty = pd.DataFrame({"A": [1, 2]})
print(df_non_empty)

#Use Case: Useful to verify if a DataFrame or Series is empty before performing operations.
print("Is df_empty empty?", df_empty.empty)  # True
print("Is df_non_empty empty?", df_non_empty.empty)  # False

# Use Case: Determine if at least one condition is satisfied in a column or dataset.

df = pd.DataFrame({
    "A": [False, False, True],
    "B": [0, 0, 0],
    "C": [False, True, False]
})
print(df)
print("Any True values per column?")
print(df.any())  # Checks column-wise

print("Any True values in the entire DataFrame?")
print(df.any().any())  # Combines results to check entire DataFrame

#Use Case: Determine if a condition holds for all elements in a column or dataset.
df1 = pd.DataFrame({
    "A": [True, True, True],
    "B": [1, 0, 1],
    "C": [True, True, False]
})

print("All True values per column?")
print(df1.all())  # Checks column-wise

print("All True values in the entire DataFrame?")
print(df1.all().all())  # Combines results to check entire DataFrame


# Use Case: Simplify boolean expressions when dealing with single-value Series or DataFrames.
# Important: Works only if the Series or DataFrame has exactly one element.
# iloc method

s = pd.Series([True])
print(bool(s.iloc[0]))  # Access the element explicitly
