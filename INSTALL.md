# Mermaid 图表渲染工具安装说明

## 依赖项

### 1. Node.js 和 npm
- 下载并安装 Node.js: https://nodejs.org/
- 安装后，在命令行中验证:
  ```
  node --version
  npm --version
  ```

### 2. mermaid-cli
安装 mermaid-cli (mmdc):
```
npm install -g @mermaid-js/mermaid-cli
```

验证安装:
```
mmdc --version
```

### 3. Python 3
- 确保已安装 Python 3.6+
- 验证: `python --version` 或 `python3 --version`

## 可选依赖 (针对 PDF 输出)

对于 PDF 输出，可能需要安装 Chromium:

### Windows
- mermaid-cli 会自动安装 Puppeteer 和 Chromium

### Linux (Ubuntu/Debian)
```bash
sudo apt-get install chromium-browser
```

### macOS
```bash
brew install chromium
```

## 安装问题解决

### Linux 沙盒问题
如果遇到沙盒错误，脚本会自动创建 `puppeteer-config.json` 配置文件。
也可以手动创建:

```json
{
  "args": ["--no-sandbox", "--disable-setuid-sandbox"],
  "executablePath": "/usr/bin/chromium"
}
```

### Windows 路径问题
如果 `mmdc` 命令未找到，请确保 npm 全局路径已添加到系统 PATH 环境变量中。

## 快速测试

1. 创建一个测试文件 `test.mmd`:
   ```mermaid
   graph TD
       A[开始] --> B{是否继续?}
       B -->|是| C[执行操作]
       B -->|否| D[结束]
       C --> D
   ```

2. 运行渲染:
   ```bash
   python render_mermaid.py test.mmd -o test.png
   ```

3. 检查生成的 `test.png` 文件。