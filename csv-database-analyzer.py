import pandas as pd

csv = input("Insert csv link")
df=pd.read_csv(csv)
print(df.head(10))
print(df.shape)
print(df.describe())
print(df.isnull().sum())
total_no=df['target'].nunique()
print(total_no)
count=df['target'].value_counts()
print(count)
