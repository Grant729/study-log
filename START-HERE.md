# 🚀 第 0 周第 1 天启动清单（今天就能开干）

按顺序做，做完一项打一个勾。全程约 2~3 小时。

## ☑ 1. 导师对齐（已基本完成）

已知：实验室数据来源于多模态实验（脑电/眼动）。这属于图情"信息行为/用户体验"方向，与你的学习大方向（数据分析 + 统计 + 可视化）完全对口，不需要再深究。

剩余可选：以后方便时顺带问一句师兄师姐用什么语言/工具（大概率会用到 Git 和 R/Python），问到就补进 [week00.md](week00.md)。

## ☐ 2. GitHub 基建（60~90 分钟，保姆级教程见 [github-setup-guide.md](github-setup-guide.md)）

教程覆盖：注册账号 → 安装登录 GitHub Desktop → 把本文件夹原地变成仓库 → 第一次提交并发布 → 以后每天的 2 分钟流程 → 常见问题。

完成后验证：浏览器打开 `https://github.com/你的用户名/study-log` 能看到文件，主页贡献格子变绿。

## ☐ 3. R 环境确认（20 分钟）

1. 打开 RStudio，在 Console 里跑：
   ```r
   R.version.string        # 确认 R 版本（建议 4.3+）
   install.packages("tidyverse")   # 装好后续要用的核心包
   ```
2. 跑通一个两行代码的 hello world：
   ```r
   library(ggplot2)
   ggplot(iris, aes(Sepal.Length, Petal.Length)) + geom_point()
   ```
   能出图 = 环境 OK，顺便你已经画出了人生第一张 R 图 🎉

## ☐ 4. R 预习（30 分钟，可选但推荐）

打开 *R for Data Science*（免费在线版）：<https://r4ds.hadley.nz/>
浏览第 1 章，不用记，找找"R 和 Python 像不像"的感觉。

## ☐ 5. 收尾（10 分钟）

1. 在 [week00.md](week00.md) 的 D1 写下今天做了什么、导师对齐的答案、遇到什么问题。
2. commit + push，保持 GitHub 第一天就是绿的 ✅

---

明天（D2）任务预告：Git 核心命令实操 + R 语法速通第一天（变量/向量/类型）。
