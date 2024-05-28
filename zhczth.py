import argparse
import os
import re

def find_nonexistent_lines(file_a, file_b, file_c):
    # 读取文本B中的所有行，存储在一个集合中
    with open(file_b, 'r', encoding='utf-8') as fb:
        lines_b = set(line.strip() for line in fb)

    # 打开文本A和输出文件C
    with open(file_a, 'r', encoding='utf-8') as fa, open(file_c, 'w', encoding='utf-8') as fc:
        for line in fa:
            stripped_line = line.strip()
            if stripped_line and stripped_line not in lines_b:
                fc.write(line)

def remove_lines_starting_with_regex(file_c):
    # 使用正则表达式匹配以 '* [\*' 开头的行，并删除这些行
    pattern = re.compile(r'^\s*\* \[\\.*')
    with open(file_c, 'r+', encoding='utf-8') as fc:
        lines = fc.readlines()
        fc.seek(0)
        for line in lines:
            if not pattern.match(line):
                fc.write(line)
        fc.truncate()

def main():
    parser = argparse.ArgumentParser(description="Find lines in file A that are not present in file B and save them to file C, then remove lines starting with specific regex from file C.")
    parser.add_argument('file_a', type=str, help="Path to the input file A")
    parser.add_argument('file_b', type=str, help="Path to the input file B")

    args = parser.parse_args()

    # 获取A所在路径
    file_a_dir = os.path.dirname(args.file_a)
    # 构建输出文件C的路径
    file_c = os.path.join(file_a_dir, 'diff.md')

    find_nonexistent_lines(args.file_a, args.file_b, file_c)
    remove_lines_starting_with_regex(file_c)

if __name__ == "__main__":
    main()
