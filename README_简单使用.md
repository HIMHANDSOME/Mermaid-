# Mermaid 图表导出工具 - 简单使用指南

## 🚀 一句话介绍
这是一个将 Mermaid 图表文件 (.mmd) 转换成图片 (PNG/SVG) 或 PDF 的小工具。

## 📦 快速安装

### Windows 用户
1. **安装 Node.js** - 从 [nodejs.org](https://nodejs.org/) 下载安装
2. **安装 Mermaid 工具** - 打开命令提示符，输入：
   ```
   npm install -g @mermaid-js/mermaid-cli
   ```
3. **确保有 Python** - 大多数电脑已自带，没有的话从 [python.org](https://www.python.org/) 安装

或者直接双击运行 `install_deps.bat` 自动安装！

### Mac/Linux 用户
打开终端，运行：
```bash
chmod +x install_deps.sh
./install_deps.sh
```

## 🎯 快速使用

### 基本命令
```bash
# 把 test.mmd 变成 test.png
python render_mermaid.py test.mmd -o test.png

# 变成 PDF
python render_mermaid.py test.mmd -f pdf -o test.pdf

# 批量转换文件夹里所有 .mmd 文件
python render_mermaid.py 你的文件夹 -o 输出文件夹
```

### 试试看！
当前目录有一个示例文件 `example.mmd`，运行：
```bash
python render_mermaid.py example.mmd -o 我的第一个图表.png
```

## ⚙️ 常用选项

| 选项 | 说明 | 例子 |
|------|------|------|
| `-o 文件名` | 指定输出文件 | `-o 图表.png` |
| `-f 格式` | 输出格式：png/svg/pdf | `-f pdf` |
| `-t 主题` | 颜色主题：default/dark/forest/neutral | `-t dark` |
| `-w 宽度` | 图片宽度（像素） | `-w 1200` |
| `-H 高度` | 图片高度（像素） | `-H 800` |

## 📁 文件结构说明

```
导出mmd/
├── render_mermaid.py    # 主程序
├── example.mmd          # 示例图表
├── install_deps.bat     # Windows安装脚本
├── install_deps.sh      # Mac/Linux安装脚本
├── README.md            # 详细文档
└── README_简单使用.md   # 本文档
```

## ❓ 遇到问题？

### 1. "mmdc 未找到"
运行：`npm install -g @mermaid-js/mermaid-cli`

### 2. "Python 未找到"
下载安装 Python 3.6+，安装时记得勾选 "Add Python to PATH"

### 3. 在 Linux 上 PDF 生成失败
安装 Chromium：`sudo apt-get install chromium-browser`

### 4. 还是不行？
查看详细文档 `README.md`，或直接问开发者！

## 💡 小技巧

- 拖拽文件到命令提示符窗口可以快速输入文件路径
- 使用 `**/*.mmd` 可以匹配所有子目录中的 .mmd 文件
- 加 `--overwrite` 可以覆盖已存在的文件

---

**一分钟上手，五分钟精通！开始制作你的漂亮图表吧！** 🎨

> 更多高级用法请查看 `README.md` 文件