import os
import re

def process_line(line):
    # 匹配以 ##、###、####、#####、###### 开头的行
    match = re.match(r'^(#{2,6})\s*\d+(\.\d+)*\.?\s+(.*)', line)
    if match:
        prefix = match.group(1)  # ##、### 等
        content = match.group(3)  # 标题内容
        return f"{prefix} {content}\n"
    return line

def process_md_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    with open(file_path, 'w', encoding='utf-8') as file:
        for line in lines:
            file.write(process_line(line))

def traverse_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                process_md_file(file_path)

if __name__ == "__main__":
    directory = "C:\\Users\\ykla\\Documents\\GitHub\\SEP-CN"  # 替换为你的目录路径
    traverse_directory(directory)