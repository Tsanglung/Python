# 加、減、乘、除、取整、餘、次方
print(2 + 3)
print(2 - 3)
print(2 * 3)
print(2 / 3)
print(2 // 3)  # 取整，無條件捨去小數
print(2 % 3)
print(2**3)

print(int(5.2))  # 將小數點無條件捨棄、數字字串轉換成數字，或布林值轉換成 1 或 0
print(float(5))  # 將整數、數字文字或布林值，轉換成浮點數

print(int("101", 2))  # 二進制 5
print(int("101", 8))  # 八進制 8
print(int("101", 16))  # 十六進制 257

# 底數

print(0b1111)  # 二進制 -> 15
print(0o1111)  # 八進制 ->  585
print(0x1111)  # 十六進制 -> 4369

# boolean
print(bool(True))
print(bool(False))
print(bool(1), bool(0))
