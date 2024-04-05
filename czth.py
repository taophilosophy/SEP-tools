import os
import tkinter as tk
from tkinter import filedialog

def keep_first_line_only(folder_path):
    # 遍历文件夹中的所有文件
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            # 对于每个文件，读取第一行内容并覆盖原文件
            with open(file_path, 'r', encoding='utf-8') as f:
                first_line = f.readline().strip()
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(first_line)

def browse_button():
    # 打开文件夹选择对话框
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        keep_first_line_only(folder_selected)
        status_label.config(text="处理完成！")

# 创建GUI窗口
root = tk.Tk()
root.title("保留第一行")

# 添加文件夹选择按钮
browse_button = tk.Button(root, text="选择文件夹", command=browse_button)
browse_button.pack(pady=20)

# 添加状态标签
status_label = tk.Label(root, text="")
status_label.pack()

# 运行主循环
root.mainloop()
