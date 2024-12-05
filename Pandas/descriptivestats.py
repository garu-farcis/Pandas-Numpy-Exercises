import pandas as pd
import numpy as np

df=pd.DataFrame({'A': np.random.randn(10),'B':np.random.randn(10)})
print(df)
print('\n',df.mean(1)) # row wise
# skipna: bool, default True
#
#     If True, it will ignore NaN values when calculating the mean.
#     This is useful when the data contains missing values.
#     If False, it will include NaN values in the calculation.
#     If there is any NaN in the data, the result will also be NaN.
# numeric_only: bool, default False
#
#     If True, it excludes non-numeric columns from the computation
#     (useful when the DataFrame has columns with non-numeric data types).
#     If False, it includes all columns that can be considered numeric.
print('\n',df.mean(0,skipna=False)) # col wise , skip na
df_with_na = pd.DataFrame({
    'A': [1, 2, 3, 4, None],
    'B': [5, None, 3, 2, 1]
})
print(df_with_na)
# By default, skipna=True, so NaNs are ignored.
print(df_with_na.mean())

df_mixed = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': ['a', 'b', 'c', 'd'],
    'C': [5, 6, 7, 8]
})
print(df_mixed)
print(df_mixed.mean(numeric_only=True))

# Combined with the broadcasting / arithmetic behavior,
# one can describe various statistical procedures,
# like standardization (rendering data zero mean and standard deviation of 1), very concisely:

ts_stand = (df - df.mean()) / df.std()
print(ts_stand)