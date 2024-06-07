import os
import sys

# 获取当前脚本文件的名称
current_script = os.path.basename(__file__)

# 指定不删除的文件列表
keep_files = ["chat_score_log.txt", "console_log.txt", current_script]

for root, dirs, files in os.walk('.', topdown=False):
    print(f"当前目录: {root}")

    # 删除文件
    for file_name in files:
        file_path = os.path.join(root, file_name)
        if file_name not in keep_files:
            try:
                os.remove(file_path)
                print(f"已删除文件: {file_path}")
            except Exception as e:
                print(f"无法删除文件: {file_path}, 错误: {e}")
        elif os.path.getsize(file_path) == 0:
            try:
                os.remove(file_path)
                print(f"已删除空文件: {file_path}")
            except Exception as e:
                print(f"无法删除空文件: {file_path}, 错误: {e}")
        else:
            print(f"文件: {file_name}")

    # 删除空文件夹
    for dir_name in dirs:
        dir_path = os.path.join(root, dir_name)
        if not os.listdir(dir_path):  # 检查文件夹是否为空
            try:
                os.rmdir(dir_path)
                print(f"已删除空文件夹: {dir_path}")
            except Exception as e:
                print(f"无法删除空文件夹: {dir_path}, 错误: {e}")

    print()  # 空行分隔不同目录的输出
