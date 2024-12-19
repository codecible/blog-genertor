# OpenAI文本生成器

这是一个简单的Python程序，可以根据用户提供的主题调用OpenAI API生成相关文本内容。

## 使用前准备

1. 确保已安装Python 3.7或更高版本

2. 安装项目依赖：   
    ```bash
    # 使用requirements.txt安装所有依赖
    pip install -r requirements.txt   
    ```

3. 设置OpenAI API密钥：   
    ```bash
   # Linux/Mac
   export OPENAI_API_KEY='你的API密钥'
   
   # Windows
   set OPENAI_API_KEY=你的API密钥   
   ```
   
   或者，你可以创建 `.env` 文件（推荐方式）：
   1. 复制 `.env.example` 文件并重命名为 `.env`
   2. 在 `.env` 文件中设置你的API密钥：
   ```text
   OPENAI_API_KEY=你的API密钥
   ```
   
   ## 环境变量配置
   
   项目使用 `.env` 文件管理环境变量，你可以在其中配置：
   - OPENAI_API_KEY: OpenAI API密钥（必需）
   - OPENAI_MODEL: 使用的模型（可选，默认为gpt-3.5-turbo）
   - MAX_TOKENS: 最大生成token数（可选，默认为1000）
   - TEMPERATURE: 生成文本的创造性程度（可选，默认为0.7）

## 使用方法

在命令行中运行以下命令：
python main.py "你的主题"