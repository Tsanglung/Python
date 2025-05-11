import random

a = random.randint(1, 99)
count = 0

while True:
    try:
        b = int(input("輸入 1～99 的數字："))
        if b < 1 or b > 99:
            print("請輸入 1 到 99 的整數！")
            continue
        count += 1
        if b < a:
            print("太小！再試一次。")
        elif b > a:
            print("太大！再試一次。")
        else:
            print(f"正確！你總共猜了 {count} 次！")
            break
    except ValueError:
        print("請輸入有效的整數！")
