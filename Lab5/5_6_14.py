import pandas as pd
data = {
    'Нейронні мережі': [95, 88, 76, 92, 85],
    'СШІ': [80, 90, 85, 70, 95]
}
df = pd.DataFrame(data)
print(df.mean().to_string())