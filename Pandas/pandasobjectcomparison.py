import pandas as pd
import numpy as np

#To compare if objects in pandas (like DataFrame or Series) are equivalent
df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
print(df)
print(df+df)
print(df + df == df * 2)
print('is df s equal?',(df + df == df * 2).all().all())

s = pd.Series(np.arange(100))
s1= s+s
s2= s*2
print('is series equal?',(s1==s2).all())

# DataFrame.equals() is specifically designed to check if two objects are exactly equal in every aspect,
# including element-wise values and metadata (like index and column labels).

df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})

print(df1.equals(df2))  # True
