maptable = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}  # 羅馬數字對應阿拉伯數字

# 阿拉伯數字對應羅馬數字（有順序）
map_table = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
]


def convert_to_roman(s):
    roman = [i for i in s]
    r_roman = roman[::-1]  # 反轉串列
    ans = maptable[r_roman[0]]
    for i in range(1, len(r_roman)):
        if maptable[r_roman[i]] < maptable[r_roman[i - 1]]:
            ans = ans - maptable[r_roman[i]]
        else:
            ans = ans + maptable[r_roman[i]]
    return ans


def convert_to_a(n):
    result = ""
    for val, symbol in map_table:
        while n >= val:
            result += symbol
            n -= val
    return result


inp = input("請輸入羅馬數字或阿拉伯數字：")

if inp.isdigit():
    num = int(inp)
    print("轉換成羅馬數字：", convert_to_a(num))
else:
    print("轉換成阿拉伯數字：", convert_to_roman(inp))
