import os
import re

def replace_links_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.readlines()

    # 使用正则表达式进行替换，但不处理以 # 开头的行
    for i, line in enumerate(content):
         if "http" in line and not line.startswith("#"):
            content[i] = re.sub(r'\\_', r'\\', line)  # 将 \_ 替换为 \
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(content)

def traverse_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            if file_name.endswith('.md'):  # 只处理文本文件
                file_path = os.path.join(root, file_name)
                replace_links_in_file(file_path)

if __name__ == "__main__":
    directory_path = input("请输入要遍历的文件夹路径：")
    traverse_directory(directory_path)
    print("链接替换完成！")
