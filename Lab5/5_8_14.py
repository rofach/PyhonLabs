import pandas as pd
index_tuples = [
    ('Червень', 'Озеро Світязь'),
    ('Червень', 'Річка Дніпро'),
    ('Липень', 'Озеро Світязь'),
    ('Липень', 'Ставок біля лісу'),
    ('Серпень', 'Річка Дніпро'),
    ('Серпень', 'Ставок біля лісу')
]
multi_index = pd.MultiIndex.from_tuples(index_tuples, names=['Місяць', 'Водойма'])
data = [12, 5, 18, 2, 25, 8]
df = pd.DataFrame({'Кількість риби': data}, index=multi_index)

print('Введіть K')
K = int(input())
print(df.head(K))

print('Введіть місяць')
month_input = input()
print(df.loc[month_input])