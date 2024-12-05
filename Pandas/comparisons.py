import pandas as pd

# Create two Series
s1 = pd.Series([1, 2, 3, 4])
s2 = pd.Series([4, 3, 2, 1])

# Element-wise comparison
print("Equal:", s1.eq(s2))  # Equal
print("Not Equal:", s1.ne(s2))  # Not Equal
print("Greater Than:", s1.gt(s2))  # Greater Than
print("Less than 4:")
df = pd.DataFrame({
    "A": [1, 2, 3],
    "B": [4, 5, 6]
})

print(df.lt(4))