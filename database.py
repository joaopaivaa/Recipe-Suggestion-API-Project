import pandas as pd

df = pd.read_csv('C:\\Users\\joaov\\Documents\\Recipe Suggestion API Project\\recipes_data.csv')

df = df.drop(['link','source','site'], axis=1)
df = df.dropna()
df = df.reset_index(drop=True)
df = df.iloc[0:80000,:]

df.to_csv('recipes_data_cleaned.csv', index=False)
