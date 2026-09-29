# %%
学院 <- c("信息管理", "计算机", "信息管理", "历史", "计算机", "信息管理", "历史", "计算机", "信息管理", "历史")
月份 <- c(1, 1, 2, 1, 2, 2, 3, 3, 3, 2)
借阅量 <- c(120, 200, 150, 80, 180, 160, 90, 220, 140, 100)
逾期数 <- c(5, 30, 8, 2, 25, 6, 3, 35, 9, 1)
df <- data.frame(学院, 月份, 借阅量, 逾期数)

# %%
df
str(df)
dim(df)
head(df)
head(df, 3)
summary(df)

# %%
df[df$借阅量 > 150, ]
df[df$学院 == "信息管理", ]
df[df$学院 == "信息管理" & df$借阅量 > 150, ]
df[order(-df$借阅量), ]
head(df[order(-df$借阅量), ], 3)
aggregate(借阅量 ~ 学院, data = df, FUN = sum)
aggregate(借阅量 ~ 学院, data = df, FUN = mean)

# %%
library(dplyr)
df |>
  group_by(学院) |>
  summarise(
    每学院总借阅量 = sum(借阅量),
    每学院平均逾期数 = mean(逾期数)
  )

# %%
library(httpgd)
hgd()
plot(mtcars$wt, mtcars$mpg)
