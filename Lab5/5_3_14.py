import pandas as pd
prices = pd.Series([100, 200, 300, 400, 500], index=['product1', 'product2', 'product3', 'product4', 'product5'])

print('product2:')
print(prices['product2'])
print(prices.iloc[1])

print('product4:')
print(prices['product4'])
print(prices.iloc[3])