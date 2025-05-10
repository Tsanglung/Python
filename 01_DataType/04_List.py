# 有別於 tuple，串列的內容項目都是「可以修改」
# 建立串列
a = ["apple", "banana", "cherry"]
b = [1, 2, 3]
print(a, b)

a = ("apple", "banana", "cherry")
b = list(a)  # 建立一個「空的」串列，或將「可迭代」( 有順序 ) 的資料轉換成串列
c = list(a[0])
print(b, c)  # ['apple', 'banana', 'cherry'] ['a', 'p', 'p', 'l', 'e']

# 合併: +、extend()
a = ["apple", "banana", "cherry"]
b = [1, 2, 3]
c = a + b
a.extend(b)  # 改變串列，但不會回傳串列的值
print(
    c, a
)  # ['apple', 'banana', 'cherry', 1, 2, 3] ['apple', 'banana', 'cherry', 1, 2, 3]

# copy
a = ["apple", "banana", "cherry"]
b = a[:]  # 複製所有項目變成一個新串列
del a[1]
print(a, b)  # ['apple', 'cherry'] ['apple', 'banana', 'cherry']

# offset、slice() 修改串列
a = ["apple", "banana", "cherry"]
a[2] = "dragon fruit"
print(a)  # ['apple', 'banana', 'dragon fruit']
a[2:4] = ["elderberry", "fig", "grape"]
print(a)  # ['apple', 'banana', 'elderberry', 'fig', 'grape']

# append()、insert 增加項目
a = ["apple", "banana", "cherry"]
a.append("dragon fruit")
print(a)  # ['apple', 'banana', 'cherry', 'dragon fruit']
a.insert(3, "elderberry")
print(a)  # ['apple', 'banana', 'cherry', 'elderberry', 'dragon fruit']

# 刪除
a = ["apple", "banana", "cherry", "dragon fruit", "elderberry", "fig", "grape"]
del a[1]
print(a)  # ['apple', 'cherry', 'dragon fruit', 'elderberry', 'fig', 'grape']
a.remove("fig")
print(a)  # ['apple', 'cherry', 'dragon fruit', 'elderberry', 'grape']
b = a.pop(2)  # 取出並移除串列裡的一個項目
print(a, b)  # ['apple', 'cherry', 'elderberry', 'grape'] dragon fruit
a.clear()  # 清空整個串列
print(a)  # []

# 排序
a = [0, 3, 2, 1, 9, 6, 7, 8, 5]
b = sorted(a)  # 產生一個排序過後的新串列，因此「不會改變」原始的串列
print(a, b)  # [0, 3, 2, 1, 9, 6, 7, 8, 5] [0, 1, 2, 3, 5, 6, 7, 8, 9]
a.sort()
print(a)  # [0, 1, 2, 3, 5, 6, 7, 8, 9]
a.sort(reverse=True)
print(a)  # [9, 8, 7, 6, 5, 3, 2, 1, 0]

# 反轉
a = [0, 1, 2, 3, 4, 5]
b = a[::-1]
print(a)  # [0, 1, 2, 3, 4, 5]
print(b)  # [5, 4, 3, 2, 1, 0]
a.reverse()
print(a)  # [5, 4, 3, 2, 1, 0]
