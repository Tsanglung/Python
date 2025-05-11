# 產生器
a = (i**2 for i in range(10))
for i in a:  # for 取出產生器的值，只能取一次，再取則無值
    print(i, end=" ")  # 0 1 4 9 16 25 36 49 64


def f(max):
    n = 0
    while n < max:  # yield 讓函數變成一個「可逐步執行」的 generator
        yield (n)  # 暫停執行，並返回 n，下次呼叫 next() 從 yield的下行繼續
        n = n + 1


g = f(10)  # 建立 產生器物件 g
a = []
b = []
for i in range(5):
    a.append(next(g))
for i in range(5):
    b.append(next(g))
print(a)  # [0, 1, 2, 3, 4]
print(b)  # [5, 6, 7, 8, 9]


# 找質數
def find(max):  #  函式
    s = set()  # 空集合
    for n in range(2, max):  # 從 range(2, max) 當中開始依序找質數
        if all(
            n % i > 0 for i in s
        ):  # 判斷如果 i 已經存在於集合，且除以集合中的值會有餘數 ( 整除表示非質數 )
            s.add(n)  # 將該數字加入集合 ( 表示質數 )
            yield n  #  yield 記錄狀態


print(*find(100))  # 結果
