import pandas as pd
import numpy as np

arr = np.ones((20, 5))
df_dummy = pd.DataFrame(arr, columns=list('12345'))
df_dummy.to_csv('education.csv', index=False)

df = pd.read_csv('education.csv')
print(df.shape)