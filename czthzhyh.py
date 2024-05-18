import os

def find_md_files(directory):
    md_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))
    return md_files

def add_padding_to_md(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # 检查文件中是否存在 <!--md-padding-ignore-begin-->
    if '<!--md-padding-ignore-begin-->\n' in lines:
        # 获取原文本的最后一行
        last_line = lines[-1].strip()

        # 在原文本的最后一行后面添加指定内容
        lines.append('<!--md-padding-ignore-end-->\n')

        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(lines)
        print(f"已在文件 {file_path} 中添加内容。")
    else:
        print(f"文件 {file_path} 中不存在 <!--md-padding-ignore-begin-->，无需操作。")

def add_padding_to_all_md_files(directory):
    md_files = find_md_files(directory)
    for file in md_files:
        add_padding_to_md(file)

if __name__ == "__main__":
    directory = input("请输入要查找的目录路径：")
    add_padding_to_all_md_files(directory)
    print("已完成对所有.md文件的处理。")
