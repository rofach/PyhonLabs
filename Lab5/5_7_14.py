import pandas as pd
products = pd.DataFrame({
    'Product': ['product1', 'product2', 'product3'],
    'Price': [800, 1500, 400]
})
df_sorted = products.sort_values(by='Price')
print(df_sorted)