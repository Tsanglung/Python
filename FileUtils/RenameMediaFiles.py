import os

def rename_files_in_directory(directory_path):
    # 定義圖片和影片的副檔名
    image_extensions = ['.png', '.jpg', '.jpeg', '.bmp', '.gif']
    video_extensions = ['.mp4', '.avi', '.mov', '.mkv', '.flv']

    # 走訪資料夾中的所有檔案
    for root, dirs, files in os.walk(directory_path):
        # 每次進入新資料夾時重置計數器
        image_count = 0
        video_count = 0

        for file in files:
            file_path = os.path.join(root, file)
            file_extension = os.path.splitext(file)[1].lower()

            if file_extension in image_extensions:
                image_count += 1
                new_file_name = f'P{image_count}{file_extension}'
                new_file_path = os.path.join(root, new_file_name)
                os.rename(file_path, new_file_path)
                print(f'Renamed {file} to {new_file_name}')
            
            elif file_extension in video_extensions:
                video_count += 1
                new_file_name = f'V{video_count}{file_extension}'
                new_file_path = os.path.join(root, new_file_name)
                os.rename(file_path, new_file_path)
                print(f'Renamed {file} to {new_file_name}')

# 指定要走訪的資料夾路徑
directory_path = r'C:\Users\Administrator\Downloads\Telegram Desktop'
rename_files_in_directory(directory_path)
