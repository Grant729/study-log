import pandas as pd

df = pd.DataFrame({
    "学院": ["信息管理", "计算机", "信息管理", "历史", "计算机",
           "信息管理", "历史", "计算机", "信息管理", "历史"],
    "月份": [1, 1, 2, 1, 2, 2, 3, 3, 3, 2],
    "借阅量": [120, 200, 150, 80, 180, 160, 90, 220, 140, 100],
    "逾期数": [5, 30, 8, 2, 25, 6, 3, 35, 9, 1]
})

print(df.head(3))
print(df.shape)
print(df.dtypes)
print(round(df.describe(), 2))
print(df['借阅量'])
print(df[['学院', '逾期数']])
print(df[df['借阅量'] > 150])
print(df[df['学院'] == '信息管理'])
print(df[(df['学院'] == '信息管理') & (df['借阅量'] > 100)])
print(df.sort_values('借阅量', ascending=False))
print(df.sort_values('借阅量', ascending=True).head(3))
print(df.groupby('学院')['借阅量'].sum())
print(df.groupby('学院')['借阅量'].mean())
df['逾期率'] = df['逾期数'] / df['借阅量']
print(df.sort_values('逾期率', ascending=False))
