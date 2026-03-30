# Mermaid Diagram Exporter - Quick Start Guide

## 🚀 One-line Description
A simple tool to convert Mermaid diagram files (.mmd) to images (PNG/SVG) or PDF.

## 📦 Quick Installation

### Windows Users
1. **Install Node.js** - Download from [nodejs.org](https://nodejs.org/)
2. **Install Mermaid CLI** - Open Command Prompt and run:
   ```
   npm install -g @mermaid-js/mermaid-cli
   ```
3. **Ensure Python 3.6+** - Most systems have it, otherwise download from [python.org](https://www.python.org/)

Or simply double-click `install_deps.bat` for automatic installation!

### Mac/Linux Users
Open terminal and run:
```bash
chmod +x install_deps.sh
./install_deps.sh
```

## 🎯 Quick Usage

### Basic Commands
```bash
# Convert test.mmd to test.png
python render_mermaid.py test.mmd -o test.png

# Convert to PDF
python render_mermaid.py test.mmd -f pdf -o test.pdf

# Batch convert all .mmd files in a folder
python render_mermaid.py your_folder -o output_folder
```

### Try It Now!
There's a sample file `example.mmd` in this directory. Run:
```bash
python render_mermaid.py example.mmd -o my_first_chart.png
```

## ⚙️ Common Options

| Option | Description | Example |
|--------|-------------|---------|
| `-o filename` | Output file name | `-o chart.png` |
| `-f format` | Output format: png/svg/pdf | `-f pdf` |
| `-t theme` | Color theme: default/dark/forest/neutral | `-t dark` |
| `-w width` | Image width in pixels | `-w 1200` |
| `-H height` | Image height in pixels | `-H 800` |

## 📁 File Structure

```
export_mmd/
├── render_mermaid.py    # Main program
├── example.mmd          # Sample diagram
├── install_deps.bat     # Windows installer
├── install_deps.sh      # Mac/Linux installer
├── README.md            # Detailed documentation (Chinese)
├── README_EN.md         # This document (English)
└── README_简单使用.md   # Simplified Chinese guide
```

## ❓ Troubleshooting

### 1. "mmdc not found"
Run: `npm install -g @mermaid-js/mermaid-cli`

### 2. "Python not found"
Download and install Python 3.6+, remember to check "Add Python to PATH"

### 3. PDF generation fails on Linux
Install Chromium: `sudo apt-get install chromium-browser`

### 4. Still having issues?
Check the detailed documentation in `README.md`, or contact the developer!

## 💡 Tips

- Drag and drop files into the terminal window for quick path input
- Use `**/*.mmd` to match all .mmd files in subdirectories
- Add `--overwrite` to overwrite existing files

---

**Get started in one minute, master it in five! Start creating beautiful diagrams!** 🎨

> For advanced usage, see the `README.md` file