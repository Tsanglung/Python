try:  # 使用 try，測試內容是否正確
    a = input("輸入數字：")
    print(a + 1)
except:  # 如果 try 的內容發生錯誤，就執行 except 裡的內容
    print("發生錯誤")

try:
    print(b)
except TypeError:
    print("型別發生錯誤")
except NameError:
    print("使用沒有被定義的對象")

try:
    a = int(input("輸入數字："))
    if a > 1:
        raise ValueError("數字不在範圍內")  # 或 assert False, '數字不在範圍內'
    print(a)
except ValueError as msg:  # 或except AssertionError as msg:
    print(msg)  # 如果輸入範圍外的數字或解析非 10 進位數字，執行這邊的程式
except:  # 其他錯誤，執行這邊的程式
    print("error.")
finally:
    print("continue...")  # 不論有沒有錯都會執行這行
