import pandas as pd

# K = 5
print('Введіть K')
K = int(input())
print('Введіть мови програмування')
languages_input = input()
languages = [lang.strip() for lang in languages_input.split(',')]
series = pd.Series(languages, index=range(1, K + 1))
print(series.to_string())