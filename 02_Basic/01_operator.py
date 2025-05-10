# 賦值
a = "hello"
b = 1
c = [1]

# 算數 先乘除後加減
a = 1 + 2
b = 2 - 3
c = 3 * 4
d = 4 / 5
e = 5 // 6  # 求整
f = 6 % 7  # 餘
g = 7**8  # 次方
print(a, b, c, d, e, f, g)  # 3 -1 12 0.8 0 6 5764801
h = 9**0.5  # 開根號
print(h)  # 3.0

# 比較
print(a < b)
print(b > c)
print(c != d)
print(d == e)


# 邏輯
t = True
f = False
print(t & f)  # False
print(t and f)
print(t | f)
print(t or f)  # True
print(not t)  # False


# in 、 is
a = 2
b = 4
c = [1, 2, 3]
print(a in c)  # True c 是否包含 a
print(b in c)  # False

x = [1, 2, 3]
y = [1, 2, 3]
z = x
print(x is y)  # False x、y是否是相同物件
print(x is z)  # True

# 位元
print(4 & 5)  # 4 且:有0為0
print(4 | 5)  # 5 或:有1為1
print(4 ^ 5)  # 1 互斥或:奇1為1
print(~4)  # -5 位元 相反
print(4 >> 2)  # 1 位元 右移，將二進位數字往右移動指定位數，左側補 0
print(5 << 2)  # 20 位元 左移，將二進位數字往左移動指定位數，右側補 0
