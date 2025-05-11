c = str(input("輸入 cm ( 公分 ) 或 ich ( 英吋 )："))
length = int(input("輸入長度數值："))

print("|公分   |公尺    |英吋")
print("|-----|-----|-----|")

if c == "cm":
    print("|", end="")  # 印出表格左側的框線
    print(f"{str(length):<5.5s}", end="|")
    print(f"{str(length*0.01):<5.5s}", end="|")
    print(f"{str(length*0.394):<5.5s}", end="|")
else:
    print("|", end="")
    print(f"{str(length*2.54):<5.5s}", end="|")
    print(f"{str(length*0.0254):<5.5s}", end="|")
    print(f"{str(length):<5.5s}", end="|")
