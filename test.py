import pandas as pd
df=pd.read_excel('DATA_SEARCH_SAMPLE.xls')
print(df.head())
print(df.columns)
print(f"The shape of the dataframe: {df.shape}")