import os
import tkinter as tk
from tkinter import filedialog

def keep_first_line_only(folder_path):
    # 遍历文件夹中的所有文件
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            # 对于每个文件，读取第一行内容并覆盖原文件
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                first_line = f.readline().strip()
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(first_line)

def browse_button():
    # 打开文件夹选择对话框
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        keep_first_line_only(folder_selected)
        status_label.config(text="处理完成！")

def close_window():
    root.destroy()

# 创建GUI窗口
root = tk.Tk()
root.title("保留第一行")

# 使窗口无边框
root.overrideredirect(True)

# 获取屏幕的宽度和高度
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# 设置窗口的宽度和高度
window_width = 300
window_height = 200

# 计算窗口的左上角坐标
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

# 设置窗口的初始位置和大小
root.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

# 添加文件夹选择按钮
browse_button = tk.Button(root, text="选择文件夹", command=browse_button)
browse_button.pack(pady=20)

# 添加退出按钮
exit_button = tk.Button(root, text="退出", command=close_window)
exit_button.pack(pady=10)

# 添加状态标签
status_label = tk.Label(root, text="")
status_label.pack()

# 鼠标按下时的坐标
def on_mouse_down(event):
    root.x = event.x
    root.y = event.y

# 鼠标移动时拖动窗口
def on_mouse_move(event):
    deltax = event.x - root.x
    deltay = event.y - root.y
    x = root.winfo_x() + deltax
    y = root.winfo_y() + deltay
    root.geometry("+%s+%s" % (x, y))

# 鼠标释放时重置坐标
def on_mouse_up(event):
    root.x = None
    root.y = None

# 绑定鼠标事件
root.bind("<Button-1>", on_mouse_down)
root.bind("<B1-Motion>", on_mouse_move)
root.bind("<ButtonRelease-1>", on_mouse_up)

# 运行主循环
root.mainloop()
