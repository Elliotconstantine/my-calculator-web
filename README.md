# 🧮 我的全栈计算器 (My Full-Stack Calculator)

一个基于 Python Flask 和原生前端技术栈打造的简易全栈计算器。支持加法运算，并能自动将计算历史记录持久化保存到本地数据库中<websource>source_group_web_2</websource>。

## ✨ 项目亮点

*   **前后端分离**：前端使用原生 HTML/CSS/JS，后端使用 Python Flask 提供 RESTful API。
*   **数据持久化**：集成 SQLite 数据库，自动保存每一次的计算记录，重启服务数据不丢失。
*   **模块化设计**：后端采用模块化架构，将数据库操作（db.py）与接口逻辑（app.py）解耦，代码清晰易维护。
*   **解决跨域问题**：内置 Flask-CORS 配置，完美支持前后端跨域数据交互<websource>source_group_web_3</websource>。

## 🛠️ 技术栈

*   **后端**：Python 3, Flask, Flask-CORS, SQLite
*   **前端**：HTML5, CSS3, JavaScript (Fetch API)
*   **工具**：Git, GitHub

## 🚀 快速开始

### 1. 环境准备
确保你的电脑上已经安装了 Python 3 环境。

### 2. 克隆与安装依赖
```bash
# 克隆项目到本地
git clone https://github.com/Elliotconstantine/my-calculator-web.git
cd my-calculator-web

# 安装 Python 依赖
pip install flask flask-cors

# 运行后端服务
在终端执行以下命令启动 Flask 后端：
python app.py

# 启动前端页面
直接在浏览器中打开项目根目录下的 index.html 文件，或者使用 VS Code 的 Live Server 插件打开，即可看到计算器界面。