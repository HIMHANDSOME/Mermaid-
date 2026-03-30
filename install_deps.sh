#!/bin/bash

echo "正在安装 Mermaid 图表渲染工具依赖..."
echo

echo "1. 检查 Node.js 是否安装..."
if ! command -v node &> /dev/null; then
    echo "错误: Node.js 未安装"
    echo "请从 https://nodejs.org/ 下载并安装 Node.js"
    exit 1
fi
echo "Node.js 已安装"

echo
echo "2. 安装 mermaid-cli (mmdc)..."
if ! command -v mmdc &> /dev/null; then
    npm install -g @mermaid-js/mermaid-cli
    if [ $? -ne 0 ]; then
        echo "错误: mermaid-cli 安装失败"
        exit 1
    fi
    echo "mermaid-cli 安装成功"
else
    echo "mermaid-cli 已安装"
fi

echo
echo "3. 检查 Python 是否安装..."
if ! command -v python3 &> /dev/null && ! command -v python &> /dev/null; then
    echo "警告: Python 未安装"
    echo "请从 https://www.python.org/ 下载并安装 Python 3.6+"
else
    echo "Python 已安装"
fi

echo
echo "4. 对于 Linux 系统，可能需要安装 Chromium..."
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    if ! command -v chromium &> /dev/null && ! command -v chromium-browser &> /dev/null; then
        echo "建议安装 Chromium 以获得更好的 PDF 支持:"
        echo "  Ubuntu/Debian: sudo apt-get install chromium-browser"
        echo "  Fedora: sudo dnf install chromium"
        echo "  Arch: sudo pacman -S chromium"
    else
        echo "Chromium 已安装"
    fi
fi

echo
echo "依赖安装完成!"
echo
echo "测试命令:"
echo "  python3 render_mermaid.py example.mmd -o example.png"
echo "  或"
echo "  python render_mermaid.py example.mmd -o example.png"