# ☁️ 全栈云计算器 (Full-Stack Cloud Calculator)

这是一个基于 **Flask** 后端和 **原生 HTML/JS** 前端的全栈计算器应用。它部署在 **PythonAnywhere** 上，支持基本的四则运算，并能将计算历史持久化存储在服务器的 JSON 文件中。

## ✨ 功能特点

- **基本运算**：支持加（+）、减（-）、乘（*）、除（/）四则运算。
- **历史记录**：自动保存每一次的计算记录，包含时间戳和计算详情。
- **数据持久化**：使用 `history.json` 本地存储，即使重启服务器，历史记录也不会丢失。
- **前后端分离**：前端通过 `fetch` API 与后端进行异步数据交互。
- **跨域支持**：集成了 `Flask-CORS`，完美支持跨域请求。

## 🛠️ 技术栈

- **前端**：HTML5, CSS3, JavaScript (ES6+)
- **后端**：Python 3, Flask
- **数据存储**：JSON 文件
- **部署平台**：PythonAnywhere (后端), GitHub Pages (前端)

## 📂 项目结构

```text
.
├── app.py              # Flask 后端主程序（路由与逻辑）
├── db.py               # 数据库模块（负责历史记录的读写）
├── history.json        # 持久化存储的历史记录文件
├── index.html          # 前端页面（包含样式与交互逻辑）
└── README.md           # 项目说明文档