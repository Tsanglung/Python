# tuple 建立後，不能修改內容

a = ["apple", "banana", "cherry", "dragon fruit", "elderberry", "fig", "grape"]
b = tuple(a)  # 轉成tuple

a0, a1, a2, a3, a4, a5, a6 = b
print(
    a0, a1, a2, a3, a4, a5, a6
)  # apple banana cherry dragon fruit elderberry fig grape

print(b[2])  # cherry

c = ("honeydew", "indian fig")
d = b + c
print(
    d
)  # ('apple', 'banana', 'cherry', 'dragon fruit', 'elderberry', 'fig', 'grape', 'honeydew', 'indian fig')
