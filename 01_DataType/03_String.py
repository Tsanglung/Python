print("hello")  # hello
print("hello")  # hello

# 多行，連續3個單/雙引號
a = """In a world where environmental responsibility critically 
underpins business success, understanding and aiming 
for carbon emissions, mainly from fossil fuel combustion, 
significantly contribute to global warming."""
print(a)

a = str(8765)
print(a)

# 轉義
a = """In a \t world where \'environmental responsibility\' critically 
underpins \\business\\ success, understanding and aiming 
for carbon emissions, mainly from fossil fuel combustion, \n
significantly contribute to global \"warming\"."""
print(a)
# \\:反斜線、\':單引號、\":雙引號、\n:換行、\t:tab

a = r"111\n222"  # r:不進行轉義
b = "111\n222"
print(a)  # 123\n456
print(b)

# 結合字串: +、放置
a = "hello"
b = "world"
c = a + " " + b + "!"
print(c)

a = "hello" " " "world" "!"
print(a)

# 重複
a = "hello" * 5
print(a)


# 取得字串、字元
a = "hello world !"
print(a[0])  # h ( 第一個字元 )
print(a[3])  # l ( 第四個字元 )
print(a[-1])  # ! ( 最後一個字元 )

a = "hello world !"
print(a[:])  # hello world ! ( 取出全部字元 )
print(a[5:])  #  world ! ( 從 5 開始到結束 )
print(a[:5])  # hello ( 從 0 開始到第 4 個 ( 5-1 ) )
print(a[5:10])  #  worl ( 從 5 開始到第 9 個 ( 10-1 ) )
print(a[5:-3])  #  worl ( 從 5 開始到倒數第 4 個 ( -3-1 ) )
print(a[5:10:2])  #  ol ( 從 5 開始到第 9 個，中間略過 2 個 )

print(len(a))  # 取得長度


# 拆分字串 split
a = "hello world, how are you?"
b = a.split(",")  # 以逗號「,」進行拆分
c = a.split(" ")  # 以空白字元「 」進行拆分
d = a.split()  # 不指定分隔符號，自動以空白字元進行拆分
print(b)  # ['hello world', ' how are you?']
print(c)  # ['hello', 'world,', 'how', 'are', 'you?']
print(d)  # ['hello', 'world,', 'how', 'are', 'you?']

# 替換 replace
a = "hello world !"
b = a.replace("hello", "HELLO")
c = a.replace("l", "L", 2)
print(b)  # HELLO world !( 所有的 hello 都被換成 HELLO )
print(c)  # heLLo world ! ( 前兩個 l 被換成 L )

# find 搜尋
a = "Hello wOrld ! hEllo earth ! hello Taiwan !"
b = a.find("ll")
print(b)  # ll ( 第一個 ll 在 2 的位置 )
b = a.count("Hello")
print(b)  # 1 ( 出現1 次 Hello)
b = a.startswith("Hello")
print(b)  # True  ( 開頭是 Hello )
b = a.isalnum()  # 是否只有字母和數字
print(b)  # False ( 裡面有驚嘆號 )
print(a.isalpha())  # 判斷字串中是否都是英文字母
print(a.isdigit())  # 判斷字串中是否都是數字
print(a.islower(), a.isupper())  # 判斷字串中是否都是小寫/大寫英文字母
# 字母變大寫、小寫、單字自首大寫、大小寫對調
print(a.upper(), a.lower(), a.title(), a.swapcase())

# 格式化 format
a = "hello {}, how are {}"
b = a.format("world ", "you ?")
print(b)
a = "hello {1}, how are {0}"  # 數字表示「填入資料的順序」
b = a.format("world ", "you ?")
print(b)
a = "hello {m}, how are {n}"  # 具名引數
b = a.format(m="world ", n="you ?")
print(b)

# f-string python-3.6
a = "world"
b = "you"
c = f"hello {a}, how are {b} !"
print(c)

# 補0測試
for i in range(1, 101):
    print(f"{i:03d}", end=" , ")  # 輸出001~100
