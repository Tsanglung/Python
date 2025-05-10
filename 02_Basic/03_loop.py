for i in range(1, 101):
    print(f"{i:03d}", end=" , ")  # 輸出001~100


for a in ["a", "b", "c"]:
    if a == "c":
        break
    for b in [1, 2, 3]:
        print(f"{a}{b}")

for a in ["a", "b", "c"]:
    if a == "b":  # 略過 a 為 b 的部分，直接跳到 a 為 c 的部分。
        continue
    for b in [1, 2, 3]:
        print(f"{a}{b}")

a = 1
while a <= 3:
    print(a)
    a += 1
