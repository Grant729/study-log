# %%
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

# %%
df = pd.read_csv('D:/AI project/demo/study-log/data/borrow_records.csv')
print(df)
print(df.shape)
print(df.dtypes)
print(df.isna().sum())

# %%
df['借阅量'] = pd.to_numeric(df['借阅量'], errors='coerce')
df['月份'] = df['月份'].astype(str).str.replace('月', '', regex=False).astype(int)
df['学院'] = df['学院'].str.strip().replace('信管', '信息管理')
df['逾期数'] = df['逾期数'].fillna(0)
df = df.dropna(subset=['借阅量'])
df = df.drop_duplicates()
df = df[df['借阅量'] >= 0]
print(df)
print(df.shape)
print(df.dtypes)
print(df.isna().sum())

# %%
df.to_csv('D:/AI project/demo/study-log/data/borrow_records_clean.csv', index=False)
print('已清洗！')

# %%
df.groupby("学院")["借阅量"].sum().sort_values(ascending=False).plot(kind="bar")
matplotlib.use("TkAgg")
plt.show()

# %%
