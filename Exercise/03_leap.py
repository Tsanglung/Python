# 閏年

y = int(input("輸入年分:"))
if y % 4 == 0:  # 如果除以 4 能整除
    if y % 100 == 0:  # 如果除以 100 能整除
        if y % 400 == 0:  # 如果除以 400 能整除，就是閏年
            print(f"{y} 閏年")
        else:
            print(f"{y} 平年")
    else:
        print(f"{y} 閏年")
else:
    print(f"{y} 平年")
