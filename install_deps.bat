@echo off
echo 正在安装 Mermaid 图表渲染工具依赖...
echo.

echo 1. 检查 Node.js 是否安装...
node --version >nul 2>&1
if %errorlevel% neq 0 (
    echo 错误: Node.js 未安装
    echo 请从 https://nodejs.org/ 下载并安装 Node.js
    pause
    exit /b 1
)
echo Node.js 已安装

echo.
echo 2. 安装 mermaid-cli (mmdc)...
npm install -g @mermaid-js/mermaid-cli
if %errorlevel% neq 0 (
    echo 错误: mermaid-cli 安装失败
    pause
    exit /b 1
)
echo mermaid-cli 安装成功

echo.
echo 3. 检查 Python 是否安装...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    python3 --version >nul 2>&1
    if %errorlevel% neq 0 (
        echo 警告: Python 未安装
        echo 请从 https://www.python.org/ 下载并安装 Python 3.6+
    ) else (
        echo Python 3 已安装
    )
) else (
    echo Python 已安装
)

echo.
echo 依赖安装完成!
echo.
echo 测试命令:
echo   python render_mermaid.py example.mmd -o example.png
pause