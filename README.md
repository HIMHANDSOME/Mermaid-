# Mermaid 图表渲染工具

一个 Python 脚本，用于将 Mermaid (.mmd) 文件渲染为 PNG、SVG 或 PDF 格式的图片。

## 功能特性

- 支持单个文件、目录或 glob 模式
- 输出格式: PNG、SVG、PDF
- 多种主题: default、dark、forest、neutral
- 可自定义背景颜色、宽度和高度
- 递归查找子目录中的 .mmd 文件
- 支持 Windows、Linux、macOS

## 快速开始

### 1. 安装依赖

#### Windows
双击运行 `install_deps.bat` 或手动安装:
- 安装 [Node.js](https://nodejs.org/)
- 安装 mermaid-cli: `npm install -g @mermaid-js/mermaid-cli`
- 确保 Python 3.6+ 已安装

#### Linux/macOS
运行安装脚本:
```bash
chmod +x install_deps.sh
./install_deps.sh
```

### 2. 基本使用

渲染单个文件:
```bash
python render_mermaid.py example.mmd -o example.png
```

渲染整个目录:
```bash
python render_mermaid.py ./docs -f pdf -o ./output
```

使用 glob 模式:
```bash
python render_mermaid.py "**/*.mmd" -o ./rendered
```

## 命令行选项

```
usage: render_mermaid.py [-h] [-o OUTPUT] [-f {png,svg,pdf}]
                         [-t {default,dark,forest,neutral}]
                         [-b BACKGROUND] [-w WIDTH] [-H HEIGHT]
                         [--no-recursive] [--overwrite]
                         input

位置参数:
  input                 输入文件、目录或 glob 模式

可选参数:
  -h, --help            显示帮助信息
  -o OUTPUT, --output OUTPUT
                        输出文件或目录路径
  -f {png,svg,pdf}, --format {png,svg,pdf}
                        输出格式 (默认: png)
  -t {default,dark,forest,neutral}, --theme {default,dark,forest,neutral}
                        主题 (默认: default)
  -b BACKGROUND, --background BACKGROUND
                        背景颜色 (默认: white)
  -w WIDTH, --width WIDTH
                        图片宽度 (像素)
  -H HEIGHT, --height HEIGHT
                        图片高度 (像素)
  --no-recursive        不递归查找子目录中的文件
  --overwrite           覆盖已存在的输出文件
```

## 示例

### 示例 1: 渲染为 PDF
```bash
python render_mermaid.py diagram.mmd -f pdf -o diagram.pdf
```

### 示例 2: 使用暗色主题
```bash
python render_mermaid.py flowchart.mmd -t dark -o flowchart.png
```

### 示例 3: 自定义尺寸
```bash
python render_mermaid.py architecture.mmd -w 1600 -H 900 -o architecture.png
```

### 示例 4: 批量处理目录
```bash
python render_mermaid.py ./mermaid_diagrams -f svg -o ./rendered_svg
```

## 高级用法

### 在 Python 代码中使用

```python
from render_mermaid import render_mermaid

# 渲染单个图表
success = render_mermaid(
    input_file='diagram.mmd',
    output_file='diagram.png',
    format='png',
    theme='dark',
    width=1200,
    height=800
)
```

### 处理渲染错误

脚本会捕获渲染错误并继续处理其他文件。错误信息会显示在控制台中。

## 常见问题

### Q: 遇到 "mmdc not found" 错误
A: 确保 mermaid-cli 已正确安装:
```bash
npm install -g @mermaid-js/mermaid-cli
```

### Q: PDF 输出在 Linux 上失败
A: 安装 Chromium:
```bash
sudo apt-get install chromium-browser  # Ubuntu/Debian
```

### Q: 如何更改输出图片质量?
A: mermaid-cli 默认使用高质量渲染。如需更高控制，可考虑直接使用 mmdc 命令。

### Q: 支持哪些 Mermaid 图表类型?
A: 支持所有 Mermaid 图表类型: flowchart、sequence diagram、class diagram、state diagram、pie chart 等。

## 许可证

MIT