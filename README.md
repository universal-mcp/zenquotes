Welcome to the **Universal MCP Zenquotes API**.
This project provides a starting point for your API application, generated automatically by **MCP CLI** to help you kickstart your development quickly.
---
## 📋 Prerequisites
Before you begin, ensure you have met the following requirements:
*   **Python 3.11+** (Recommended)
*   **[uv](https://github.com/astral-sh/uv)** installed globally (`pip install uv`)
---
## 🛠️ Setup Instructions
Follow these steps to get the development environment up and running:
### 1. Sync Project Dependencies
Navigate to the project root directory (where `pyproject.toml` is located).
```bash
uv sync
```
This command uses `uv` to install all dependencies listed in `pyproject.toml` into a virtual environment (`.venv`) located in the project root.
### 2. Activate the Virtual Environment
Activating the virtual environment ensures that you are using the project's specific dependencies and Python interpreter.
- On **Linux/macOS**:
```bash
source .venv/bin/activate
```
- On **Windows**:
```bash
.venv\\Scripts\\activate
```
### 3. Start the MCP Inspector
Use the MCP CLI to start the application in development mode.
```bash
mcp dev src/universal_mcp_zenquotes/mcp.py
```
The MCP inspector should now be running. Check the console output for the exact address and port.
---
## 🚀 Usage
Once the server is running, you can test the tools and interact with them.
---
## 📁 Project Structure
The generated project has a standard layout:
```
.
├── src/                  # Source code directory
│   └── universal_mcp_zenquotes/
│       ├── __init__.py
│       └──   mcp.py      # Server is launched here
│       └──   app.py      # Application tools are defined here
├── tests/                # Directory for project tests
├── .env                  # Environment variables (for local development)
├── pyproject.toml        # Project dependencies managed by uv
├── README.md             # This file
```
---
## ➡️ Next Steps
---
## 📄 License
---
_This project was generated using **MCP CLI** — Happy coding! 🚀_
