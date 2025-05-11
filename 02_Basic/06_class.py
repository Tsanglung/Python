# 物件類別


class empty:  # pass建立空類別
    pass


class mouse:  # 鼠類別
    def __init__(self, age):  # 預設屬性、age參數
        self.eye = 2  # 眼睛
        self.ear = 2  # 耳朵
        self.nose = 1  # 鼻子
        self.mouth = 1  # 嘴吧
        self.fur = True  # 有毛皮
        self.age = age

    def fur_color(self, color):  # 自訂義屬性
        print(color)

    @property  # 唯讀屬性
    def tail(self):
        return 1


mouse.feet = 4  # 外部定義屬性 4隻腳

guinea_pig = mouse(3)  # 天竺鼠
print(guinea_pig.fur)
guinea_pig.fur_color("yellow")
print(guinea_pig.feet, guinea_pig.tail)

gray_mouse = mouse(10)
print(gray_mouse.age)
