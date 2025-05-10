a = 1  # 將 1 放入物件 a
print(a)
b = c = a  # 讓物件 b、c  = a
print(a, b, c)

a, b, c = 1, 2, 3  # 一行設定三變數
print(a, b, c)

# 多變數同時賦值
a = []
b = a
a.append(1)  # 修改 a 串列內容
print(a)  # [1]
print(b)  # [1]   # 被影響

c = []
d = c
c = [1]
print(c)  # [1]
print(d)  # []    # 不受影響

# 交換變數名稱
a, b, c = 1, 2, 3
print(a, b, c)
a, b, c = b, c, a  # 交換內容
print(a, b, c)

# 全域、區域變數
global_a = 1


def two():
    local_a = 2
    print(local_a)


two()
print(global_a)
