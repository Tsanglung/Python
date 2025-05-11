import time

# 1. 取得目前時間的秒數（從 1970/1/1 開始的秒數）
now_seconds = time.time()
print("目前時間（秒數）:", now_seconds)

# 2. 使用 sleep 暫停程式
for i in range(2):
    print(f"\r倒數 {2-i} 秒", end="")
    time.sleep(1)

# 3. 轉換為本地時間字串
print("本地時間：", time.ctime(now_seconds))

# 4. 轉為 struct_time 格式（本地時間和 UTC 時間）
local = time.localtime(now_seconds)
utc = time.gmtime(now_seconds)
print("Local struct_time：", local)
print("UTC struct_time：", utc)

# 5. struct_time 轉秒數
re_seconds = time.mktime(local)
print("轉回秒數：", re_seconds)

# 6. struct_time 轉為文字時間
asctime_text = time.asctime(local)
print("文字時間（asctime）：", asctime_text)

# 7. 使用 strftime 格式化時間
formatted = time.strftime("%Y-%m-%d %H:%M:%S", local)
print("格式化時間：", formatted)

# 8. 使用 strptime 解析字串為時間格式
parsed_time = time.strptime("2025-05-10 12:00:00", "%Y-%m-%d %H:%M:%S")
print("解析後的 struct_time：", parsed_time)
