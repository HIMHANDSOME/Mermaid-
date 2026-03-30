#!/usr/bin/env python3
"""
Mermaid 图表渲染工具
将 .mmd 文件转换为 PNG 或 PDF 格式的图片
依赖: Node.js 和 mermaid-cli (mmdc)
安装: npm install -g @mermaid-js/mermaid-cli
"""

import os
import sys
import argparse
import subprocess
import glob
from pathlib import Path
import tempfile
import shutil

def check_mmdc():
    """检查 mmdc 是否可用"""
    try:
        subprocess.run(['mmdc', '--version'],
                      capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def find_mmd_files(input_path):
    """查找所有 .mmd 文件"""
    mmd_files = []
    if os.path.isfile(input_path) and input_path.endswith('.mmd'):
        mmd_files.append(input_path)
    elif os.path.isdir(input_path):
        # 递归查找所有 .mmd 文件
        for root, dirs, files in os.walk(input_path):
            for file in files:
                if file.endswith('.mmd'):
                    mmd_files.append(os.path.join(root, file))
    else:
        # 尝试 glob 模式
        mmd_files = glob.glob(input_path, recursive=True)
        mmd_files = [f for f in mmd_files if f.endswith('.mmd')]

    return mmd_files

def render_mermaid(input_file, output_file, format='png', theme='default',
                  background='white', width=None, height=None):
    """
    使用 mmdc 渲染 Mermaid 图表

    参数:
        input_file: 输入 .mmd 文件路径
        output_file: 输出文件路径
        format: 输出格式 (png, svg, pdf)
        theme: 主题 (default, dark, forest, neutral)
        background: 背景颜色
        width: 图片宽度 (像素)
        height: 图片高度 (像素)
    """
    # 构建 mmdc 命令
    cmd = ['mmdc', '-i', input_file, '-o', output_file]

    # 添加格式选项
    if format:
        cmd.extend(['-e', format])

    # 添加主题选项
    if theme:
        cmd.extend(['-t', theme])

    # 添加背景颜色
    if background:
        cmd.extend(['-b', background])

    # 添加宽度和高度
    if width:
        cmd.extend(['-w', str(width)])
    if height:
        cmd.extend(['-H', str(height)])

    # 添加 puppeteer 配置以避免沙盒问题 (Linux 环境)
    if sys.platform.startswith('linux'):
        cmd.extend(['-p', 'puppeteer-config.json'])

    # 执行命令
    try:
        print(f"正在渲染: {input_file} -> {output_file}")
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        if result.stderr:
            print(f"警告: {result.stderr}")
        print(f"成功: {output_file}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"渲染失败: {input_file}")
        print(f"错误输出: {e.stderr}")
        print(f"命令: {' '.join(cmd)}")
        return False
    except Exception as e:
        print(f"未知错误: {str(e)}")
        return False

def create_puppeteer_config():
    """创建 puppeteer 配置文件以解决沙盒问题"""
    config = {
        "args": ["--no-sandbox", "--disable-setuid-sandbox"],
        "executablePath": "chromium" if shutil.which("chromium") else None
    }

    import json
    with open('puppeteer-config.json', 'w') as f:
        json.dump(config, f)

    return 'puppeteer-config.json'

def main():
    parser = argparse.ArgumentParser(
        description='将 Mermaid (.mmd) 文件渲染为 PNG 或 PDF 图片',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
使用示例:
  # 渲染单个文件为 PNG
  python render_mermaid.py input.mmd -o output.png

  # 渲染整个目录为 PDF
  python render_mermaid.py ./docs -f pdf -o ./output

  # 使用暗色主题，指定宽度
  python render_mermaid.py diagram.mmd -t dark -w 1200 -o diagram.png

  # 使用 glob 模式
  python render_mermaid.py "**/*.mmd" -o ./rendered

依赖:
  需要安装 Node.js 和 mermaid-cli:
    npm install -g @mermaid-js/mermaid-cli
"""
    )

    parser.add_argument('input', help='输入文件、目录或 glob 模式')
    parser.add_argument('-o', '--output', help='输出文件或目录路径')
    parser.add_argument('-f', '--format', choices=['png', 'svg', 'pdf'],
                       default='png', help='输出格式 (默认: png)')
    parser.add_argument('-t', '--theme',
                       choices=['default', 'dark', 'forest', 'neutral'],
                       default='default', help='主题 (默认: default)')
    parser.add_argument('-b', '--background', default='white',
                       help='背景颜色 (默认: white)')
    parser.add_argument('-w', '--width', type=int, help='图片宽度 (像素)')
    parser.add_argument('-H', '--height', type=int, help='图片高度 (像素)')
    parser.add_argument('--no-recursive', action='store_true',
                       help='不递归查找子目录中的文件')
    parser.add_argument('--overwrite', action='store_true',
                       help='覆盖已存在的输出文件')

    args = parser.parse_args()

    # 检查 mmdc 是否可用
    if not check_mmdc():
        print("错误: 未找到 mermaid-cli (mmdc)")
        print("请安装: npm install -g @mermaid-js/mermaid-cli")
        sys.exit(1)

    # 创建 puppeteer 配置文件 (如果需要)
    if sys.platform.startswith('linux'):
        create_puppeteer_config()

    # 查找输入文件
    if args.no_recursive and os.path.isdir(args.input):
        # 仅查找当前目录
        mmd_files = [os.path.join(args.input, f) for f in os.listdir(args.input)
                    if f.endswith('.mmd') and os.path.isfile(os.path.join(args.input, f))]
    else:
        mmd_files = find_mmd_files(args.input)

    if not mmd_files:
        print(f"未找到 .mmd 文件: {args.input}")
        sys.exit(1)

    print(f"找到 {len(mmd_files)} 个 .mmd 文件")

    # 准备输出路径
    output_specified = bool(args.output)

    # 处理每个文件
    success_count = 0
    for input_file in mmd_files:
        # 确定输出文件路径
        if output_specified:
            output_path = args.output
            # 如果输出路径是目录，则创建对应的输出文件名
            if os.path.isdir(output_path) or (not output_path.endswith(('.png', '.svg', '.pdf')) and not os.path.exists(output_path)):
                # 确保输出目录存在
                os.makedirs(output_path, exist_ok=True)
                # 基于输入文件名创建输出文件名
                input_name = os.path.splitext(os.path.basename(input_file))[0]
                output_file = os.path.join(output_path, f"{input_name}.{args.format}")
            else:
                output_file = output_path
                # 如果输出文件已存在且未指定覆盖，则跳过
                if os.path.exists(output_file) and not args.overwrite:
                    print(f"跳过: {output_file} 已存在 (使用 --overwrite 覆盖)")
                    continue
        else:
            # 未指定输出，使用输入文件同目录
            input_dir = os.path.dirname(input_file)
            input_name = os.path.splitext(os.path.basename(input_file))[0]
            output_file = os.path.join(input_dir, f"{input_name}.{args.format}")

        # 确保输出目录存在
        output_dir = os.path.dirname(output_file)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)

        # 渲染图表
        if render_mermaid(input_file, output_file, args.format, args.theme,
                         args.background, args.width, args.height):
            success_count += 1

    print(f"\n完成: 成功渲染 {success_count}/{len(mmd_files)} 个文件")

    # 清理临时配置文件
    if os.path.exists('puppeteer-config.json'):
        os.remove('puppeteer-config.json')

    if success_count == 0:
        sys.exit(1)

if __name__ == '__main__':
    main()