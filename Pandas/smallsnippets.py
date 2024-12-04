import numpy as np
import  pandas as pd
from pandas.conftest import index

# data = [np.random.randn(10)]
# print(data)
#by default numpy produces array -2 d series , where index must be same length as data
data1= pd.Series(np.random.randn(5))
# print(data1)
data = np.zeros((2,), dtype=[("A", "i4"), ("B", "f4"), ("C", "S10")])
data[:] = [(1, 2.0, "Hello"), (2, 3.0, "World")]
print(data)
x= pd.DataFrame(data)
print(x)
print(pd.DataFrame(data, columns=["C", "A", "B"]))

my_arr= np.arange(1000000)
my_list= list(my_arr)
print(my_arr)
print(my_list[100089])