import random

# 設定種子
random.seed(42)

print("1. random(): 產生 0.0～1.0 之間的隨機浮點數")
print(random.random())
print()

print("2. uniform(10, 20): 產生 10～20 的隨機浮點數")
print(random.uniform(10, 20))
print()

print("3. randint(1, 100): 產生 1～100 的隨機整數")
print(random.randint(1, 100))
print()

print("4. randrange(1, 20, 2): 產生 1～20 間隔為 2 的隨機整數（奇數）")
print(random.randrange(1, 20, 2))
print()

# 一組獎品清單
prizes = ["iPad", "筆電", "耳機", "禮券", "滑鼠"]

print("5. choice(prizes): 隨機抽一個獎品")
print(random.choice(prizes))
print()

print("6. choices(prizes, k=3): 隨機抽 3 個獎品（可重複）")
print(random.choices(prizes, k=3))
print()

print("7. sample(prizes, k=3): 隨機抽 3 個獎品（不重複）")
print(random.sample(prizes, k=3))
print()

print("8. shuffle(prizes): 將獎品清單順序打亂")
random.shuffle(prizes)
print(prizes)
