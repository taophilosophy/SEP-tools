# SEP-tools

一些会用到的实用脚本，大部分由 ChatGPT 编写。



- czth.py 遍历指定文件夹中的所有文件，并且只保留其第一行的内容。（`python czth.py`）
- czthxhx.py 遍历指定文件夹中的所有文件，查找替换链接中的 `*\` 为正确的下划线。【请勿使用】
- czthxhx2.py 遍历指定文件夹中的所有文件，查找替换链接中的 `\_` 为正确的 `\`。【请勿使用】
- czthzhyh.py 如果找到了`<!--md-padding-ignore-begin-->` 就在文本的最后一行新建一行，内容为 `<!--md-padding-ignore-end-->`。
- jzqswj.py 检查 `<!--md-padding-ignore-begin-->` 和 `<!--md-padding-ignore-end-->` 是否成对出现。
- czxtscbt.py 对比文件 A 和 文件 B，查找 A 有而 B 无的内容，输出到 A 所在路径下的 diff.md，并过滤掉任何以以 `* [\*` 开头的行，并无视以这些开头的行前面的空格。用法示例：`czxtscbt.py C:\Users\ykla\Desktop\SUMMARY.md  C:\Users\ykla\Desktop\mu-lu-s.md` （优先使用 `zhczth.py`）
- zhczth.py 在 `czxtscbt.py` 的基础上对输出按 A 文件进行排序（优先使用本脚本）
- scdian.py 自动删除二级标题到六级标题之间的数字编号。默认路径为 `C:\\Users\\ykla\\Documents\\GitHub\\SEP-CN`