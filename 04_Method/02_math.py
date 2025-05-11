a = int("123")
b = int("123", base=8)
print(a, b)  # 123 83

c = abs(-123)  # 絕對值
print(c)

a = divmod(10, 6)  # 回傳一個內容為「( x//y, x%y ) 的 tuple」
b = divmod(27, 3)
print(a)  # (1,4)
print(b)  # (9,0)

a = (9, 8, 55)
# 取最大、最小、次方pow、和
print(max(a), min(a), pow(c, 2), sum(a))

fa = 3.14159
print(round(fa, 3))  # 四捨五入後的 fa，小數後第3位四捨五入

c1 = complex(3, -5)  # 複數
print(c1)
