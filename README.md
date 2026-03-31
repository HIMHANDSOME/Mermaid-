# Mermaid 图表渲染工具

一个 Python 脚本，用于将 Mermaid (.mmd) 文件渲染为 PNG、SVG 或 PDF 格式的图片。

## 功能特性

- 支持单个文件、目录或 glob 模式
- 输出格式: PNG、SVG、PDF
- 多种主题: default、dark、forest、neutral
- 可自定义背景颜色、宽度和高度
- 递归查找子目录中的 .mmd 文件
- 支持 Windows、Linux、macOS

## 环境配置

### Conda 环境配置（可选）

如果你使用 Conda 管理 Python 环境，可以按照以下步骤创建并激活环境：

1. 创建新的 Conda 环境（Python 3.6+）：
   ```bash
   conda create -n mermaid-render python=3.8
   ```

2. 激活环境：
   ```bash
   conda activate mermaid-render
   ```

3. 本项目没有额外的 Python 包依赖，只需要确保 Node.js 和 mermaid-cli 已安装（见下方安装依赖）。

### PyCharm 项目配置

如果你使用 PyCharm 进行开发，可以按以下步骤配置：

1. **打开项目**：在 PyCharm 中选择 "Open" 并打开本目录。
2. **设置 Python 解释器**：
   - 打开设置（File → Settings 或 Ctrl+Alt+S）
   - 进入 "Project: 导出mmd" → "Python Interpreter"
   - 点击齿轮图标，选择 "Add Interpreter" → "Conda Environment"
   - 选择 "Existing environment"，然后选择上面创建的 Conda 环境（或系统 Python 解释器）
3. **创建运行配置**：
   - 打开 `render_mermaid.py` 文件
   - 右键点击编辑器区域，选择 "Run 'render_mermaid'"
   - 或者点击右上角的运行配置下拉菜单，选择 "Edit Configurations"
   - 添加新的 Python 配置，脚本路径选择 `render_mermaid.py`
   - 在 "Parameters" 中可填写命令行参数，例如：`example.mmd -o example.png`
   - 工作目录设置为项目根目录

**提示**：在 PyCharm 的终端中使用 Conda 环境时，可能需要手动激活环境。可以在 PyCharm 的设置中，将终端路径设置为 Conda 环境的可执行文件（例如在 Windows 上为 `C:\Users\<用户名>\miniconda3\Scripts\activate.bat`）。

## 快速开始

### 1. 安装依赖

**注意**：无论使用 Conda 环境还是系统 Python，都需要安装以下依赖。如果使用了 Conda 环境，请确保在激活环境后安装 Node.js 和 mermaid-cli。

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
