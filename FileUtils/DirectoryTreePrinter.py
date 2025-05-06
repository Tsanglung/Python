import os
#遞迴列出指定目錄（資料夾）底下的檔案與子目錄結構
#但會排除名為 name1 和 name2 的資料夾
def list_directory_tree(path, level=0):
    # 排除 node_modules 目錄
    if os.path.basename(path) == "node_modules":#需要排除的資料夾名稱
        return
    if os.path.basename(path) == "assets":
        return
    
    # 打印目錄名稱
    print("  " * level + "|-- " + os.path.basename(path))
    
    # 獲取目錄內容
    if os.path.isdir(path):
        for item in sorted(os.listdir(path)):
            item_path = os.path.join(path, item)
            # 遞迴處理子目錄
            list_directory_tree(item_path, level + 1)

# 使用範例
directory_path = "D:/Workspace-Root/App-Workspace/Expo/PetFeeding"  
list_directory_tree(directory_path)
