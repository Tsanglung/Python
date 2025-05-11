# 生成式

# 1. 串列生成式
a = [i * i for i in range(1, 10)]
print(a)  # [1, 4, 9, 16, 25, 36, 49, 64, 81]

a = [i + str(j) for i in "abc" for j in range(1, 4)]  # 雙重迴圈
print(a)  # ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']

# 搭配 if
a = [i for i in range(1, 10) if i % 2 == 0]
print(a)  # [2, 4, 6, 8]

# 三元運算
a = [i if i % 2 == 0 else "odd" for i in range(1, 10)]
print(a)  # ['odd', 2, 'odd', 4, 'odd', 6, 'odd', 8, 'odd']

# 2. 字典生成式
a = {i: i * i for i in range(1, 10)}
print(a)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

# 3.集合生成式
a = {i * i for i in range(1, 10)}
print(a)  # {64, 1, 4, 36, 9, 16, 49, 81, 25}

# 4. tuple 生成式
a = tuple(i for i in range(10))
print(a)  # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
