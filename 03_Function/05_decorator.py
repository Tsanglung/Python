# 裝飾器
# 在不需要做任何代碼修改的前提下增加額外功能，裝飾器的返回值也是一個函式或類對象


def first(func):  # 接受另一個函式 func 做參數
    print("one")  # 先印 one
    return func  # 原封不動回傳 func 本身


def first_2(func):
    print("one_2")
    return func


@first  # 先執行 first，回傳原本 second 本身
@first_2

# 多個裝飾器，順序由下往上。先first_2再first
def second():  # 裝飾
    print("two")


second()
# one_2
# one
# two
