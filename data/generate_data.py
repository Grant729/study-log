# -*- coding: utf-8 -*-
"""生成 D5 练习数据集：带脏数据的借阅记录 CSV（固定随机种子，可重复生成）"""
import random
import numpy as np
import pandas as pd

random.seed(42)
np.random.seed(42)

colleges = ["信息管理", "计算机", "历史", "文学", "法学"]
rows = []
for i in range(150):
    rows.append({
        "读者编号": f"R{1000 + i}",
        "学院": random.choice(colleges),
        "月份": random.randint(1, 3),
        "借阅量": random.randint(1, 200),
        "逾期数": random.randint(0, 40),
    })
df = pd.DataFrame(rows)

# —— 注入真实感"脏数据"，是明天清洗课的素材 ——
df.loc[10:20, "逾期数"] = np.nan      # 10 个缺失值
df.loc[25, "借阅量"] = "约120"         # 文本混入数值列
df.loc[26, "借阅量"] = -5              # 不可能为负
df.loc[27, "月份"] = "3月"             # 文本月份
df.loc[28, "学院"] = "信息管理 "       # 尾部空格 → 分组时会算成另一类
df.loc[29, "学院"] = "信管"            # 不规范写法
df.loc[30, "借阅量"] = 9999            # 离群值
df = pd.concat([df, df.iloc[5:8]], ignore_index=True)  # 3 行完全重复

out = r"d:/AI project/demo/study-log/data/borrow_records.csv"
df.to_csv(out, index=False, encoding="utf-8-sig")
print("已生成:", out, "| 行数:", len(df), "| 列数:", len(df.columns))
