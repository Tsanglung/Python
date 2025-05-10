import os
import subprocess
#自動將某個資料夾底下的所有子資料夾壓縮成 .rar 檔
def compress_subfolders_to_rar(parent_folder_path):
    winrar_path = r"C:\Program Files\WinRAR\WinRAR.exe"  # WinRAR 的安裝路徑，請確認安裝位置

    # 遍歷父資料夾下的每個子資料夾
    for folder_name in os.listdir(parent_folder_path):
        folder_path = os.path.join(parent_folder_path, folder_name)
        if os.path.isdir(folder_path):  # 確保是資料夾
            output_rar_path = os.path.join(parent_folder_path, f"{folder_name}.rar")
            command = f'"{winrar_path}" a -r "{output_rar_path}" "{folder_path}\\*"'
            subprocess.run(command, shell=True, check=True)
            print(f"資料夾已成功壓縮成 {output_rar_path}")

# 設定父資料夾的路徑
parent_folder_path = r"C:\Users\Administrator\Downloads"
compress_subfolders_to_rar(parent_folder_path)
