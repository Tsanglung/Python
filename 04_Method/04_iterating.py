a = list("12345")  # 將「字串、tuple、字典或集合」轉變成串列
b = dict(
    [["x", "100"], ["y", "200"], ["z", "300"]]
)  # 將「帶有鍵與值、兩個值的二維串列或 tuple、雙字元的字串串列或 tuple」轉變成字典
c = set({"x": 1, "y": 2, "z": 3})  # 將「串列、tuple、字串或字典」轉換為集合
d = tuple("12345")  # 將「串列、集合、字串或字典」轉換為數組

fs = frozenset({"x": 1, "y": 2, "z": 3})  # 建立一個「不可改變」的集合
print(fs)

enu = enumerate(
    {"a": 1, "b": 2, "c": 3}, start=2  # 第一項索引變2
)  # 將「串列、集合、tuple、字典」建立為可迭代並附加索引值的 enumerate 物件
print(list(enu))

it = iter({"a", "b", "c"})  # 將「串列、集合、tuple、字典」建立為可迭代的 iter 物件
print(
    next(it)
)  # 和 iter() 與 enumerate() 搭配，將 enumerate 和 iter 物件的內容「依序取出並移除」


# 迭代操作
a = range(1, 100, 10)  # range(start, stop, step)
print(list(a))  # [1, 11, 21, 31, 41, 51, 61, 71, 81, 91]

for i in range(1, 10, 2):
    print(i)  # 1 3 5 7 9
print(len(a))  # 取得串列、字典、集合、tuple 的長度

# map 依序處理可迭代物件的每個項目，處理後產生一個全新的物件
c = map(lambda x: x + 1, [1, 2, 3, 4, 5])
print(tuple(c))  # (2, 3, 4, 5, 6)

a = [1, 2, 3, 4]
b = [5, 6, 7]
c = [8, 9]
d = zip(
    a, b, c
)  # 將指定的可迭代物件，打包變成一個新的物件，新物件的長度與「最短」的一致
print(list(d))  # [(1, 5, 8), (2, 6, 9)]
