import calendar

# 1. 印出今年的整年份月曆
year = 2025
print(f"\n{year} 年：")
print(calendar.calendar(year))

# 2. 印出指定月份的月曆
month = 5
print(f"\n{year} 年 {month} 月：")
print(calendar.month(year, month))

# 3. 查詢某年是否為閏年
print(f"\n {year} 是閏年嗎？", calendar.isleap(year))

# 4. 計算 2000 到 2025 之間有幾個閏年
print(
    "2000～2025 共有", calendar.leapdays(2000, 2026), "個閏年。"
)  # 要包含 2025 要寫 2026

# 5. 查詢某天是星期幾
y, m, d = 2025, 5, 10
weekday = calendar.weekday(y, m, d)
print(f"{y}/{m}/{d} 星期 ", calendar.day_name[weekday])  # 星期幾中文可以自己定義對應表

# 6. 印出星期的縮寫
print("\n星期縮寫：", calendar.weekheader(3))

# 7. 查詢月份資訊
start_day, days_in_month = calendar.monthrange(year, month)
print(f"{year} 年 {month} 月的第一天是星期 {start_day}，共 {days_in_month} 天")

# 8. 修改每週的第一天為星期日（0 是星期一）
calendar.setfirstweekday(calendar.SUNDAY)
print("\n修改後的 2025 年 5 月月曆（星期日為第一天）：")
cal = calendar.TextCalendar()
print(cal.formatmonth(2025, 5))
