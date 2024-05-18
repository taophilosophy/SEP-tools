import os

def find_md_files(directory):
    md_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))
    return md_files

def check_ignore_tags(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if '<!--md-padding-ignore-begin-->' in content and '<!--md-padding-ignore-end-->' not in content:
        return False, f"存在 <!--md-padding-ignore-begin-->，但不存在 <!--md-padding-ignore-end-->，文件路径：{file_path}"
    elif '<!--md-padding-ignore-end-->' in content and '<!--md-padding-ignore-begin-->' not in content:
        return False, f"存在 <!--md-padding-ignore-end-->，但不存在 <!--md-padding-ignore-begin-->，文件路径：{file_path}"
    else:
        return True, None

def check_ignore_tags_in_all_md_files(directory):
    md_files = find_md_files(directory)
    for file in md_files:
        result, message = check_ignore_tags(file)
        if not result and message:
            print(message)

if __name__ == "__main__":
    directory = input("请输入要查找的目录路径：")
    check_ignore_tags_in_all_md_files(directory)
    print("已完成对所有.md文件的检查。")
