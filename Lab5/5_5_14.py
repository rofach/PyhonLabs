import pandas as pd

df = pd.DataFrame({'A': range(10), 'B': range(10, 20)})
print(df)

print('Введіть K')
K = int(input())
print(df.head(K))

print('Введіть L')
L = int(input())
print(df.tail(L))
