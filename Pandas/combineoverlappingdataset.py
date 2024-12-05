import pandas as pd
import numpy as np

# np.where(condition, value_if_true, value_if_false)
#
#     This is a NumPy function that works element-wise:
#         If condition is True, it takes the value from value_if_true.
#         Otherwise, it takes the value from value_if_false


def combiner(x, y):

    return np.where(pd.isna(x), y, x)

x= pd.Series([1,np.nan, 2])
y = pd.Series([2,3,4])

print(combiner(x,y))


