# 繼承
class parents:
    def __init__(self):
        self.eye = 2
        self.ear = 2
        self.mouth = 1
        self.nose = 1
        self.hair = True
        self.hand = 2
        self.feet = 2

    def __money(self):  # 私有方法
        print("$10000")

    def getMoney(self):
        self.__money()


class father(parents):
    def __init__(self):
        super().__init__()  # super 不覆寫 父類別 全部屬性
        self.hair = False  # 屬性相同，才覆寫

    def gender(self):
        print("male")


class mother(parents):
    def gender(self):
        print("female")


class son(father, mother):  # 先讀取 father 再 mother，將father覆寫 mother同名方法
    def play(self):  # 自己的方法
        print("game")


human_1 = father()
human_2 = mother()
print(human_1.hair)
human_1.gender()
human_2.gender()
son1 = son()
print(son1.hair)  # 繼承老爸的光頭
son1.getMoney()
