from datetime import date, time, datetime, timedelta, timezone

# 1. 取得今天的日期
today = date.today()
print("今天日期：", today)

# 2. 建立時間物件
t = time(14, 30, 0)
print("時間物件：", t)

# 3. 現在的日期與時間
now = datetime.now()
print("現在時間：", now)

# 4. 手動建立一個日期與時間
custom_dt = datetime(2025, 5, 10, 9, 0, 0)
print("自訂 datetime：", custom_dt)

# 5. 計算時間差（兩個 datetime 相減會得到 timedelta）
delta = now - custom_dt
print("距離自訂時間的差距：", delta)

# 6. 使用 timedelta 增加或減少時間
tomorrow = now + timedelta(days=1)
yesterday = now - timedelta(days=1)
print("明天：", tomorrow)
print("昨天：", yesterday)

# 7. 處理時區（+8 是台灣時間）
tw_timezone = timezone(timedelta(hours=8))
dt_with_tz = datetime.now(tw_timezone)
print("台灣時間（帶時區）：", dt_with_tz)

# 8. ISO 格式輸出
print("ISO 格式：", now.isoformat())

# 9. 自訂格式輸出
print("格式化時間：", now.strftime("%Y年%m月%d日 %H:%M:%S"))
