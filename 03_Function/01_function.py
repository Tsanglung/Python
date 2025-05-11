def add(x, y=1):  # 參數預設值
    z = x + y
    print(z)


add(3, 5)  # 3+5 = 8
add(5)  # 5  + 1 = 6


def sub(x, y=-100):
    z = x - y
    return z


diff = sub(50)
print(diff)  # 150


def loop(a, start=0, end=10):
    for i in a[start:end]:
        print(i)


b = [9, 8, 7, 6, 5]
# 關鍵字引數
loop(b, start=3, end=len(b))  # 6 5
loop(b)  # 9 8 7 6 5


def args_test(
    *args,
):  # 帶有 args ( 一個星號 * ) 運算子的參數，則傳入的所有參數，都會被組合成 tuple 的型態
    print(args)


args_test("apple", "banana", "cherry")


def kwargs_test(
    **kwargs,
):  # 帶有 kwargs ( 兩個星號 ** ) 運算子的參數，則傳入的所有「帶有關鍵字引數」的參數，都會被組合成字典的型態
    print(kwargs)  # {'apple': 'red', 'banana': 'yellow', 'cherry': 'dark red'}


kwargs_test(apple="red", banana="yellow", cherry="dark red")
