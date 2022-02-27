import pandas as pd
df = pd.read_csv("2022-02-23_시가총액.csv",index_col=0)

# df = df.fillna("")

df['PER'] = df['PER'].apply(pd.to_numeric,errors='coerce')
print(df.info())
k1 = df['PER']<5
print(df[k1])