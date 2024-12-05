import pandas as pd
import numpy as np

s1= pd.Series(np.arange(10))
s2 = pd.Series(np.arange(20))
s3 =pd.Index(np.arange(10))
ar1= pd.array(np.arange(20))
print(s1==s3)
print(s1==s3)
print(s2==ar1)