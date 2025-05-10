a = set()  # 空集合
a = set(["apple", "banana", "cherry", "dragon fruit", "elderberry", "fig", "grape"])

print(a)  # {'banana', 'fig', 'grape', 'dragon fruit', 'cherry', 'elderberry', 'apple'}

a.add(0)
print(
    a
)  # {0, 'fig', 'apple', 'elderberry', 'cherry', 'dragon fruit', 'grape', 'banana'}
a.remove("dragon fruit")
print(a)  # {0, 'grape', 'apple', 'fig', 'cherry', 'elderberry', 'banana'}

a = {0, 1, 2, 3, 4, 5}
b = {1, 3, 5, 7, 9}
print(a.intersection(b))  # 交集 {1, 3, 5}
print(a & b)

print(a.union(b))  # 聯集 {0, 1, 2, 3, 4, 5, 7, 9}
print(a | b)

print(a.difference(b))  # 差集 {0, 2, 4}
print(a - b)

print(a.symmetric_difference(b))  # 對稱差集 {0, 2, 4, 7, 9}
print(a ^ b)
