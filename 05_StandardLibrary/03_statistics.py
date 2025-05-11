import statistics as stats

data_odd = [10, 20, 30, 40, 50]
data_even = [10, 20, 30, 40]
data_grouped = [1, 1, 2, 2, 2, 3, 4, 5]

print("資料（奇數筆）：", data_odd)
print("資料（偶數筆）：", data_even)
print("資料（分組範例）：", data_grouped)
print()

# 平均值
print("1. 平均值 mean():", stats.mean(data_odd))

# 中位數（奇數）
print("2. 中位數 median():", stats.median(data_odd))

# 中位數（偶數：低與高）
print("3. median_low()：", stats.median_low(data_even))
print("4. median_high()：", stats.median_high(data_even))

# 分組中位數
print("5. median_grouped()：", stats.median_grouped(data_grouped))

# 眾數
print("6. 眾數 mode()：", stats.mode(data_grouped))
print()

# 樣本標準差與變異數（用於統計推論時使用的樣本）
print("7. 樣本標準差 stdev()：", stats.stdev(data_odd))
print("8. 樣本變異數 variance()：", stats.variance(data_odd))
print()

# 母體標準差與變異數（用於整個母體資料）
print("9. 母體標準差 pstdev()：", stats.pstdev(data_odd))
print("10. 母體變異數 pvariance()：", stats.pvariance(data_odd))
