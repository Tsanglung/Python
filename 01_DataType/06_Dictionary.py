# 字典
a = {"apple": "banana", "cherry": "dragon fruit", "elderberry": "fig"}
b = dict(a)
print(b)  # {'apple': 'banana', 'cherry': 'dragon fruit', 'elderberry': 'fig'}

# 讀取
a = {"apple": 1, "banana": 2, "cherry": 3, "dragon fruit": 4, 100: ["apple", "banana"]}
print(a)  # {'apple': 1, 'banana': 2, 'cherry': 3, 'dragon fruit': 4}
print(a["apple"])
print(a[100][0])  # apple
print(a.get("cherry"))  # 3
# 修改
a["apple"] = 50
print(
    a
)  # {'apple': 50, 'banana': 2, 'cherry': 3, 'dragon fruit': 4, 100: ['apple', 'banana']}
a[50] = ["a", "b", "c"]
print(  # 修改字典時，鍵不存在於字典中，會直接加入一個新的鍵和值
    a
)  # {'apple': 50, 'banana': 2, 'cherry': 3, 'dragon fruit': 4, 100: ['apple', 'banana'], 50: ['a', 'b', 'c']}

# 刪除
del a[50]
print(
    a
)  # {'apple': 50, 'banana': 2, 'cherry': 3, 'dragon fruit': 4, 100: ['apple', 'banana']}
b = a.pop(100)
print(
    a, b
)  #'{'apple': 50, 'banana': 2, 'cherry': 3, 'dragon fruit': 4} ['apple', 'banana']

# clear() 清空

# 結合
c = {1: 2, 2: 3}
a.update(c)
print(a)  # {'apple': 50, 'banana': 2, 'cherry': 3, 'dragon fruit': 4, 1: 2, 2: 3}

# 取得所有key、value
a_key = a.keys()
a_value = a.values()
print(
    a_key, a_value
)  # dict_keys(['apple', 'banana', 'cherry', 'dragon fruit', 1, 2]) dict_values([50, 2, 3, 4, 2, 3])
