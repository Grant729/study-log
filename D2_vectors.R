books <- c(3, 5, 8, 12, 7, 15, 9)
typeof(books)
length(books)
books[3]
books[1:3]
books[c(1,7)]
books[-2]
books[books>8]
sum()
sum(books)
mean(books)
round(mean(books))
round(mean(books),3)
max(books)
codes <- c("G250", "G252", "G353", "G354", "G356")
codes[c(1,4)]
length(codes)
mix <- c(1, "图书情报")
typeof(mix)
b2 <- c(3, NA, 5)
sum(b2)
sum(b2, na.rm = TRUE)
seq(1, 12)
sort(books, decreasing = TRUE)
rep("G", 3)
